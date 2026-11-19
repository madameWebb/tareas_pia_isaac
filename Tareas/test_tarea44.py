from tarea44 import aplicar, funcion

def test_aplicar_numero():
    assert [1, 4, 9, 16] == aplicar([1, 2, 3, 4],funcion)

def test_aplicar_str():
    assert "Esto es una lista" == aplicar("esto es una lista",funcion)

def test_aplicar_int():
    assert 25 == aplicar(5,funcion)

def test_aplicar_list():
    assert ['A', 'B', 'C', 16] == aplicar(['a', 'b', 'c', 4],funcion)


def test_funcion_numero():
    assert [1, 4, 9, 16] == funcion([1, 2, 3, 4])

def test_funcion_str():
    assert "Esto es una lista" == funcion("esto es una lista")

def test_funcion_int():
    assert 25 == funcion(5)

def test_funcion_list():
    assert ['A', 'B', 'C', 16] == funcion(['a', 'b', 'c', 4])