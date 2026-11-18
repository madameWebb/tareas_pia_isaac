from datetime import date


def calcular_antiguedad(anno: int) -> int:
    """Calcula los años de antigüedad a partir del año de construcción."""
    anno_actual = date.today().year
    return anno_actual - anno


def calcular_precio(inmueble: dict[str, int | str | bool | float]) -> float:
    """Calcula el precio de un inmueble según sus características y zona."""
    antiguedad = calcular_antiguedad(inmueble["ano"])
    
    # En Python, True vale 1 y False vale 0 automáticamente al multiplicar
    precio_base = (
        inmueble["metros"] * 1000
        + inmueble["habitacións"] * 5000
        + inmueble["garaxe"] * 15000
    ) * (1 - antiguedad / 100)

    # Usamos .strip() porque en tus datos de ejemplo hay un espacio en ' B'
    if inmueble["zona"].strip() == "B":
        return precio_base * 1.5
    return precio_base


def buscar_inmuebles(
    inmuebles: list[dict[str, int | str | bool | float]], 
    presupuesto: float
) -> list[dict[str, int | str | bool | float]]:
    """Filtra inmuebles por presupuesto y añade el atributo 'prezo' a cada resultado."""
    resultado: list[dict[str, int | str | bool | float]] = []
    
    for elemento in inmuebles:
        precio_calculado = calcular_precio(elemento)
        if precio_calculado <= presupuesto:
            copia_inmueble = elemento.copy()
            copia_inmueble["prezo"] = round(precio_calculado, 2)
            resultado.append(copia_inmueble)
            
    return resultado


if __name__ == "__main__":
    lista_inmuebles = [
        {"ano": 2000, "metros": 100, "habitacións": 3, "garaxe": True, "zona": "A"},
        {"ano": 2012, "metros": 60, "habitacións": 2, "garaxe": True, "zona": " B"},
        {"ano": 1980, "metros": 120, "habitacións": 4, "garaxe": False, "zona": "A"},
        {"ano": 2005, "metros": 75, "habitacións": 3, "garaxe": True, "zona": " B"},
        {"ano": 2015, "metros": 90, "habitacións": 2, "garaxe": False, "zona": "A"},
    ]

    encontrados = buscar_inmuebles(lista_inmuebles, 100000)
    for piso in encontrados:
        print(piso)
