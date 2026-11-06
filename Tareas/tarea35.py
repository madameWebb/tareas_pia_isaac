# Escribir un programa que almacene unha lista os números do 1 ao 10 e os ensine por patalla en orde inversa separados por comas. Usa o metodo join da clase string para separalos por comas

if __name__ == "__main__":
    numeros = []
    cadena = []
    n = 0
    while n <= 9:
        n += 1
        numeros.append(n)
        cadena.append(str(n))

    cadena.reverse()
    
    imprimir = ",".join(cadena)

    print(imprimir)
