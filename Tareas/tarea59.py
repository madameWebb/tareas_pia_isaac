# Tarefa 59. Operacións matemáticas

# Desenvolve un módulo que permita realizar operacións matemáticas básicas.

# Crea as seguintes funcións:

#     sumar(a, b): devolve a suma de dous números enteiros.
#     restar(a, b): devolve a diferenza entre dous números enteiros.
#     multiplicar(a, b): devolve o produto de dous números enteiros.
#     dividir(a, b): devolve a división de dous números enteiros.

# Requisitos:

#     Utiliza type hints para indicar os tipos dos parámetros.
#     Indica o tipo de dato que devolve cada función.
#     Ten en conta que a función dividir():
#         Debe comprobar que o divisor non sexa cero (lanzar excepción)
#         Se o resultado da división non é un enteiro, debe devolver None
#     Verifica e fai algúns test.

from functools import wraps
from typing import Callable

def comprobar_int(func: Callable) -> Callable:
    """Decorador que comprueba si el númento es de tipo entero."""
    @wraps(func)
    def envoltura(a: int, b: int, *args, **kwargs):
        if type(a) is not int or type(b) is not int:
            raise TypeError("Los parámetros deben ser de tipo entero (int)")
        return func(a, b, *args, **kwargs)
    return envoltura

@comprobar_int
def sumar(a: int, b: int) -> int:
    return a + b

@comprobar_int
def restar(a: int, b: int) -> int:
    return a - b

@comprobar_int
def multiplicar(a: int, b: int) -> int:
    return a * b

@comprobar_int
def dividir(a: int, b: int) -> int | None:
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    if a % b != 0:
        return None
    return a // b
    

# if __name__ == "__main__":
#     try:
#         print(sumar(1, 1))
#         print(restar(1, 2))
#         print(multiplicar(2, "a"))
#         print(dividir(4, 0))
#     except Exception as e:
#         print(f"Error: {e}")

