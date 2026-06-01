# PROYECTO FINAL PLAYLIST
#lista de canciones 
playlist=[]
#Bloqueo de seguridad
contraseña= "1234"
usuario_registrado= "admin"
#datos de la nueva cuenta creada
nuevo_usuario= ""
nueva_contraseña=""
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
        if(USUARIO == usuario_registrado and clave == contraseña) or (USUARIO == nuevo_usuario and clave == nueva_contraseña):
            print("\n Acceso Permitido")
            print("\n ---SISTEMA LISTO PARA USAR---")
            break
        else:
            print("usuario o contraseña incorrectos")
    if OPCION == "2":
        nuevo_usuario = input ("cree su nombre de usuario: ")
        nueva_contraseña= input ("cree su contraseña: ")
        if nuevo_usuario != "" and nueva_contraseña != "":
            print(" Registro completado con exito! Ya puedes iniciar sesion")
        else:
            print("Error: no se permite datos vacios, intenta de nuevo")
    elif OPCION == "3":
        print("Saliendo del sistema ...")
        break
    else:
        print("Opcion incorrecta, intente nuevamente")