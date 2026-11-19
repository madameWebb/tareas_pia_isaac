# Esta tarefa é igual que a anterior, cunhas pequenas modificacións, polo que se pode partir do feito nela.

# Co feito ata o de agora, cando se crea unha instancia se valida o número co algoritmo de Lunh. Pero que pasa despois? O numero de tarxeta pode ser cambiado e non se valida para nada.

# Usa properties para modificar isto, de tal xeito que o número de tarxeta sexa validado cando se lle intente cambiar o valor. Se o número non e correcto, o usuario debe manter o código de tarxeta anterior e se debe lanzar unha excepción.


class Persona:
    def __init__(self, nombre: str, usuario: str, clave: str, tarjeta: str | None = None):
        self._nombre = nombre
        self._usuario = usuario
        self._clave = clave
        self._tarjeta = None
        if tarjeta is not None:
            self.tarjeta = tarjeta

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def usuario(self) -> str:
        return self._usuario  

    @property
    def tarjeta(self) -> bool | str:
        if self._tarjeta is None:
            return False
        return self._tarjeta 

    @tarjeta.setter
    def tarjeta(self, valor: str) -> None:
        if self.comprobar_numero(valor):
            self._tarjeta = valor
        else: 
            raise ValueError("Número no válido")

    def comprobar_numero(self, numero: str) -> bool:
        limpio = "".join(numero.split())
        if len(limpio) == 16 and limpio.isdigit():
            resultado = list(limpio)
            i = 0
            while i < 16:
                digito = int(resultado[i]) * 2
                if digito > 9:
                    digito = digito - 9
                resultado[i] = str(digito)
                i += 2

            suma = 0
            for elemento in resultado:
                suma += int(elemento)

            return suma % 10 == 0
        return False


if __name__ == "__main__":
    # user = Persona("Jose", "jos", "clave")
    # user2 = Persona("Jose", "jos", "clave", "4539 3195 0343 6467")
    # user.set_tarjeta("1234 5678 9101 1121")
    # user2.set_tarjeta("3195 4539 0343 6467")
        
    
    # if user.get_tarjeta():
    #     print(user.get_tarjeta())
    # else:
    #     print("Error: No has introducido un número válido.")

    # if user2.get_tarjeta():
    #     print(user2.get_tarjeta())
    # else:
    #     print("Error: No has introducido un número válido.")
    user = Persona("Jose", "jos", "clave", "4539 3195 0343 6467")
    print("Tarjeta inicial:", user.tarjeta)

    try:
        # Intentamos cambiarla por una falsa
        user.tarjeta = "1234 5678 9101 1121"
    except ValueError as e:
        print("Excepción capturada:", e)

    # Comprobamos que mantiene la tarjeta válida anterior
    print("Tarjeta tras el intento fallido:", user.tarjeta)