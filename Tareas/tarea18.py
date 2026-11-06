#Escribir un programa que pregunte ao usuario a súa idade e mostre por pantalla todos os anos que cumpriu (desde 1 ata a súa idade).


if __name__ == "__main__":
    
    edad= int(input("Escribe tu edad: "))

    for i in range(0,edad):
        print(i+1)
