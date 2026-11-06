#Para tributar un determinado imposto débese ser maior de 16 anos e ter uns ingresos iguais ou superiores a 1000 € mensuais.

#Escribir un programa que pregunte ao usuario a súa idade e os seus ingresos mensuais e mostre por pantalla se o usuario ten que tributar ou non.

if __name__ == "__main__":
    
    edad= int(input("Escribe tu edad: "))
    ingresos= float(input("escribe tus ingresos mensuales: "))

    if edad >= 16 and ingresos >= 1000:
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")
