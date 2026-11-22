# Implementa a clase Bicicleta, que ten tres atributos:

#     velocidadActual, platoActual e piñonActual, de tipo enteiro v

# Ademais posue 2 métodos:

#     acelerar(), que duplica a velocidade actual cada vez que se chama. Se e velociade actual é cero entón pasa a ser 1. v
#     frear(), reduce á metade a velocidade actual, tendo en conta que a velocidade é un enteiro, v

# A clase debe ter ademais un construtor que inicialice todos os atributos, pero se non se lle pasa nada inicializa velocidade actual a 0 e o plato e o piñon a 1. v

# Fai que o a velocidadeActual non pode ser negativo, nin o piñonActual e platoActual tampouco poden valer negativo. v
# Os platos e os piñons so poden cambiar de 1 en 1, e dicir, se o piñon é 2 non se pode cambiar de golge a 4. v

# Agora ten en conta que aparecen novos modelos de bicicleta, BicicletaMontaña e BicicletaTandem.
# A bicicleta de montaña ten un atributo chamado suspensión. Que funciona igual que os outros, non pode valer negativo e so pode cambiar de 1 en 1.

# A BicicletaTandem ten un atributo que é numAsientos.

# O método acelerar na clase BicicletaMontaña triplica a velocidade, mentras que BicicletaTandem a cuadriplica.

# Lembra facer os test.

from functools import wraps
from typing import Callable

def no_negativo(func: Callable) -> Callable:
    """Decorador que impide asignar un valor numérico negativo a un setter."""
    @wraps(func)
    def envoltura(self, valor: int):
        if valor < 0:
            raise ValueError("El valor introducido no puede ser negativo")
        return func(self, valor)
    return envoltura

def cambio_de_uno(nombre_atributo: str) -> Callable:
    """Decorador que impide cambiar un atributo en más de 1 unidad de golpe."""
    def decorador(func: Callable) -> Callable:
        @wraps(func)
        def envoltura(self, valor: int):
            if hasattr(self, nombre_atributo):
                valor_actual = getattr(self, nombre_atributo)
                if abs(valor - valor_actual) != 1:
                    raise ValueError(f"El atributo '{nombre_atributo}' solo puede cambiar de 1 en 1")
            return func(self, valor)
        return envoltura
    return decorador

class Bicicleta:
    def __init__(self, velocidad_actual: int = 0, plato_actual: int = 1, pinnon_actual: int = 1):
        self.velocidad_actual = velocidad_actual
        self.plato_actual = plato_actual
        self.pinnon_actual = pinnon_actual

    @property
    def velocidad_actual(self) -> int:
        return self._velocidad_actual

    @property
    def plato_actual(self) -> int:
        return self._plato_actual

    @property
    def pinnon_actual(self) -> int:
        return self._pinnon_actual

    @velocidad_actual.setter
    @no_negativo
    def velocidad_actual(self, velocidad: int)-> None:
        self._velocidad_actual = velocidad

    @plato_actual.setter
    @no_negativo
    @cambio_de_uno("_plato_actual")
    def plato_actual(self, plato: int) -> None:
        if plato == 0:
            raise ValueError("Siempre habrá un plato activo")
        else:
            self._plato_actual = plato

    @pinnon_actual.setter
    @no_negativo
    @cambio_de_uno("_pinnon_actual")
    def pinnon_actual(self, pinnon: int) -> None:
        if pinnon == 0:
            raise ValueError("Siempre habrá un piñon activo") 
        else:
            self._pinnon_actual = pinnon

    def acelerar(self) -> None:
        if self.velocidad_actual == 0:
            self.velocidad_actual = 1
        else:
            self.velocidad_actual = 2 * self.velocidad_actual

    def frenar(self) -> None:
        self.velocidad_actual = self.velocidad_actual // 2

    def cambiar(self, variable: int, cambia: int) -> None:
        '''variable sólo tiene dos valores 0 o 1 para determinar si se cambia el piñón o el plato
        cambia solo tiene dos valores 1 o -1, para cambiar a un valor superior o inferior'''
        if variable == 0:
            self.pinnon_actual = self._pinnon_actual + cambia
        elif variable == 1:
            self.plato_actual = self._plato_actual + cambia
        else:
            raise ValueError("Dato no válido") 

