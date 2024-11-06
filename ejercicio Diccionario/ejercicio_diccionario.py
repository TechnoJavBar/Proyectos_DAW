

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
        for diccionario in lista:
            if diccionario['cancion']==cancion and diccionario['autor']==artista:
                lista.remove(diccionario)
                print(f"La cancion {cancion} de {artista} ha sido eliminada.")
    return lista

def buscar_cancion(nombre, lista):
    esta = False
    for diccionario in lista:
        if diccionario['cancion'] == nombre:
            esta= True
    
    return esta
    print(esta)

def guardar_lista(lista, nombreFichero):
    with open(nombreFichero,"w") as fichero:
        for diccionario in lista:
            fichero.write(f"{diccionario['cancion']}-{diccionario['autor']}-{diccionario['genero']}\n")
        # for cancion, autor in diccionario.items():
        #     fichero.write(cancion+"-"+autor+"\n")
        #     fichero.write(f"{cancion} - {autor}\n")

############################################################################
playlist= cargar_lista("ejercicio Diccionario\\playlist.txt")

print(agregar_cancion(playlist,"Brisa","Paul thin","pop"))
eliminar_cancion(playlist,"Nuestra cancion","Alvaro de luna")
guardar_lista(playlist, "ejercicio Diccionario\\playlist.txt")