# ==========================================
# SEMANA 1
# Inicio de sesión y creación de cuenta
# ==========================================

usuarios = {}

while True:

    print("\n===== SISTEMA DE PLAYLIST =====")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. entrar al menu principal ")
    print("4. salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":

        usuario = input("Ingrese usuario: ").strip()

        while usuario == "":
            print("El usuario no puede estar vacío.")
            usuario = input("Ingrese usuario: ").strip()

        contraseña = input("Ingrese contraseña: ").strip()

        while contraseña == "":
            print("La contraseña no puede estar vacía.")
            contraseña = input("Ingrese contraseña: ").strip()

        usuarios[usuario] = contraseña

        print("Cuenta creada correctamente.")

    elif opcion == "2":

        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()

        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("Inicio de sesión exitoso.")
        else:
            print("Usuario o contraseña incorrectos.")

    elif opcion == "3":

        print("entrando al menu principal")
        break
    elif opcion == "4":
        print("saliendo del sistema ...")
        exit ()
    else:
        print("opcion invalida")
# ==========================================
# SEMANA 2
# Menú principal de Playlist
# ==========================================

playlist = []

while True:

    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Mostrar playlist")
    print("4. Buscar canción")
    print("5. Contar canciones")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        cancion = input("Nombre de la canción: ")
        playlist.append(cancion)

        print("Canción agregada.")

    elif opcion == "2":

        cancion = input("Canción a eliminar: ")

        if cancion in playlist:
            playlist.remove(cancion)
            print("Canción eliminada.")
        else:
            print("Canción no encontrada.")

    elif opcion == "3":

        if len(playlist) == 0:
            print("La playlist está vacía.")
        else:
            print("\n===== PLAYLIST =====")

            for cancion in playlist:
                print("-", cancion)

    elif opcion == "4":

        cancion = input("Buscar canción: ")

        if cancion in playlist:
            print("Canción encontrada.")
        else:
            print("Canción no encontrada.")

    elif opcion == "5":

        print("Cantidad de canciones:", len(playlist))

    elif opcion == "6":

        print("Saliendo...")
        break

    else:

        print("Opción inválida.")