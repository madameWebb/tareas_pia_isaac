#Escribir un programa que pregunte ao usuario a súa idade e mostre por pantalla se é maior de idade ou non.


if __name__ == "__main__":
    
    edad = input("Introduce tu edad: ")

    if int(edad) >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")
