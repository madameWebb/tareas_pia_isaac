# Tarefa 60. Xestión dunha lista de notas

# Crea un programa para xestionar as cualificacións dun alumno.

# Implementa as seguintes funcións:

#     calcular_media(notas): recibe unha lista de cualificacións e devolve a media. v
#     nota_maxima(notas): devolve a cualificación máis alta. v
#     nota_minima(notas): devolve a cualificación máis baixa. v
#     aprobado(media): recibe unha media e devolve True se é igual ou superior a 5, e False noutro caso. v

# Requisitos:

#     Emprega type hints nos parámetros e valores de retorno. v
#     Indica explicitamente que notas é unha lista de números decimais. v
#     Comproba que a lista non estea baleira antes de calcular os resultados. v
#     Verifica e facer test. V

from decimal import Decimal
from statistics import mean
from functools import wraps
from typing import Callable

def comprobar_list(func: Callable) -> Callable:
    """Decorador que comprueba que la lista no esté vacía."""
    @wraps(func)
    def envoltura(lista: list[Decimal], *args, **kwargs):
        if len(lista) == 0:
            raise ValueError("La lista de notas está vacia")
        return func(lista, *args, **kwargs)
    return envoltura

@comprobar_list
def calcular_media(notas: list[Decimal]) -> Decimal: 
   #recibe unha lista de cualificacións e devolve a media.
   return mean(notas)

@comprobar_list   
def nota_maxima(notas: list[Decimal]) -> Decimal: 
   #devolve a cualificación máis alta.
   return max(notas)

@comprobar_list
def nota_minima(notas: list[Decimal]) -> Decimal: 
   #devolve a cualificación máis baixa.
   return min(notas)

def aprobado(media: Decimal) -> bool: 
   #recibe unha media e devolve True se é igual ou superior a 5, e False noutro caso
   return media >= 5
    

if __name__ == "__main__":
    alumnos: dict[str, dict[str, list[str]]] ={
        "Ana": {
            "Matemáticas": ["5", "5.25", "8", "4"],
            "Lengua": ["6", "8.25", "9", "7.5"],
            "Informática": ["5", "5", "6", "4"]
        },
        "Manuel": {
            "Matemáticas": ["4", "5.25", "4.5", "4"],
            "Lengua": ["6", "6.25", "9", "7"],
            "Informática": ["5.5", "5", "6", "4"]
        },
        "Isidora":{
            "Matemáticas": ["10", "8.5", "9", "9.5"],
            "Lengua": ["6", "8.25", "9", "7.5"],
            "Informática": ["8", "8.5", "6.75", "5"]
        },
        "Filemón":{
            "Matemáticas": ["8.5", "9.25", "8", "10"],
            "Lengua": ["6", "8.25", "9", "7.5"],
            "Informática": ["10", "8.75", "9.5", "9"]
        }
    }

    for alumno, asignaturas in alumnos.items():
        for materia, notas in asignaturas.items():
            asignaturas[materia] = [Decimal(nota) for nota in notas]
                
                

    for alumno, asignaturas in alumnos.items():
        print(f"\n--- {alumno} ---")
        for materia, notas in asignaturas.items():
            media = calcular_media(notas)
            maxima = nota_maxima(notas)
            minima = nota_minima(notas)
            estado = "Aprobado" if aprobado(media) else "Suspenso"
            print(f"{materia}: Media={media:.2f} | Máx={maxima} | Mín={minima} -> {estado}")