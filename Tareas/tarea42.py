#Similar a exercicios anteriores, podes copiar o feito nesa parte e continuar ampliando:

#Escribir unha función que calcule a área dun círculo e outra que calcule o volume dun cilindro usando a primeira función. É dicir, o volume do cilindro é a área do circulo que forma a base pola altura do cilibro. Polo que dende dentro da función para calcular o volume do cilindro hai que chamar á función que calcula a área do circulo que forma a base.

#    A area do círculo é pi*r**2
#    O volume do cilindro é pi*r**2 * h

#Nota: O valor de PI o tes dentro dó módulo math.

#import math

#print(math.pi)

#Xera test uniatarios, primeiro para a función que calcula a area do circulo, e logo para o volume do cilindro.

import math


def calcular_area(r):
    print(math.pi)
    return math.pi*r**2

def calcular_volumen(d,h):
    r = d / 2
    area = calcular_area(r)
    return area, area * h

if __name__ == "__main__":

    #print(math.pi)
    
    d = float(input("Introduce el diámetro de la base del cilindro: "))
    h = float(input("Introduce la altura del cilindro: "))
    area, volumen = calcular_volumen(d, h)

    print(f"Area = {area:.2f}, volumen = {volumen:.2f}")