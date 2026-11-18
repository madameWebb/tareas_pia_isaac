#Fai unha función que nos indique se todos os elementos dunha lista son pares ou non.



def comprobar_lista(lista:list[int])-> bool:
    son_pares:list[int] = []
    for elemento in lista:
        if comprobar_par(elemento):
            son_pares.append(elemento)
    if len(son_pares) == len(lista):
        return True   
    else:
        return False

def comprobar_par(numero):
    if numero % 2 == 0:
        return True       
    else:
        return False

def mostrar(lista: bool )-> None:
    if lista is False:
        print("No todos los números son pares en esta lista")
    else:
        print("Todos los números de esta lista son pares")

if __name__ == "__main__":

    lista1 = comprobar_lista([1,15,13,-28,-7, 2, 3])
    lista2 = comprobar_lista([4,-6,8])

    mostrar(lista1)
    mostrar(lista2)
    