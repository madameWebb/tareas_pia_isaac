import pytest
from tarea57 import eliminar_datos, ErrorPermisos

def test_administradores_pueden_ejecutar(capsys):
    # Ejecutamos con las dos administradoras de la tabla
    eliminar_datos("Ana")
    eliminar_datos("María")

    # Comprobamos que se imprimió el texto esperado
    salida = capsys.readouterr().out
    assert "Pasé por aquí" in salida

def test_usuarios_normales_lanzan_error():
    # Comprobamos que Pedro y Xoán provocan la excepción ErrorPermisos
    with pytest.raises(ErrorPermisos):
        eliminar_datos("Pedro")

    with pytest.raises(ErrorPermisos):
        eliminar_datos("Xoán")

def test_usuario_no_registrado_lanza_error():
    # Comprobamos que alguien fuera del diccionario tampoco pasa
    with pytest.raises(ErrorPermisos):
        eliminar_datos("Luis")

