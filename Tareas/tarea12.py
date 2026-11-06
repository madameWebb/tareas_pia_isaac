#Escribir un programa que almacene a cadea de caracteres contrasinal nunha variable, terá un valor predifinido.

#Logo debe preguntar ao usuario polo contrasinal e imprima por pantalla se o contrasinal introducido polo usuario coincide ou non coa variable. Non importan as maiúsculas e minúsculas.

if __name__ == "__main__":
    
    contrasinal = "iI5432!"

    introducir= input("introduce tu contraseña: ")

    if introducir == contrasinal:
        print("Contraseña correcta")
    else:
        print("Contraseña errónea")
