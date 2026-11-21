# O xogo do blackjack… simple.

# Ao blackjack se xoga con baralla francesa: A,K,Q,J,10..2 un total de 52 cartas.

# As cartas se agrupan en mans e a puntuación da man se conseguir sumando a puntuación de cada carta tendo en conta que:

#     cada carta númerica vale o seu número
#     as cartas K,Q,J valen 10
#     O as pode valer 11 ou 1, dependendo do necesario.

# A puntuación máis alta obxectivo é chegar 21. Se a man ten mais de 21 puntos se perde.

# Cada xogador ten unha man e se elixe ao gañador (se o hai) como o que ten a puntuación maior (sen pasarse do límite)

class Blackjack:
    def __init__(self, baraja:dict[str, list[tuple[str, int]]], jugadores:list[str]):
        self._baraja = baraja
        self._jugadores = jugadores
        self._crupier = "crupier"

    @property
    def baraja(self) -> dict[str, list[tuple[str, int]]]:
        return self._baraja
    @property
    def jugadores(self) -> list[str]:
        return self._jugadores
    @property
    def crupier(self) -> str:
        return self._crupier

    @baraja.setter
    def baraja(self, baraja:dict[str, list[tuple[str, int]]]) -> None:
        self._baraja = baraja

    
def configurar_juego() -> Blackjack | None:
    juego: Blackjack
    opcion = int(input(
        """Jugamos al blackjack? yo soy el cuprier.
        Elige para comenzar:
            1- jugar
            2- salir
            """))
    if opcion == 2:
        print("Hasta pronto")
        return None
    elif opcion == 1:
        baraja: dict[str, list[tuple]] = {}
        valor_cartas = list(range(1,11))
        clave_valores =  [str(n) for n in valor_cartas]
        valor_cartas.extend([10]*3)
        clave_valores.extend(["J", "Q", "K"])
        cartas = list(zip(clave_valores, valor_cartas)) #lista de tuplas

        jugadores: list[str] = []

        n_jugadores = int(input("""Cuantos jugadores van a participar? """)) 
        n_barajas = int(input("""Cuantas barajas vamos a utilizar? """)) 
        if n_barajas in {1, 2, 4, 6, 8} and n_jugadores >=1:  
            for _ in range(n_jugadores):
                jugadores.append(str(input("Escribe el nombre del jugador: ")))
            cartas = cartas * n_barajas
            baraja = {
                        "Corazones": cartas.copy(),
                        "Diamantes": cartas.copy(),
                        "Treboles" : cartas.copy(),
                        "Picas" : cartas.copy() 
                    }
            juego =  Blackjack(baraja, jugadores)
            return juego 
        else:
            print("Número de barajas o jugadores no válido.")
            return configurar_juego()              
    else:
        print("Has escogico un número incorrecto")
        return configurar_juego()

def jugar(juego: Blackjack)-> None:
    manos = {jugador: [] for jugador in juego.jugadores}
    manos["Crupier"] = []
        
    for _ in range(2):  # Repartimos 2 cartas iniciales a cada uno
        for participante in manos:
            sacar_carta(juego, manos[participante])
    pedir_carta(juego, manos)

def sacar_carta(juego, participante):
    import random
    palo = random.choice(list(juego.baraja.keys()))
    indice = random.randrange(len(juego.baraja[palo]))
    nombre, valor = juego.baraja[palo].pop(indice)
    participante.append((palo, nombre, valor))

def pedir_carta(juego, manos):
    for jugador in juego.jugadores:
        print(f"\nTurno de {jugador}. Tus cartas: {manos[jugador]}")
        puntuacion = puntuar(manos[jugador])
        print(puntuacion)
        while True:
            opcion = int(input("""Quieres otra carta? 
                        Elige: 
                            1- Si
                            2- Me planto
                            """))
            if opcion == 1:
                sacar_carta(juego, manos[jugador])
                print(manos[jugador])
                puntuacion = puntuar(manos[jugador])
                print(puntuacion)
                if puntuacion >= 21:
                    break
            elif opcion == 2: #suma de las cartas
                print(f"{jugador} se planta.")
                print(puntuacion)
                break
            else:
                print("opción incorrecta")
    #Turno Crupier
    puntos_crupier = puntuar(manos["Crupier"])
    print("Turno Crupier")
    print(manos["Crupier"])
    print(puntos_crupier)
    if puntos_crupier <= 16:
        while puntos_crupier < 17:
            sacar_carta(juego, manos["Crupier"])
            puntos_crupier = puntuar(manos["Crupier"])
            print(puntos_crupier)
    else:
        print(puntos_crupier)
    determinar_ganador(manos)

def puntuar(manos):
    puntuacion: int = 0
    for i in range(len(manos)):
        puntuacion += manos[i][2]
    return puntuacion

def determinar_ganador(manos):
    puntos_validos = {}

    for participante, cartas in manos.items():
        puntos = puntuar(cartas)
        if puntos <= 21:
            puntos_validos[participante] = puntos
    if len(puntos_validos) == 0:
        print("Nadie gana")
    else:
        mayor_valor = max(puntos_validos.values())
        ganador = max(puntos_validos, key=puntos_validos.get)
        print(f"Gana: {ganador} con {mayor_valor} puntos")

if __name__ == "__main__":
    juego = configurar_juego()
    if juego is not None:
        jugar(juego)