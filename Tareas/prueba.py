from decimal import Decimal
import csv
from pathlib import Path

lista_aux: list[list[str | Decimal]] = []
ruta_csv = Path(__file__).parent / "starwars.csv"
with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
    lector = csv.reader(archivo, delimiter=",", quotechar='"')
    claves: list[str] = next(lector)  # Salta o guarda la primera fila
    
    for fila in lector:
        lista_aux.append(["0" if x == "NA" or x == "none" else x for x in fila])
    for elemento in lista_aux:
        diccionario: dict[str, str | Decimal] = dict(zip(claves, elemento))
        for clave, valor in diccionario.items():
            if clave == "height" or clave == "mass" or clave == "birth_year":
                diccionario[clave] = Decimal(diccionario[clave])
        
for elemento in lista_aux:
    print(elemento)