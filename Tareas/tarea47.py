#Unha inmobiliaria dunha cidade manexa unha lista de inmobles como a seguinte:

# [{'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe':  True, 'zona': 'A'},
# {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe':  True, 'zona': ' B'},
# {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe':  False, 'zona': 'A'},
# {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe':  True, 'zona': ' B'},
# {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe':  False, 'zona': 'A'}]

# Construír unha función que permita facer a procura de inmobles en función dun orzamento dado. A función recibirá como entrada a lista de inmobles e un prezo, e devolverá outra lista cos inmobles onde o prezo sexa menor ou igual que o dado. Os inmobles da lista que se devolva deben incorporar un novo atributo do a cada dicionario co prezo do inmoble, onde o prezo dun inmoble calcúlase coa seguinte fórmula en función da zona:

# Zona A: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100)
# Zona  B: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100) * 1.5

# Para isto, parte inicialmente dunha función que a partires dun diccionario que representa a un dos inmobles obteña o seu prezo. A partires desa función e as ferramentas que Python podes ir construíndo o resto.

def buscar_inmuebles(inmuebles:list[dict[str, int | str | bool | float]], precio: float) ->list[dict[str, int | str | bool | float]]:
    lista:list[dict[str, int | str | bool | float]] = []
    for elemento in inmuebles:
        precio_calculado = calcular_precio(elemento)
        if precio_calculado <= precio:
            copia = elemento.copy()
            copia["prezo"] = precio_calculado
            lista.append(copia)
    return lista


def calcular_precio (diccionario:dict[str, int | str | bool | float]) -> float:
    # Zona A: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100)
    # Zona  B: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100) * 1.5
    precio = (diccionario["metros"]* 1000 + diccionario["habitacións"] * 5000 + diccionario["garaxe"] * 15000) * (1- calcular_antiguedad(diccionario["ano"])/100)
    if diccionario["zona"].strip() == "A":
        return precio
    else:
        return (precio * 1.5)

def calcular_antiguedad(anno:int)->int:
    import time
    return time.localtime().tm_year - anno


def mostrar(lista:list[dict[str, int | str | bool | float]])-> None:
    for elemento in lista:
        print(elemento)


if __name__ == "__main__":

    lista_inmuebles = [
        {'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe':  True, 'zona': 'A'},
        {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe':  True, 'zona': ' B'},
        {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe':  False, 'zona': 'A'},
        {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe':  True, 'zona': ' B'},
        {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe':  False, 'zona': 'A'}
        ]
    precio = 150000

    lista_buscada = buscar_inmuebles(lista_inmuebles, precio)
    mostrar(lista_buscada)
