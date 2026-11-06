#Escribir un programa que pregunte o nome do usuario na consola e despois de que o usuario introdúzao amose por pantalla: 
# ten < n> letras
# onde o nome de usuario saia en maiúsculas e 
# é o número de letras que ten o nome.


if __name__ == "__main__":
    nombre = input("Introduce tu nombre y apellidos: ")
    n = len(nombre.replace(" ", ""))

    print(nombre.lower())
    print("El nombre tiene; ", n, " letras")
