import json
from ej2 import analize_from_file  # Importamos 'analize_from_file' desde 'ej2.py'

def print_words_from_json(json_path):
    # Leer el archivo JSON proporcionado.
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: El archivo {json_path} no existe.")
        return
    except json.JSONDecodeError:
        print(f"Error: El archivo {json_path} no tiene un formato JSON válido.")
        return

    # Extraer la lista de palabras únicas del análisis.
    # Las palabras únicas están en la clave "unicas" como un diccionario.
    vocabulario = data.get("unicas", {})

    # Imprimir la lista de palabras únicas.
    palabras_unicas = list(vocabulario.keys())
    print("Palabras únicas en el archivo de análisis:")
    for palabra in palabras_unicas:
        print(palabra)

