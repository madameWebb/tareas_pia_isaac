#Escribir unha función que calcule a área dun círculo e outra que calcule o volume dun cilindro usando a primeira función. É dicir, o volume do cilindro é a área do circulo que forma a base pola altura do cilibro. Polo que dende dentro da función para calcular o volume do cilindro hai que chamar á función que calcula a área do circulo que forma a base.

#    A area do círculo é pi*r**2
#    O volume do cilindro é pi*r**2 * h

#Nota: O valor de PI o tes dentro dó módulo math.

import math


def calcular_area(r):
    
    return math.pi*r**2

def calcular_volumen(d,h):
    r = d / 2
    return calcular_area(r) * h

if __name__ == "__main__":

    print(math.pi)
    
    d = float(input("Introduce el diámetro de la base del cilindro: "))
    h = float(input("Introduce la altura del cilindro: "))

    print(calcular_volumen(d, h), " es el volumen del cilindro.")
        
            
        
