from tarea43 import aplicar

def test_aplicar_none():
    assert (None, None) == aplicar(None, 1)

def test_aplicar_iva():
    assert (21, 121) == aplicar (21, 100)

def test_aplicar_descuento():
    assert (-10, 90) == aplicar (-10, 100)