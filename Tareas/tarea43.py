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


def aplicar(precio: float, valor: None | float | int) -> tuple[float | None, float]:
    if valor is not None:
        resultado_valor = precio * valor / 100
        valor_aplicado = precio + resultado_valor
        return resultado_valor, valor_aplicado
    return None, precio


def mostrar(cesta: dict[str, list[float | int | None]]) -> None:
    total_base = 0.0
    total_descuentos = 0.0
    total_iva = 0.0
    total_final = 0.0

    print("Producto \t\tPrecio \t\tDescuento \tIva \t\tNeto + Iva \tUnidades \tTotal")
    
    for clave, valores in cesta.items():
        precio_base = valores[0]
        iva_eur = valores[1]
        precio_final_unidad = valores[2]  # Ya incluye el descuento y el IVA
        descuento_eur = valores[3] if valores[3] is not None else 0.0
        unidades = valores[4]

        subtotal_linea = precio_final_unidad * unidades

        # Acumulamos totales reales multiplicando por unidades
        total_base += precio_base * unidades
        total_descuentos += descuento_eur * unidades
        total_iva += iva_eur * unidades
        total_final += subtotal_linea

        texto_descuento = f"{valores[3]:.2f}" if valores[3] is not None else "None"

        print(f"{clave:<15} \t{precio_base:.2f} \t\t{texto_descuento} \t\t{iva_eur:.2f} \t\t{precio_final_unidad:.2f} \t\t{unidades} \t\t{subtotal_linea:.2f}")

    print("-" * 105)
    print(f"Totales \t\t{total_base:.2f} \t\t{total_descuentos:.2f} \t\t{total_iva:.2f} \t\t\t\t\t\t{total_final:.2f}")


if __name__ == "__main__":
    iva_21 = 21
    iva_10 = 10
    iva_4 = 4
    descuento = -10

    precios = {
        "manzanas": [1.35, iva_4, None, 2],
        "lavavajillas": [2.35, iva_10, descuento, 1],
        "patatillas": [3.00, iva_21, descuento, 1]
    }

    cesta = {}
    # Automatizamos la creación de la cesta para no repetir código por cada producto
    for producto, datos in precios.items():
        precio_u, iva_pct, desc_pct, unidades = datos
        desc_eur, precio_con_desc = aplicar(precio_u, desc_pct)
        iva_eur, precio_con_iva = aplicar(precio_con_desc, iva_pct)
        
        cesta[producto] = [precio_u, iva_eur, precio_con_iva, desc_eur, unidades]

    mostrar(cesta)
