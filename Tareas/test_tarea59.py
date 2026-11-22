import pytest
from tarea59 import sumar, restar, multiplicar, dividir

def test_operaciones_basicas():
    assert sumar(4, 2) == 6
    assert restar(4, 2) == 2
    assert multiplicar(4, 2) == 8

def test_dividir_exacta_y_no_exacta():
    assert dividir(10, 2) == 5
    assert isinstance(dividir(10, 2), int)
    assert dividir(10, 3) is None

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

def test_tipos_no_enteros_lanzan_error():
    with pytest.raises(TypeError):
        sumar(2.5, 3)
    with pytest.raises(TypeError):
        dividir("10", 2)

