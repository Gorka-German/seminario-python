import csv
import json

def analizar_trafico(csv_path, json_path='estadisticas.json'):
    # Inicializar el diccionario para almacenar las estadísticas
    estadisticas = {
        "total_entradas_salidas": 0,
        "velocidad_minima": float('inf'),
        "velocidad_maxima": float('-inf'),
        "velocidades": []  # Se usará para calcular la velocidad media
    }

    # Abrir el archivo CSV y leerlo línea por línea
    try:
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Asumimos que el CSV tiene las columnas "id_sistema" y "velocidad"
                id_sistema = row.get("id_sistema")
                velocidad = row.get("velocidad")

                # Contar las entradas/salidas si "id_sistema" no es None ni está vacío
                if id_sistema:
                    estadisticas["total_entradas_salidas"] += 1

                # Procesar la velocidad, si está presente y es válida
                try:
                    # Convertir la velocidad a float solo si no es None o vacía
                    if velocidad is not None and velocidad.strip() != "":
                        velocidad = float(velocidad)
                        estadisticas["velocidades"].append(velocidad)
                        # Actualizar la velocidad mínima y máxima
                        estadisticas["velocidad_minima"] = min(estadisticas["velocidad_minima"], velocidad)
                        estadisticas["velocidad_maxima"] = max(estadisticas["velocidad_maxima"], velocidad)
                except ValueError:
                    # Si no se puede convertir la velocidad a número, la ignoramos
                    continue

    except FileNotFoundError:
        print(f"Error: El archivo {csv_path} no se encontró.")
        return
    except Exception as e:
        print(f"Error al leer el archivo {csv_path}: {e}")
        return

    # Calcular la velocidad media si hay velocidades registradas
    if estadisticas["velocidades"]:
        estadisticas["velocidad_media"] = sum(estadisticas["velocidades"]) / len(estadisticas["velocidades"])
    else:
        # Si no hay velocidades, asignamos None para indicar ausencia de datos
        estadisticas["velocidad_media"] = None
        estadisticas["velocidad_minima"] = None
        estadisticas["velocidad_maxima"] = None

    # Eliminar la lista de velocidades ya que solo nos interesa la media para guardar el JSON
    estadisticas.pop("velocidades")

    # Guardar las estadísticas en un archivo JSON
    try:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(estadisticas, json_file, indent=4, ensure_ascii=False)
        print(f"Estadísticas guardadas en {json_path}")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Ejecución de la función con el archivo proporcionado
analizar_trafico('Alcoi_dades_trafic_2022_T4.csv')

