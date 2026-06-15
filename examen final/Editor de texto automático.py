frase=input("Ingrese una frase: ")
if "triste" in frase.lower():
    nueva_frase=frase.replace("triste","feliz")
    nueva_frase= nueva_frase.replace("triste","feliz")
    print("nueva frase",nueva_frase)
else:
    print(frase.upper())