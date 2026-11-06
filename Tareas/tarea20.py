#Escribir un programa que pida ao usuario un número enteiro positivo e mostre por pantalla a conta atrás desde ese número ata cero


if __name__ == "__main__":
    
    numero= int(input("Escribe un número entero positivo: "))
    numero = numero + 1

    for i in range(0,numero):
        numero= numero -1
        print(numero)
