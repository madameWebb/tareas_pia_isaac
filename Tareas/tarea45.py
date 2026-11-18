#Fai unha función que recolla como parámetro unha lista de números e nos indique que elementos son primos.

#Para iso, parte inicialmente dunha función que indique se un número é primo ou non e posteriormente aplica esa función a cada membro da lista (co mecanismo que prefiras).



def comprobar_lista(lista:list[int])->list[int] | bool:
    son_primos:list[int] = []
    for elemento in lista:
        if comprobar_primos(elemento):
            son_primos.append(elemento)
    if len(son_primos) == 0:
        return False                
    return son_primos

def comprobar_primos(numero):
    if numero > 1:
        divisor = numero // 2
        while divisor >= 2:
            if numero % divisor == 0:
                return False
            divisor = divisor -1          
    else:
        return False
    return True

def mostrar(lista:list[int] | bool )-> None:
    if lista is False:
        print("No hay ningún primo")
    else:
        print(f"Estos números son primos: {lista}")

if __name__ == "__main__":

    lista1 = comprobar_lista([1,15,13,-28,-7, 2, 3])
    lista2 = comprobar_lista([4,-6,8])

    mostrar(lista1)
    mostrar(lista2)
    