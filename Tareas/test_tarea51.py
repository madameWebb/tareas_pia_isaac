import pytest
from tarea51 import Vehiculo

def test_creacion_vehiculo():
    v = Vehiculo("600", 100, 50)
    assert v.nombre == "600"
    assert v.velocidad_max == 100
    assert v.kilometraje == 50

def test_velocidad_negativa():
    v = Vehiculo("600", 100, 0)
    with pytest.raises(ValueError):
        v.velocidad_max = -10
    assert v.velocidad_max == 100

def test_kilometraje_no_desciende():
    v = Vehiculo("850", 120, 100)
    v.kilometraje = 150
    assert v.kilometraje == 150
    with pytest.raises(ValueError):
        v.kilometraje = 80
    assert v.kilometraje == 150

def test_str():
    v = Vehiculo("600", 100, 0)
    assert "600" in str(v)
    assert "100" in str(v)
