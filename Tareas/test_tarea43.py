from tarea43 import aplicar

def test_aplicar_none():
    assert (None, 1) == aplicar(1, None)

def test_aplicar_iva():
    assert (21, 121) == aplicar (100, 21)

def test_aplicar_descuento():
    assert (-10, 90) == aplicar (100, -10)