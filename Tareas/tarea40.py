#Escribir un programa que cre un dicionario simulando unha cesta da compra. O programa debe preguntar o artigo e o seu prezo e engadir o par ao dicionario, ata que o usuario decida terminar. Despois débese amosar por pantalla a lista da compra e o custo total, co seguinte formato
#Lista da compra 	 
#Artigo 1 	Prezo
#Artigo 2 	Prezo
#Artigo 3 	Prezo
#… 	…
#Total 	Custo



def construir_menu(opcion):

    while opcion is not 2:


if __name__ == "__main__":
    opcion = int(input("Escribe el número correspondiente para operar: \n 1 comprar \n 2 recibir total \n 3 salir app"))
    if opcion == 3:
        pass
    elif opcion == 2:
        pass
    else:
        construir_menu(opcion)

    

    quilos = input("Cuantos quilos quieres? ")

    coste = calcular_precio(float(dict_fruta[fruta]), float(quilos))
    
            
    print(f"{quilos} de {fruta}, a {dict_fruta[fruta]}, cuesta {coste} €")