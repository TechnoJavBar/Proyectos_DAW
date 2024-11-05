import random #Se importa la biblioteca para poder utilizarla en la funcion de playlist aleatoria

playlist = {}  #Se crea el diccionario que se va a utilizar para almacenar los datos
playlist_aleatoria = {} #Se crea el diccionario para poder crear la playlist aleatoria y no influir en la principal

def cargarlista():  #Se lee el archivo canciones.txt y se introduce en el diccionario playlist
    global playlist #Se utiliza global para indicar que es una variable que existe fuera de la función
    archivo_playlist = open("canciones.txt", "r")
    for linea in archivo_playlist:
        cancion, autor = linea.strip().split("-") #se eliminan los espacios y se identifican los datos con el separador " - "
        playlist[cancion] = autor
    archivo_playlist.close()

def agregar_cancion(): #Se pide al usuario el nombre de la cación y del autor para introducirlo en el diccionario
    global playlist #Se utiliza global para indicar que es una variable que existe fuera de la función
    cancion = input("Introduce la canción: ")
    autor = input("Introduce el autor: ")
    playlist[cancion] = autor
    print(f'La canción "{cancion}" de {autor} ha sido agregada.') 

def eliminar_cancion(): #Se le pide al usuario que introduzca el nombre de la cancion para eliminarla del diccionario
    global playlist #Se utiliza global para indicar que es una variable que existe fuera de la función
    cancion = input("Introduce el nombre de la canción a eliminar: ")
    if cancion in playlist: #Se recorre todo el diccionario buscando la cancion
        playlist.pop(cancion) #Se elimina del diccionario
        print(f'La canción "{cancion}" ha sido eliminada.')
    else:
        print("La canción no se encuentra en la lista.") #Mensaje en el caso de no encontrar la cancion

def contar_canciones(): #Se cuenta las canciones que hay en el diccionario utilizando la longitud
    global playlist #Se utiliza global para indicar que es una variable que existe fuera de la función
    print(f"Total de canciones en la playlist: {len(playlist)}")

def buscar_por_artista(): #Se pide al usuario el nombre del artista para buscar las canciones en el diccionario
    global playlist #Se utiliza global para indicar que es una variable que existe fuera de la función
    artista = input("Introduce el artista: ")
    print(f"Canciones de {artista}:")
    contador= 0
    for cancion, autor in playlist.items():
        if autor == artista:
            print(f"- {cancion}")
            contador +=1
        
    if contador == 0:
        print("No hay canciones de ese artista en la playlist.")

def ordenar_alfabeticamente():
    global playlist #Se utiliza global para indicar que es una variable que existe fuera de la función
    playlist = dict(sorted(playlist.items(), key=lambda x: x[0])) #Se ordena el diccionario 
                                                                  #Key=lambda x: x[0] indica que debe usar el primer elemento de cada tupla
                                                                  #en este caso ya que queremos ordenar por cancion, la cual el la key y es el primer elemento
                                                                  #de la tupla
    print("La playlist ha sido ordenada alfabéticamente por nombre de canción.")

def crear_lista_aleatoria(): #Crea una playlist aleatoria y la introduce el el diccionario playlist_aleatoria
    global playlist #Se utiliza global para indicar que es una variable que existe fuera de la función
    cantidad = int(input("¿De cuántas canciones quieres la playlist? "))
    if cantidad > len(playlist): #Se comprueba si tiene suficientes canciones
        print("No hay suficientes canciones en la lista.")
        return

    # Seleccionar canciones aleatorias y crear un diccionario
    canciones_aleatorias = random.sample(list(playlist.items()), cantidad)
    playlist_aleatoria = dict(canciones_aleatorias)

    print("Esta es tu playlist aleatoria, que la disfrutes:") #Imprime por pantalla la playlist aleatoria
    for cancion, autor in playlist_aleatoria.items():
        print(f"- {cancion} de {autor}")

def guardar_lista(): #Lee el diccionario y sus datos los escribe en el archivo canciones.txt
    global playlist #Se utiliza global para indicar que es una variable que existe fuera de la función
    archivo_playlist = open("canciones.txt", "w")
    for cancion, autor in playlist.items():
        archivo_playlist.write(f"{cancion}-{autor}\n")
        
    print("La lista ha sido guardada exitosamente en 'canciones.txt'.")
    archivo_playlist.close()

while True: #Se crea un menu para que el usuario pueda interactuar con el programa
    print("\nMenu")
    print("1. Cargar lista")
    print("2. Agregar canción") 
    print("3. Eliminar canción")
    print("4. Contar canciones")
    print("5. Buscar canción por artista")
    print("6. Ordenar alfabéticamente")
    print("7. Crear playlist aleatoria")
    print("8. Guardar lista")
    print("9. Salir")

    op = input("Introduce una opción: ")
    if op == "1":
        cargarlista()
    elif op == "2":
        agregar_cancion()
    elif op == "3":
        eliminar_cancion()
    elif op == "4":
        contar_canciones()
    elif op == "5":
        buscar_por_artista()
    elif op == "6":
        ordenar_alfabeticamente()
    elif op == "7":
        crear_lista_aleatoria()
    elif op == "8":
        guardar_lista()
    elif op == "9":
        print("Espere por favor...") 
        print("Saliendo del programa...")
        break  #Finaliza el programa
    else:
        print("Opción no válida, por favor introduce una opción válida.")
