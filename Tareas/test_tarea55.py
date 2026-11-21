from tarea55 import contar


def test_contar_valores_basicos():
    assert contar(1) == 1
    assert contar(5) == 15
    assert contar(10) == 55
    assert contar(100) == 5050


def test_contar_cero_o_negativo():
    assert contar(0) == 0
    assert contar(-5) == 0


def test_decorador_imprime_nombre_y_tiempo(capsys):
    resultado = contar(1000)
    assert resultado == 500500

    # capsys captura lo que el decorador imprimió por pantalla
    salida = capsys.readouterr().out
    assert "contar" in salida
    assert "segundos" in salida
