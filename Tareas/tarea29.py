#Unha xoguetería ten moito éxito en dous dos seus produtos: pallasos e bonecas.

#Adoita facer venda por correo e a empresa de loxística cóbralles por peso de cada paquete, así que deben calcular o peso dos pallasos e bonecas que sairán en cada paquete a demanda. Cada pallaso pesa 112 g e cada boneca 75 g.

#Escribir un programa que lea o número de pallasos e bonecas vendidos no último pedido e calcule o peso total en Kg do paquete que será enviado.

def calcular_peso(payasos, munnecas):
    peso_payaso = 112 #en gramos
    peso_munneca = 75 #en gramos
    peso_total = ((peso_payaso * payasos) + (peso_munneca * munnecas)) / 1000 #en kg
    return peso_total

if __name__ == "__main__":
    
    payasos = float(input("Escribe el número de payasos a enviar: "))
    munnecas = float(input("Escribe el número de munnecas a enviar: "))

    print(calcular_peso(payasos, munnecas), " kg")
        
            
        
