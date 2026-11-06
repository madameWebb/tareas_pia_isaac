#Escribir un programa que pida ao usuario un número enteiro e mostre por pantalla se é par ou impar.

#Para iso, basta dividir por 2 e ver se o resto da división é cero. O resto da división se calcula co operador %

if __name__ == "__main__":
    
    num = int(input("Escribe un número entero: "))

    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

    