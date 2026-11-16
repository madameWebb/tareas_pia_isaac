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
        return None, None
    return resultado_valor, valor_aplicado

def mostrar(cesta:dict[str, list[float, float, float]])->None:
    total = []
    print(f"Producto    Precio    Iva    Precio + Iva    Descuento    Precio + Descuento    Total")
    for clave, valor in cesta.items():
        valores =[]
        i = 0
        for elemento in valor:
            
            valores.append(elemento)
            
            total.append(valores[i])
            i = +1

        
        print(f"{clave}    {valores[0]:.2f}       {valores[1]:.2f}        {(valores[0] + valores[1]):.2f}        {valores[2]:.2f}       {(valores[0] + valores[2]):.2f}                  {(valores[0] + valores[1] + valores[2]):.2f}")
        
        
            
        
    
    print(f"Totales    {total[0]}    Total + Iva = {total[0]*(1+total[1]/100)}    Total Descuentos{total[2]}")
    total = []


if __name__ == "__main__":

    iva_21 = 21
    iva_10 = 10
    iva_4 = 4
    descuento = -10
    A=aplicar

    precios = {"manzanas":[1.35, iva_4, None],
             "lavavajillas":[2.35, iva_10, descuento],
             "patatillas":[3.00, iva_21, descuento]}
    
    iva_manzanas, manzanas_c_iva = A(precios["manzanas"][0]*2, precios["manzanas"][1])
    descuentos_manzanas, manzanas_c_descuentos  =A(precios["manzanas"][0]*2, precios["manzanas"][2])
    iva_lavavajillas, lavavajillas_c_iva = A(precios["lavavajillas"][0]*2, precios["lavavajillas"][1])
    descuentos_lavavajillas, lavavajillas_c_descuentos  =A(precios["lavavajillas"][0]*2, precios["lavavajillas"][2])
    iva_patatillas, patatillas_c_iva= A(precios["patatillas"][0]*2, precios["patatillas"][1])
    descuentos_patatillas, patatillas_c_descuentos  =A(precios["patatillas"][0]*2, precios["patatillas"][2])
    
    
    cesta = {"manzanas":[precios["manzanas"][0]*2, 
                         iva_manzanas, 
                         manzanas_c_iva,
                         descuentos_manzanas]
            #  "lavavajillas":[precios["lavavajillas"][0], 
            #                  iva_lavavajillas, lavavajillas_c_iva,
            #                  descuentos_lavavajillas],
            #  "patatillas":[precios["patatillas"][0],
            #                iva_patatillas,
            #                patatillas_c_iva,
            #                descuentos_patatillas]
                           }
    mostrar(cesta)

