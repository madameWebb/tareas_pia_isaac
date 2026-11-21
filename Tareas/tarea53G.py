import random


class Blackjack:
    def __init__(self, baraja: dict[str, list[tuple[str, int]]], jugadores: list[str]):
        self._baraja = baraja
        self._jugadores = jugadores
        self._crupier = "Crupier"

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
    def baraja(self, baraja: dict[str, list[tuple[str, int]]]) -> None:
        self._baraja = baraja


def configurar_juego() -> Blackjack | None:
    while True:
        try:
            opcion = int(input(
                "¿Jugamos al Blackjack? Yo soy el crupier.\n"
                "Elige para comenzar:\n"
                "  1- Jugar\n"
                "  2- Salir\n"
                "> "
            ))
        except ValueError:
            print("Por favor, introduce un número válido.\n")
            continue

        if opcion == 2:
            print("Hasta pronto.")
            return None

        if opcion == 1:
            valor_cartas = list(range(1, 11))
            clave_valores = [str(n) for n in valor_cartas]
            clave_valores[0] = "A"  # Representamos el 1 como As ('A')
            valor_cartas.extend([10] * 3)
            clave_valores.extend(["J", "Q", "K"])
            cartas = list(zip(clave_valores, valor_cartas))

            try:
                n_jugadores = int(input("¿Cuántos jugadores van a participar? "))
                n_barajas = int(input("¿Cuántas barajas vamos a utilizar (1, 2, 4, 6, 8)? "))
            except ValueError:
                print("Debes introducir valores numéricos.\n")
                continue

            if n_barajas in {1, 2, 4, 6, 8} and n_jugadores >= 1:
                jugadores: list[str] = []
                for i in range(1, n_jugadores + 1):
                    nombre = input(f"Escribe el nombre del jugador {i}: ").strip()
                    jugadores.append(nombre or f"Jugador {i}")

                cartas = cartas * n_barajas
                baraja = {
                    "Corazones": cartas.copy(),
                    "Diamantes": cartas.copy(),
                    "Tréboles": cartas.copy(),
                    "Picas": cartas.copy(),
                }
                return Blackjack(baraja, jugadores)
            else:
                print("Número de barajas o jugadores no válido.\n")
        else:
            print("Has escogido un número incorrecto.\n")


def sacar_carta(juego: Blackjack, mano: list[tuple[str, str, int]]) -> None:
    palos_con_cartas = [palo for palo, lista in juego.baraja.items() if len(lista) > 0]
    palo = random.choice(palos_con_cartas)
    indice = random.randrange(len(juego.baraja[palo]))
    nombre, valor = juego.baraja[palo].pop(indice)
    mano.append((palo, nombre, valor))


def formatear_mano(mano: list[tuple[str, str, int]]) -> str:
    return ", ".join(f"{nombre} de {palo}" for palo, nombre, _ in mano)


def puntuar(mano: list[tuple[str, str, int]]) -> int:
    puntuacion = 0
    tiene_as = False

    for _, nombre, valor in mano:
        puntuacion += valor
        if nombre == "A":
            tiene_as = True

    # El As vale 11 mientras no nos pasemos de 21
    if tiene_as and puntuacion + 10 <= 21:
        puntuacion += 10

    return puntuacion


def jugar(juego: Blackjack) -> None:
    manos: dict[str, list[tuple[str, str, int]]] = {jugador: [] for jugador in juego.jugadores}
    manos[juego.crupier] = []

    # Reparto inicial de 2 cartas a cada participante
    for _ in range(2):
        for participante in manos:
            sacar_carta(juego, manos[participante])

    # Mostramos solo la primera carta del crupier (como en el casino real)
    carta_visible = manos[juego.crupier][0]
    print(f"\nCarta visible del {juego.crupier}: {carta_visible[1]} de {carta_visible[0]}")

    # Turno de cada jugador
    for jugador in juego.jugadores:
        puntuacion = puntuar(manos[jugador])
        print(f"\n--- Turno de {jugador} ---")
        print(f"Tus cartas: {formatear_mano(manos[jugador])} (Puntos: {puntuacion})")

        if puntuacion == 21:
            print(f"¡Blackjack de {jugador}!")
            continue

        while puntuacion < 21:
            try:
                opcion = int(input("¿Quieres otra carta? (1- Sí / 2- Me planto): "))
            except ValueError:
                print("Introduce 1 o 2.")
                continue

            if opcion == 1:
                sacar_carta(juego, manos[jugador])
                puntuacion = puntuar(manos[jugador])
                print(f"Tus cartas: {formatear_mano(manos[jugador])} (Puntos: {puntuacion})")
            elif opcion == 2:
                print(f"{jugador} se planta con {puntuacion} puntos.")
                break
            else:
                print("Opción incorrecta.")

        if puntuacion > 21:
            print(f"{jugador} se ha pasado de 21.")

    # Turno automático del crupier
    print(f"\n--- Turno del {juego.crupier} ---")
    puntos_crupier = puntuar(manos[juego.crupier])
    print(f"Cartas del {juego.crupier}: {formatear_mano(manos[juego.crupier])} (Puntos: {puntos_crupier})")

    while puntos_crupier < 17:
        sacar_carta(juego, manos[juego.crupier])
        puntos_crupier = puntuar(manos[juego.crupier])
        print(f"{juego.crupier} saca carta: {formatear_mano(manos[juego.crupier])} (Puntos: {puntos_crupier})")

    if puntos_crupier > 21:
        print(f"El {juego.crupier} se ha pasado de 21.")

    determinar_ganador(manos)


def determinar_ganador(manos: dict[str, list[tuple[str, str, int]]]) -> None:
    puntos_validos = {
        participante: puntuar(cartas)
        for participante, cartas in manos.items()
        if puntuar(cartas) <= 21
    }

    print("\n=== RESULTADO FINAL ===")
    if not puntos_validos:
        print("Todos se han pasado de 21. Nadie gana.")
        return

    mayor_valor = max(puntos_validos.values())
    ganadores = [nombre for nombre, pts in puntos_validos.items() if pts == mayor_valor]

    if len(ganadores) == 1:
        print(f"Gana {ganadores[0]} con {mayor_valor} puntos.")
    else:
        print(f"Empate entre {', '.join(ganadores)} con {mayor_valor} puntos.")


if __name__ == "__main__":
    partida = configurar_juego()
    if partida is not None:
        jugar(partida)
