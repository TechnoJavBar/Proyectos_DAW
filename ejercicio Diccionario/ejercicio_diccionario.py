

def cargar_lista(nombreFichero):
    lista_diccionario= []
    contador= len(lista_diciconario)

    with open(nombreFichero,"r") as fichero:
        for linea in fichero:
            contador += 1 #se utiliza para contar el numero de canciones y asi llamar los diccionarios diferentes
            cancion, autor, genero = linea.strip().split("-")
            diccionario= {"cancion": cancion, "autor": autor, "genero": genero} #se debe de crear un diccionario por cada cancion
            lista_diccionario.append(diccionario)
            
    
    return diccionario

def guardar_lista(diccionario, nombreFichero):
    with open(nombreFichero,"w") as fichero:
        for cancion, autor in diccionario.items():
            #fichero.write(cancion+"-"+autor+"\n")
            fichero.write(f"{cancion} - {autor}\n")

def agregar_cancion(diccionario, cancion, autor):
    if cancion in diccionario:
        print(f"La cancion {cancion} ya se encuentra en la lista.")
    else:
        diccionario[cancion]= autor
        print(f"La cancion {cancion} se ha añadido correctamente.")

def eliminar_cancion(diccionario, cancion):
    if cancion in diccionario:
        del diccionario[cancion]
    else:
        print(f"La cancion {cancion} no se encuentra en la lista.")