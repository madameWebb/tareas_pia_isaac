# Lembras a tarefa 51?

# Escribe un programa onde declares unha clase vehiculo con velocidade máxima e kilometraxe coma atributos. Controla que a velocidade máxima non pode ser negativa, e que o kilometraxe nunca pode descender. Implementa a transformación do obxecto vehiculo a string. Fai os test correspondentes

# Fai decoradores para impedir que un parámetro sexa negativo e que un parámetro non disminua.

from functools import wraps
from typing import Callable


def no_negativo(func: Callable) -> Callable:
    """Decorador que impide asignar un valor numérico negativo a un setter."""
    @wraps(func)
    def envoltura(self, valor: float):
        if valor < 0:
            raise ValueError("El valor introducido no puede ser negativo")
        return func(self, valor)
    return envoltura


def no_disminuye(nombre_atributo: str) -> Callable:
    """Decorador que impide que el nuevo valor sea menor que el valor actual del atributo."""
    def decorador(func: Callable) -> Callable:
        @wraps(func)
        def envoltura(self, valor: float):
            valor_actual = getattr(self, nombre_atributo)
            if valor < valor_actual:
                raise ValueError(f"El valor de '{nombre_atributo}' no puede descender")
            return func(self, valor)
        return envoltura
    return decorador


class Vehiculo:
    def __init__(self, nombre: str, velocidad_max: float, kilometraje: float = 0):
        self._nombre = nombre
        self._velocidad_max = 0.0
        self._kilometraje = 0.0
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def velocidad_max(self) -> float:
        return self._velocidad_max

    @property
    def kilometraje(self) -> float:
        return self._kilometraje

    @velocidad_max.setter
    @no_negativo
    def velocidad_max(self, valor: float) -> None:
        self._velocidad_max = valor

    @kilometraje.setter
    @no_negativo
    @no_disminuye("kilometraje")
    def kilometraje(self, valor: float) -> None:
        self._kilometraje = valor

    def __str__(self) -> str:
        return f"Vehículo: {self._nombre} | Velocidad máx: {self._velocidad_max} km/h | Kilometraje: {self._kilometraje} km"


if __name__ == "__main__":
    vehiculo1 = Vehiculo("600", 100, 0)
    vehiculo2 = Vehiculo("850", 120, 100)

    print(vehiculo1)
    print(vehiculo2)

    # Test 1: Subir kilometraje (válido)
    vehiculo2.kilometraje = 150
    print("\nTras actualizar km:", vehiculo2)

    # Test 2: Intentar bajar kilometraje (salta @no_disminuye)
    try:
        vehiculo2.kilometraje = 120
    except ValueError as e:
        print("Excepción capturada (km):", e)
    print("Kilometraje actual:", vehiculo2.kilometraje)

    # Test 3: Intentar poner velocidad negativa (salta @no_negativo)
    try:
        vehiculo1.velocidad_max = -20
    except ValueError as e:
        print("Excepción capturada (velocidad):", e)
    print("Velocidad actual:", vehiculo1.velocidad_max)

    # Test 4: Intentar poner kilometraje negativo (salta @no_negativo antes que @no_disminuye)
    try:
        vehiculo1.kilometraje = -5
    except ValueError as e:
        print("Excepción capturada (km negativo):", e)
