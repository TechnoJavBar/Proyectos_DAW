

def cargar_lista(nombreFichero):
    lista_diccionario= []

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
    esta= False #Se crea un booleano para poder comprobar si está la canción ya introducida
    # if cancion in diccionario:
    #     print(f"La cancion {cancion} ya se encuentra en la lista.")
    # else:
    #     diccionario[cancion]= autor
    #     print(f"La cancion {cancion} se ha añadido correctamente.")
    
    for diccionario in lista:
        if cancion == diccionario["cancion"]:
            print(f"La cancion {cancion} ya se encuentra en la lista.")
            esta= True
    if not esta:
        diccionario= {
            "cancion": cancion,
            "autor": autor,
            "genero": genero
        }
        lista.append(diccionario)
        print(f"La cancion: {cancion} de {autor} se ha añadido correctamente.")
    

def eliminar_cancion(lista, cancion):
    # if cancion in diccionario:
    #     del diccionario[cancion]
    # else:
    #     print(f"La cancion {cancion} no se encuentra en la lista.")

    return lista

def guardar_lista(lista, nombreFichero):
    with open(nombreFichero,"w") as fichero:
        for diccionario in lista:
            fichero.write(f"{diccionario['cancion']} - {diccionario['autor']} - {diccionario['genero']}\n")
        # for cancion, autor in diccionario.items():
        #     fichero.write(cancion+"-"+autor+"\n")
        #     fichero.write(f"{cancion} - {autor}\n")

############################################################################
playlist= cargar_lista("ejercicio Diccionario\\playlist.txt")
print(playlist)

print("##############################################################################")
print(agregar_cancion(playlist,"Nuestra cancion","Alvaro de luna","pop"))
guardar_lista(playlist, "ejercicio Diccionario\\playlist.txt")