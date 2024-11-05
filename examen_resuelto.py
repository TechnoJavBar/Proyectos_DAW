import random

playlist = {}
playlist_aleatoria = {}

def cargarlista():
    archivo_playlist = open("canciones.txt", "r")
    for linea in archivo_playlist:
        cancion, autor = linea.strip().split("-")
        playlist[cancion] = autor
    archivo_playlist.close()

def agregar_cancion():
    cancion = input("Introduce la canción: ")
    autor = input("Introduce el autor: ")
    playlist[cancion] = autor
    print(f'La canción "{cancion}" de {autor} ha sido agregada.')

def eliminar_cancion():
    cancion = input("Introduce el nombre de la canción a eliminar: ")
    if cancion in playlist:
        playlist.pop(cancion)
        print(f'La canción "{cancion}" ha sido eliminada.')
    else:
        print("La canción no se encuentra en la lista.")

def contar_canciones():
    print(f"Total de canciones en la playlist: {len(playlist)}")

def buscar_por_artista():
    artista = input("Introduce el artista: ")
    print(f"Canciones de {artista}:")
    for cancion, autor in playlist.items():
        if autor == artista:
            print(f"- {cancion}")

def ordenar_alfabeticamente():
    global playlist
    playlist = dict(sorted(playlist.items(), key=lambda x: x[0]))
    print("La playlist ha sido ordenada alfabéticamente por nombre de canción.")

def crear_lista_aleatoria():
    cantidad = int(input("¿De cuántas canciones quieres la playlist? "))
    if cantidad > len(playlist):
        print("No hay suficientes canciones en la lista.")
        return

    # Seleccionar canciones aleatorias y crear un diccionario
    canciones_aleatorias = random.sample(list(playlist.items()), cantidad)
    playlist_aleatoria = dict(canciones_aleatorias)

    print("Esta es tu playlist aleatoria, que la disfrutes:")
    for cancion, autor in playlist_aleatoria.items():
        print(f"- {cancion} de {autor}")

def guardar_lista():
    archivo_playlist = open("canciones.txt", "w")
    for cancion, autor in playlist.items():
        archivo_playlist.write(f"{cancion}-{autor}\n")
        
    print("La lista ha sido guardada exitosamente en 'canciones.txt'.")
    archivo_playlist.close()

while True:
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
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor introduce una opción válida.")
