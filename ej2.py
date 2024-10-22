import json
from ej1 import analize  # Importamos la función 'analize' desde el archivo 'analize.py'

def analize_from_file(file_path, json_path=None):
    # Leer el contenido del archivo de texto.
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe.")
        return

    # Llamar a la función 'analize' que se desarrolló en el ejercicio 1.
    analysis_result = analize(text)

    # Si se proporciona una ruta de salida para el JSON, guardar el resultado.
    if json_path:
        try:
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(analysis_result, json_file, indent=4, ensure_ascii=False)
            print(f"Resultados guardados en {json_path}")
        except Exception as e:
            print(f"Error al escribir en el archivo {json_path}: {e}")
    else:
        # Si no se proporciona una ruta, imprimir el resultado en formato JSON.
        print(json.dumps(analysis_result, indent=4, ensure_ascii=False))
