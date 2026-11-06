#Escribir un programa que pida ao usuario un número enteiro e mostre por pantalla un triángulo rectángulo como o de máis abaixo, de altura o número introducido.

#*
#**
#***
#****
#*****

#Cando un string se multiplica por un número, o resultado é o string duplicado o número de veces indicado.

if __name__ == "__main__":
    
    numero = int(input("Escribe un número entero positivo: "))
    
    
    for i in range(0, numero + 1):
        
        cadena = "*"
        cadenas = cadena * i
        print(cadenas)
        
            
        
