#Escribir un programa que pregunte ao usuario os números gañadores da lotería primitiva, os almacene nunha lista e logo os amose por pantalla ordenados de menor a maior.

# -> list[int] va a devolver una lista de int
def ordenar(ganadores: list[int]) -> list[int]:
    lista = sorted(ganadores, reverse = True)

    return lista

if __name__ == "__main__":

    ganadores: list[int] = []
    i = 0

    while i <= 5:
        i = i+1
        ganadores.append(int(input(f"Escribe el {i}º número de la combinación ganadora de la primitiva: ")))

    
    print(ordenar(ganadores)) 
        



    