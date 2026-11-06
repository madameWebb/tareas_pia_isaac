#Escribir un programa que pida ao usuario un número enteiro positivo e mostre por pantalla todos os números impares desde 1 ata ese número.


if __name__ == "__main__":
    
    numero= int(input("Escribe un número entero: "))

    for i in range(0,numero):
        n = i+1
        if n%2 != 0:

            print(n)
