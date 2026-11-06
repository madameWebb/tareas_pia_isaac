#Escribir un programa que pida ao usuario que introduza unha frase na consola e mostre por pantalla a frase invertida.


if __name__ == "__main__":
    
    texto = input("Introduce una frase: ")

    print("".join(reversed(texto)))
    
    
    textos = "Python"
    print(textos[::-1])
    
