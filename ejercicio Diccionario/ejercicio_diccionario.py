

def cargar_lista(nombreFichero):
    lista_diccionario= []
    diccionario={}

    with open(nombreFichero,"r") as fichero:
        for linea in fichero:
            cancion, autor, genero = linea.strip().split("-")
            diccionario= {
                "cancion": cancion, 
                "autor": autor, 
                "genero": genero
                } #se debe de crear un diccionario por cada cancion
            lista_diccionario.append(diccionario)
            
    
    return lista_diccionario

def agregar_cancion(lista, cancion, autor, genero):
    # if cancion in diccionario:
    #     print(f"La cancion {cancion} ya se encuentra en la lista.")
    # else:
    #     diccionario[cancion]= autor
    #     print(f"La cancion {cancion} se ha añadido correctamente.")
    diccionario= {
        "cancion": cancion,
        "autor": autor,
        "genero": genero
    }

    lista.append(diccionario)
    return lista

def eliminar_cancion(diccionario, cancion):
    if cancion in diccionario:
        del diccionario[cancion]
    else:
        print(f"La cancion {cancion} no se encuentra en la lista.")

def guardar_lista(diccionario, nombreFichero):
    with open(nombreFichero,"w") as fichero:
        for cancion, autor in diccionario.items():
            #fichero.write(cancion+"-"+autor+"\n")
            fichero.write(f"{cancion} - {autor}\n")

############################################################################
playlist= cargar_lista("ejercicio Diccionario\\playlist.txt")
print(playlist)

print("##############################################################################")
print(agregar_cancion(playlist,"Nuestra cancion","Alvaro de luna","pop"))