# Escribe unha función que reciba coma parámetros unha lista e mais unha función, e devolva unha nova lista onde cada elemento é o resultado de aplicares a función ao elemento orixinal da lista.

# Xera os test unitarios.

def aplicar(lista:list, funcion):
    
    return funcion(lista)

def funcion(lista:any):
    if type(lista) is list:
        lista_modificada = []
        for elemento in lista:
            if type(elemento) is str:
                lista_modificada.append(elemento.capitalize())
            else:
                lista_modificada.append(elemento**2)

        return lista_modificada
    elif type(lista) is str:
        return lista.capitalize()
    else:
        return lista**2


if __name__ == "__main__":
    lista = [1, 2, 3, 4]
    print(lista)
    print(aplicar(lista, funcion))
    lista_s = "esto es una lista"
    print(lista_s)
    print(aplicar(lista_s, funcion))

    lista_a = 5.25

    print(lista_a)
    print(aplicar(lista_a, funcion)) 

    lista_b= ["a", "b", "c", 4]
    print(lista_b)
    print(aplicar(lista_b, funcion))