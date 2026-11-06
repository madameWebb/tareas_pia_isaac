#Escribir un programa que lea un enteiro positivo, n, introducido polo usuario e despois mostre en pantalla a suma de todos os enteiros desde 1 ata n.


if __name__ == "__main__":
    
    numero = int(input("Escribe un número entero positivo: "))
    suma = 0
    
    for i in range(0, numero + 1):
        
        suma += i
        print(numero, "  ",suma)

    comprobacion = (numero * (numero + 1)) / 2

    print(suma, " ", comprobacion)
