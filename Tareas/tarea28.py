#Escribir unha función que calcule o total dunha factura tras aplicarlle o IVE. A función debe recibir a cantidade sen IVE e a porcentaxe de IVE a aplicar, e devolver o total da factura.

#Se se invoca a función sen pasarlle a porcentaxe de IVE, deberá aplicar un 21%.


if __name__ == "__main__":
    
    def calcular_con_iva(total_sin_iva, iva):
        
        total_con_iva = total_sin_iva * (1 + (iva / 100))

        return total_con_iva

    total_sin_iva = float(input("Escribe factura sin IVA: "))
    iva = float(input("Escribe IVA a aplicar: "))
    
    print("total con IVA: ", calcular_con_iva(total_sin_iva, iva))
        
            
        
