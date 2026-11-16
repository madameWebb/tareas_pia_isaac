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


def aplicar(valor:any, precio:float)->any:
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
        for elemento in cesta[clave]:
            i = 0
            print(f"{clave}    {elemento[0]}    {elemento[1]}    {elemento[0] + elemento[1]}    {elemento[2]}    {elemento[0] + elemento[2]}    {elemento[0] + elemento[1] + elemento[2]}")
            if len(total) <= 4:
                
                if total[i] is not None:
                    total.append(elemento[i])
                    
                else:
                    total[i].append[0]
            else:
                if total[i] is not None:
                    total.append(elemento[i])
                    
                else:
                    total[i].append[0]
    
    print(f"Totales    {total[0]}    Total + Iva = {total[0]*total[1]/100}    Total Descuentos{total[2]}    {total[3]}")


if __name__ == "__main__":

    iva_21 = 21
    iva_10 = 10
    iva_4 = 4
    descuento = -10
    A=aplicar

    precios = {"manzanas":[1.35, iva_4, None],
             "lavavajillas":[2.35, iva_10, descuento],
             "patatillas":[3.00, iva_21, descuento]}
    cesta:dict[str, list[float, float, float]]
    cesta = {"manzanas":[precios["manzanas"][0]*2, 
                         A(precios["manzanas"][0]*2, precios["manzanas"][1]), 
                         A(precios["manzanas"][0]*2, precios["manzanas"][2])],
             "lavavajillas":[precios["lavavajillas"][0], 
                             A(precios["lavavajillas"][0], precios["lavavajillas"][1]),
                             A(precios["lavavajillas"][0], precios["lavavajillas"][2])],
             "patatillas":[precios["patatillas"][0],
                           A(precios["patatillas"][0], precios["patatillas"][1]),
                           A(precios["patatillas"][0], precios["patatillas"][2])]}


