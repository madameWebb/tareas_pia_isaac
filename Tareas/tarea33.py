#Escribir un programa que pida ao usuario dous números enteiros e mostre por pantalla a <n> entre <m> dá un cociente <c> e un resto <r> onde <n> e <m> son os números introducidos polo usuario, e <c> e <r> son o cociente e o resto da división enteira respectivamente.

#Neste exercicio se trata de prácticar o uso de tuplas. Na función que fagas para implementar a división terás como parámetros o dividende o mailo divisor, e vas calcular o dividendo e máis o resto. Como só podes devolver no return un elemento terás que empaquetar a resposta nunha tupla.

#No programa principal podes chamar a esa función, recoller o resultado e acceder á tupla devolta para facer a impresión en pantalla.

#se indica que recibe una tupla cuyos componentes son integer
def calcular(factores: tuple[int, int]):
    dividendo, divisor = factores
    cociente = dividendo // divisor
    resto = dividendo % divisor

    return (cociente, resto)

if __name__ == "__main__":
    factores= (int(input("Escribe un número entero: ")), int(input("Escribe otro número entero: ")))
    cociente_resto = calcular(factores)
    print(factores[0], " dividido entre: ", factores[1], " tiene como cociente: ", int(cociente_resto[0]), " y como resto: ", cociente_resto[1])
    print(f"{factores[0]} dividido entre {factores[1]} tiene como cociente {cociente_resto[0]} y como resto {cociente_resto[1]}")


    