#Escribir un programa que garde nun dicionario os prezos das froitas da táboa, pregunte ao usuario por unha froita, un número de quilos e mostre por pantalla o prezo dese número de quilos de froita.

#Se a froita non está no dicionario debe mostrar unha mensaxe informando diso.
#Froita 	Prezo
#Plátano 	1.35
#Mazá 	0.80
#Pera 	0.85
#Laranxa 	0.70


def calcular_precio(precio_fruta : float, quilos : float) -> float:

    return precio_fruta * quilos
    


if __name__ == "__main__":
    
    dict_fruta = {"Plátano": 1.35, "Mazá" : 0.8, "Pera" : 0.85, "Laranxa" : 0.7}
    fruta = input("Qué fruta quieres? ")
    while fruta not in dict_fruta:
        fruta = input("No tenemos esa fruta, elige otra: ")

    quilos = input("Cuantos quilos quieres? ")

    coste = calcular_precio(float(dict_fruta[fruta]), float(quilos))
    
            
    print(f"{quilos} de {fruta}, a {dict_fruta[fruta]}, cuesta {coste} €")