#Para esta tarefa imos a precisar: 
# - Unha función que aplique un 21% de IVE a unha cantidade 
# - Unha función que aplique un 4% de IVE a unha cantidade 
# - Unha función que aplique un 10% de desconto a unha cantidade.

# Finalmente vas a ter unha lista coa lista da compra. Para elemento da lista será un dicionario onde haberá:

#     prezo do produto sen IVE
#     unha función que aplica o desconto… ou None en caso de non ter desconto
#     unha función que calcule o IVE do produto

# Crearás unha función que colla unha cesta da compra e nos devolve o total a pagar, o IVE da compra e máis a cantidade obtida de aplicar os descontos.

# Xera os tes unitarios correspondentes.


def aplicar(precio:float, valor:any)->any:
    if valor is not None:
        resultado_valor = precio*valor/100
        valor_aplicado = precio + resultado_valor
    else:
        return None, precio
    return resultado_valor, valor_aplicado


def mostrar(cesta:dict[str, list[float, float, any, int]])->None:
    total = []
    print(f"Producto \t\tPrecio \t\tDescuento \t\tIva \t\tNeto + Iva \t\tUnidades \t\tTotal")
    for clave, valor in cesta.items():
        valores =[]
        i = 0
        for elemento in valor:
            
            valores.append(elemento)
            if len(total) == 0:
                if elemento is not None:
                    total.append(valores[i])
                else:
                    total.append(0)
            else:
                if elemento is not None:
                    total[i]=total[i] + valores[i]
                else:
                    total[i]=total[i] + 0
            i += 1
        descuento = None
        if valores[3] is not None:
            descuento = valores[3]
                
            print(f"{clave} \t\t{valores[0]:.2f} \t\t{descuento:.2f} \t\t\t{valores[1]:.2f} \t\t{(valores[0] + valores[1]):.2f} \t\t\t{valores[len(valores)-1]} \t\t\t{(valores[0] + valores[1] + descuento):.2f}")
        else:
            print(f"{clave} \t\t{valores[0]:.2f} \t\t{descuento} \t\t\t{valores[1]:.2f} \t\t{(valores[0] + valores[1]):.2f} \t\t\t{valores[len(valores)-1]} \t\t\t{((valores[0] + valores[1])*valores[len(valores)-1]):.2f}")
    
    print(f"Totales \t\t{total[0]} \t\tTotal Descuentos ={total[3]} \t\tTotal + Iva = {total[0]*(1+total[1]/100)}")
    


if __name__ == "__main__":

    iva_21 = 21
    iva_10 = 10
    iva_4 = 4
    descuento = -10
    A=aplicar

    precios = {"manzanas":[1.35, iva_4, None, 2],
             "lavavajillas":[2.35, iva_10, descuento, 1],
             "patatillas":[3.00, iva_21, descuento, 1]}

    descuentos_manzanas, manzanas_c_descuentos  =A(precios["manzanas"][0], precios["manzanas"][2])
    descuentos_lavavajillas, lavavajillas_c_descuentos  =A(precios["lavavajillas"][0], precios["lavavajillas"][2])
    descuentos_patatillas, patatillas_c_descuentos  =A(precios["patatillas"][0], precios["patatillas"][2])

    iva_manzanas, manzanas_c_iva = A(manzanas_c_descuentos, precios["manzanas"][1])        
    iva_lavavajillas, lavavajillas_c_iva = A(lavavajillas_c_descuentos, precios["lavavajillas"][1])    
    iva_patatillas, patatillas_c_iva= A(patatillas_c_descuentos, precios["patatillas"][1])
    
    
    
    cesta = {"manzanas":[precios["manzanas"][0], 
                         iva_manzanas, 
                         manzanas_c_iva,
                         descuentos_manzanas,
                         precios["manzanas"][3]],
             "lavavajillas":[precios["lavavajillas"][0], 
                             iva_lavavajillas, 
                             lavavajillas_c_iva,
                             descuentos_lavavajillas,
                             precios["lavavajillas"][3]],
             "patatillas":[precios["patatillas"][0],
                           iva_patatillas,
                           patatillas_c_iva,
                           descuentos_patatillas,
                           precios["patatillas"][3]]
                           }
    mostrar(cesta)

