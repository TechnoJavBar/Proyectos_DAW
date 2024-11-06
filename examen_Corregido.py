import random

def cargar_lista(nombreFichero):
    diccionario= {}
    with open(nombreFichero,"r") as fichero:
        for linea in fichero:
            cancion, autor = linea.strip().split("-")
            diccionario[cancion]= autor

    return diccionario

def guardar_lista(diccionario, nombreFichero):
    with open(nombreFichero,"w") as fichero:
        for cancion, autor in diccionario.items():
            #fichero.write(cancion+"-"+autor+"\n")
            fichero.write(f"{cancion} - {autor}\n")

def eliminar_cancion(diccionario, cancion):
    if cancion in diccionario:
        del diccionario[cancion]
    else:
        print(f"La cancion {cancion} no se encuentra en la lista.")


def crear_lista_aleatoria(diccionario, n):
    n = min(n, len(diccionario))
    return random.sample(diccionario.items(), n)

def contar_canciones(diccionario):
    return len(diccionario)

def agregar_cancion(diccionario, cancion, autor):
    if cancion in diccionario:
        print(f"La cancion {cancion} ya se encuentra en la lista.")
    else:
        diccionario[cancion]= autor
        print(f"La cancion {cancion} se ha añadido correctamente.")

def buscar_por_artista(diccionario, artistaBuscado):
    lista_artista= []

    for cancion in diccionario:
        if diccionario[cancion] == artistaBuscado:
            lista_artista.append(cancion)
        
    return lista_artista
listaCanciones= cargar_lista("playlist.txt")
eliminar_cancion(listaCanciones,"Wonderwall")
print(buscar_por_artista(listaCanciones,"Queen"))
guardar_lista(listaCanciones,"playlist.txt")
print(listaCanciones)