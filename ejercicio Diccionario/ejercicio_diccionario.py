

def cargar_lista(nombreFichero):
    lista_diccionario= []

    with open(nombreFichero,"r") as fichero:
        for linea in fichero:
            cancion, autor, genero = linea.strip().split("-")
            
            #se debe de crear un diccionario por cada cancion
            diccionario= {
                "cancion": cancion, 
                "autor": autor, 
                "genero": genero
                } 
            lista_diccionario.append(diccionario)
            
    
    return lista_diccionario

def agregar_cancion(lista, cancion, autor, genero):
    
    esta = buscar_cancion(cancion,lista)
    if esta:
        print(f"La cancion {cancion} ya se encuentra registrada")
    else:
        diccionario= {
            "cancion": cancion,
            "autor": autor,
            "genero": genero
        }
        lista.append(diccionario)
        print(f"La cancion: {cancion} de {autor} se ha añadido correctamente.")
    

def eliminar_cancion(lista, cancion, artista):

    found= buscar_cancion(cancion,lista)

    if not found:
        print(f"La cancion {cancion} del artista {artista} no se encuentra en la lista.")
    else:
        del lista[found]
        print(f"La cancion {cancion} de {artista} se ha eliminado correctamente")
    return lista

def buscar_cancion(nombre, lista):
    
    for i,diccionario in enumerate(lista):
        if diccionario['cancion'] == nombre:
            return i
    return -1
    

def guardar_lista(lista, nombreFichero):
    with open(nombreFichero,"w") as fichero:
        for diccionario in lista:
            fichero.write(f"{diccionario['cancion']}-{diccionario['autor']}-{diccionario['genero']}\n")

############################################################################


playlist= cargar_lista("ejercicio Diccionario\\playlist.txt")
cancion= input("Introduce el nombre de la canción a añadir: ")
autor= input("Introduce el nombre del artista: ")
genero= input("Introduce el género: ")

print(agregar_cancion(playlist,cancion, autor, genero))

cancion= input("Introduce el nombre de la canción a borrar: ")
autor= input("Introduce el nombre del artista: ")

eliminar_cancion(playlist,cancion,autor)
guardar_lista(playlist, "ejercicio Diccionario\\playlist.txt")