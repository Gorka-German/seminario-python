def analize(texto):
    d={}
    d["lineas"] = len(texto.splitlines())

    d["palabras"] = len(texto.split())
    
    d["caracteres"] = len(texto)

    d["unicas"] = {}

    lista_palabras = texto.split()

    for palabra in set(lista_palabras):
        d["unicas"][palabra] = lista_palabras.count(palabra)

    d["caracteres_unicos"] = {}

    
    minusculas = texto.replace("\n", "").replace(" ", "").lower()

    for caracter in set(texto):
        d["caracteres_unicos"][caracter] = minusculas.count(caracter)
    
    return d

resultado = analize("Hola buenas tardes")
print(resultado)
