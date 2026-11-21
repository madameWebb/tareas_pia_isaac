from pytest import raises
from tarea54 import Vehiculo


def test_creacion_valida():
    v = Vehiculo("600", 100, 50)
    assert v.nombre == "600"
    assert v.velocidad_max == 100
    assert v.kilometraje == 50


def test_creacion_invalida_lanza_error():
    with raises(ValueError):
        Vehiculo("600", -10, 0)
    with raises(ValueError):
        Vehiculo("600", 100, -5)


def test_decorador_no_negativo():
    v = Vehiculo("600", 100, 0)
    with raises(ValueError):
        v.velocidad_max = -20
    assert v.velocidad_max == 100  # Mantiene el valor anterior

    v.velocidad_max = 0  # El 0 sí es válido (no es negativo)
    assert v.velocidad_max == 0


def test_decorador_no_disminuye():
    v = Vehiculo("850", 120, 100)
    v.kilometraje = 150
    assert v.kilometraje == 150

    v.kilometraje = 150  # Mantener el mismo kilometraje es válido
    assert v.kilometraje == 150

    with raises(ValueError):
        v.kilometraje = 120
    assert v.kilometraje == 150  # Mantiene el valor anterior


def test_transformacion_str():
    v = Vehiculo("600", 100, 50)
    texto = str(v)
    assert "600" in texto
    assert "100" in texto
    assert "50" in texto
