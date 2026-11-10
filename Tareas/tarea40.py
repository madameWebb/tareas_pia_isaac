#Escribir un programa que cre un dicionario simulando unha cesta da compra. O programa debe preguntar o artigo e o seu prezo e engadir o par ao dicionario, ata que o usuario decida terminar. Despois débese amosar por pantalla a lista da compra e o custo total, co seguinte formato
#Lista da compra 	 
#Artigo 1 	Prezo
#Artigo 2 	Prezo
#Artigo 3 	Prezo
#… 	…
#Total 	Custo



def construir_menu():
    return int(input("Escribe el número correspondiente para operar: \n 1 comprar \n 2 recibir total \n 3 salir app \n"))

    
def llenar_carrito(opcion, carrito):
    if opcion == 3:
        print("Hasta pronto")
    
    elif opcion == 2:
        if len(carrito) == 0:
            print("No hay nada en tu carrito")
            llenar_carrito(construir_menu(), carrito)
        else:
            opcion = mostrar(carrito)
            
    else:
        elegir_productos(carrito)

def elegir_productos(carrito):
    clave = input("Que producto deseas comprar? ") 
    valor = float(input (f"Cuanto cuesta {clave} "))
    carrito[clave] = valor
    llenar_carrito(construir_menu(), carrito)

def mostrar(carrito):
    
    print("lista da compra")
    
    for clave,valor in carrito.items():
        print(f"{clave} \t {valor}")

    print(f"Total \t {sum(carrito.values())}")
    
    return llenar_carrito(construir_menu(), carrito)
    
    
    

if __name__ == "__main__":

    carrito = {}
    
    llenar_carrito(construir_menu(), carrito)

   

    

    

    