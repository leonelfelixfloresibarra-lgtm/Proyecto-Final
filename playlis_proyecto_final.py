# PROYECTO FINAL PLAYLIST
#lista de canciones 
playlist=[]
#Bloqueo de seguridad
contraseña= "1234"
while True:
    clave=input("Ingrese la contraseña del sistema: ").strip()
    if clave== contraseña:
        print("\nAcceso permitido")
        break
    else:
        print("contraseña incorrecta")