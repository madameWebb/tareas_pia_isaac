from decimal import Decimal
import pytest
from tarea60 import calcular_media, nota_maxima, nota_minima, aprobado

def test_calculos_notas_validas():
    notas = [Decimal("5"), Decimal("5.25"), Decimal("8"), Decimal("4")]
    assert calcular_media(notas) == Decimal("5.5625")
    assert nota_maxima(notas) == Decimal("8")
    assert nota_minima(notas) == Decimal("4")

def test_aprobado_y_suspenso():
    assert aprobado(Decimal("5")) is True
    assert aprobado(Decimal("8.75")) is True
    assert aprobado(Decimal("4.99")) is False

def test_lista_vacia_lanza_excepcion():
    with pytest.raises(ValueError):
        calcular_media([])
    with pytest.raises(ValueError):
        nota_maxima([])
    with pytest.raises(ValueError):
        nota_minima([])
