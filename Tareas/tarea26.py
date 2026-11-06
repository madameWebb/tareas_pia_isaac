#Escribir unha función que reciba un número enteiro positivo e devolva o seu factorial.

# O factorial dun número se consegue multiplicando todos os números entre o número orixinal ata 1. Por exemplo:


# O factorial de 5 é:

# f5 = 5 * 4 * 3 * 2 * 1



if __name__ == "__main__":
    
    def factorizar(n):
        contador = n
        factorizado = n
        # contador = factorizado = n

        while contador != 1:
            
            contador = contador - 1
            factorizado = factorizado * contador

        return factorizado

    n = int(input("Escribe un número entero positivo: "))
    print(factorizar(n))
        
            
        