class BicicletaMontanna(Bicicleta):
    def __init__(self, velocidad_actual: int = 0, plato_actual: int = 1, pinnon_actual: int = 1, suspension: int = 1):
        super().__init__(velocidad_actual, plato_actual, pinnon_actual)
        self.suspension = suspension
    
    @property
    def suspension(self) -> int:
        return self._suspension
    
    @suspension.setter
    @no_negativo
    @cambio_de_uno("_suspension")
    def suspension(self, valor: int) -> None:
        self._suspension = valor    

    def acelerar(self) -> None:
        if self.velocidad_actual == 0:
            self.velocidad_actual = 1
        else:
            self.velocidad_actual = 3 * self.velocidad_actual

    def cambiar(self, variable: int, cambia: int) -> None:
        """variable: 0 (piñón), 1 (plato) o 2 (suspensión). cambia: 1 o -1."""
        if variable == 2:
            self.suspension = self.suspension + cambia
        else:
            super().cambiar(variable, cambia)

class BicicletaTandem(Bicicleta):
    def __init__(self, velocidad_actual: int = 0, plato_actual: int = 1, pinnon_actual: int = 1, num_asientos: int = 2):
        super().__init__(velocidad_actual, plato_actual, pinnon_actual)
        self.num_asientos = num_asientos

    @property
    def num_asientos(self) -> int:
        return self._num_asientos
    
    @num_asientos.setter
    @no_negativo
    def num_asientos(self, valor: int) -> None:
        if valor < 2:
            raise ValueError("El número mínimo de asientos en una bicicleta tandem es 2") 
        else:
            self._num_asientos = valor    

    def acelerar(self) -> None:
        if self.velocidad_actual == 0:
            self.velocidad_actual = 1
        else:
            self.velocidad_actual = 4 * self.velocidad_actual

def comprobar_error(funcion, *args, **kwargs):
    """Función auxiliar para verificar que se lanza un ValueError."""
    try:
        funcion(*args, **kwargs)
        assert False, f"Se esperaba ValueError en {funcion}"
    except ValueError as e:
        print(f"OK (Error capturado correctamente): {e}")


if __name__ == "__main__":
    print("--- 1. PRUEBAS BICICLETA ESTÁNDAR ---")
    bici = Bicicleta()
    bici.acelerar()  # Pasa a 1
    bici.acelerar()  # Pasa a 2
    assert bici.velocidad_actual == 2
    
    bici.cambiar(0, 1)  # Sube piñón a 2
    bici.cambiar(1, 1)  # Sube plato a 2
    assert bici.pinnon_actual == 2 and bici.plato_actual == 2

    # Comprobar excepciones
    comprobar_error(setattr, bici, "velocidad_actual", -5)   # Negativo
    comprobar_error(setattr, bici, "plato_actual", 4)        # Salto mayor de 1
    bici.cambiar(1, -1)                                      # Baja plato a 1 (es válido, no debe dar error)
    comprobar_error(bici.cambiar, 1, -1)                     # Intenta bajar plato a 0 (aquí sí salta el error)

    print("\n--- 2. PRUEBAS BICICLETA MONTAÑA ---")
    mtb = BicicletaMontanna()
    mtb.acelerar()  # 1
    mtb.acelerar()  # 3
    assert mtb.velocidad_actual == 3
    
    mtb.cambiar(2, 1)  # Sube suspensión a 2 (nuevo)
    mtb.cambiar(0, 1)  # Sube piñón a 2 (heredado de Bicicleta)
    assert mtb.suspension == 2 and mtb.pinnon_actual == 2
    
    comprobar_error(mtb.cambiar, 2, 2)  # Salto de 2 en suspensión

    print("\n--- 3. PRUEBAS BICICLETA TÁNDEM ---")
    tandem = BicicletaTandem(num_asientos=3)
    tandem.acelerar()  # 1
    tandem.acelerar()  # 4
    assert tandem.velocidad_actual == 4 and tandem.num_asientos == 3
    
    comprobar_error(BicicletaTandem, num_asientos=1)  # Menos de 2 asientos

    print("\n¡Todas las pruebas pasaron con éxito!")

