# Escribe un programa onde declares unha clase vehiculo con velocidade máxima e kilometraxe coma atributos.

# Controla que a velocidade máxima non pode ser negativa, e que o kilometraxe nunca pode descender.

# Implementa a transformación do obxecto vehiculo a string.

# Fai os test correspondentes

class Vehiculo:
    def __init__(self, nombre: str, velocidad_max: float, kilometraje: float = 0):
        self._nombre = nombre
        self._velocidad_max = 0
        self._kilometraje = 0
        # Pasamos por los setters para validar desde el inicio
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
    def velocidad_max(self, valor: float) -> None:
        if self.comprobar_vel(valor):
            self._velocidad_max = valor
        else: 
            raise ValueError("La velocidad introducida no puede ser negativa")

    @kilometraje.setter
    def kilometraje(self, valor: float) -> None:
        if self.comprobar_kilometraje(valor):
            self._kilometraje = valor
        else: 
            raise ValueError("El kilometraje no puede descender")

    def comprobar_vel(self, valor: float) -> bool:
        return valor >= 0

    def comprobar_kilometraje(self, valor: float) -> bool:
        return valor >= self.kilometraje

    def __str__(self) -> str:
        return f"Vehículo: {self._nombre} | Velocidad máx: {self._velocidad_max} km/h | Kilometraje: {self._kilometraje} km"


if __name__ == "__main__":
    vehiculo1 = Vehiculo("600", 100, 0)
    vehiculo2 = Vehiculo("850", 120, 100)
    
    # Prueba de transformación a string (__str__)
    print(vehiculo1)
    print(vehiculo2)

    # Test 1: Subir kilometraje (válido)
    vehiculo2.kilometraje = 150
    print("\nTras actualizar km:", vehiculo2)

    # Test 2: Intentar bajar kilometraje (debe lanzar excepción y mantener 150)
    try:
        vehiculo2.kilometraje = 120
    except ValueError as e:
        print("Excepción capturada (km):", e)
    print("Kilometraje actual:", vehiculo2.kilometraje)

    # Test 3: Intentar poner velocidad negativa (debe lanzar excepción)
    try:
        vehiculo1.velocidad_max = -20
    except ValueError as e:
        print("Excepción capturada (velocidad):", e)
    print("Velocidad actual:", vehiculo1.velocidad_max)
