#Escribir un programa que pida ao usuario ou seu peso (en kg) e estatura (en centímetros), calcule ou índice de masa corporal e o almacene nunha variable, e mostre por pantalla a frase: O teu índice de masa corporal é <imc> onde <imc> é o índice de masa corporal calculado redondeado con dous decimais.

#O indice de masa corporal de calcula dividindo o peso en Kg polo cuadrado da altura medida en metros.



if __name__ == "__main__":
    
    def calcular_imc(peso, altura):

        imc = round((peso / (altura**2)), 2)

        return imc

    peso = float(input("Escribe tu peso en kg: "))
    altura = float(input("Escribe tu altura en metros: "))
    
    print(calcular_imc(peso, altura))
        
            
        
