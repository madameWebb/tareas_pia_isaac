# Crea un decorador chamado medir_tempo que permita calcular canto tempo tarda en executarse unha función.

# O decorador debe cumprir os seguintes requisitos:

#     Debe utilizar a función time.time() do módulo time para obter o instante inicial e final da execución.
#     Debe calcular o tempo transcorrido.
#     Debe mostrar por pantalla o nome da función executada e o tempo que tardou en executarse.
#     Debe devolver o resultado orixinal da función.

# A continuación, utiliza o decorador para modificar unha función chamada contar, que reciba un número enteiro n e calcule a suma de todos os números desde 1 ata n.

# Lembra facer os test.

import time
from functools import wraps
from typing import Callable


def medir_tempo(func: Callable) -> Callable:
    """Decorador que mide e imprime el tiempo de ejecución de una función."""
    @wraps(func)
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        
        transcurrido = fin - inicio
        print(f"Función '{func.__name__}' ejecutada en {transcurrido:.6f} segundos.")
        return resultado
    return envoltura


@medir_tempo
def contar(n: int) -> int:
    """Calcula la suma de todos los números desde 1 hasta n."""
    if n < 1:
        return 0
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


if __name__ == "__main__":
    total = contar(1_000_000)
    print(f"Resultado de la suma: {total}")
