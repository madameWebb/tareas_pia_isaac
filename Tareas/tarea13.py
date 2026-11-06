#Escribir un programa que pida ao usuario dous números, dividendo e divisor.

#Logo debe amosar por pantalla a súa división, aínda que se o divisor é cero debes amosar unha mensaxe de erro (do estilo non se pode dividir por 0).


if __name__ == "__main__":
    
    dividendo = float(input("Escribe un número: "))
    divisor = float(input("Escribe un número distinto de 0: "))

    while divisor == 0:

        divisor = float(input("No se puede dividir por 0, introduce otro número: "))

    print(dividendo/divisor)