from tarea42 import calcular_area, calcular_volumen

def test_calcular_area():
    assert 3.141592653589793 == calcular_area(1)

def test_calcular_volumen():
    assert 3.141592653589793, 6.283185307179586 == calcular_volumen(2, 2)