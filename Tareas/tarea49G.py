# No sistema temos presente usuarios. Cada un deles ten un nome, un nome de usuario, un contrasinal e un número de tarxeta. O número de tarxeta segue a fórmula de Luhn. Os usuarios poden ter establecido o número de tarxeta ou non, en todo caso, se o teñen ten que seguir a fórmula.

# Pensa primeiramente que relación existe entre os usuarios e os números de Lunh, e logo implementa.

# O algoritmo de Luhn é unha fórmula de suma de comprobación sinxela que se usa para validar unha variedade de números de identificación, como os números de tarxeta de crédito e os números de seguridade social canadense.

# Na tarefa haberá comprobar se unha cadea determinada é válida. Para indicar que non é válida deberemos lanzar unha excepción.
# Validación do numero

# As cadeas de lonxitude 1 ou inferior non son válidas. Os espazos están permitidos na entrada, pero deben eliminarse antes de verificalos. Os únicos caracteres válidos son os números 0..9
# Exemplo 1: número de tarxeta de crédito válido

# 4539 3195 0343 6467

# O primeiro paso do algoritmo de Luhn é duplicar os díxitos en posición par, comezando pola dereita. Dobraremos

# 4_3_ 3_9_ 0_4_ 6_6_

# Se duplicando o número resulta un número maior que 9, resta 9 do produto.

# No exemplo, o primeiro par que atopamos é o 6. 6 * 2 = 12, maior que 9, así que 12 - 9 = 3, que será o número que se pon.

# Aplicando o dito ao código de antes:

# 8569 6195 0383 3437

# Despois suma todos os díxitos:

# 8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80

# Se a suma é divisible por 10, entón o número é válido. Este número é válido!
# Exemplo 2: número de tarxeta de crédito non válido

# 8273 1232 7352 0569

# Dobra os díxitos en posición par, comezando pola dereita

# 7253 2262 5312 0539

# Suma os díxitos

# 7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57

# 57 non é divisible por 10, polo que este número non é válido.


class Persona:
    def __init__(self, nombre: str, usuario: str, clave: str, tarjeta: str | None = None):
        self._nombre = nombre
        self._usuario = usuario
        self._clave = clave
        self._tarjeta = None
        if tarjeta is not None:
            self.set_tarjeta(tarjeta)

    def get_nombre(self) -> str:
        return self._nombre

    def get_usuario(self) -> str:
        return self._usuario  

    def get_tarjeta(self) -> bool | str:
        if self._tarjeta is None:
            return False
        return self._tarjeta 

    def set_tarjeta(self, valor: str) -> None:
        if self.comprobar_numero(valor):
            self._tarjeta = valor

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
    user = Persona("Jose", "jos", "clave")
    user2 = Persona("Jose", "jos", "clave", "4539 3195 0343 6467")
    user.set_tarjeta("1234 5678 9101 1121")
    user2.set_tarjeta("3195 4539 0343 6467")
        
    
    if user.get_tarjeta():
        print(user.get_tarjeta())
    else:
        print("Error: No has introducido un número válido.")

    if user2.get_tarjeta():
        print(user2.get_tarjeta())
    else:
        print("Error: No has introducido un número válido.")
