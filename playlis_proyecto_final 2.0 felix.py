# PROYECTO FINAL PLAYLIST
#lista de canciones 
playlist=[]
#Bloqueo de seguridad
contraseña= "1234"
usuario_registrado= "admin"
while True:
    print("""======= SISTEMA DE GESTION DE PLAYLIST ======
          1.INICIAR SESION
          2. REGISTRARSE
          3. SALIR
          """)
    OPCION =(input("seleccione una opcion: "))
    if OPCION == "1":
        print("\n---INICIO DE SESION---")
        USUARIO=input("ingrese su usuario: ")
        clave=input("ingrese la contraseña del sistema: ")
        if USUARIO==usuario_registrado and clave == contraseña:
            print("\n Acceso Permitido")
            print("\n ---SISTEMA LISTO PARA USAR---")
            break
        else:
            print("usuario o contraseña incorrectos")
    if OPCION == "2":
        print("\n ---REGISTRO DE USUARIO---")
        user = input("cree su nombre de usuario: ")
        password = (input("cree su contraseña: ")) 
        user == input('Ingrese su usuario: ') and password == int(input("Ingrese password: "))
        print('registro completado con exito¡ Ya puedes iniciar sesion')
    elif OPCION == "3":
        print("Saliendo del sistema ...")
        break
    else:
        print("Opcion incorrecta, intente nuevamente")
