from decimal import Decimal
import pytest
from tarea61 import Personaxes, Droides, Bioloxicos, leer_archivo

def test_creacion_droide_y_str():
    droide = Droides(
        "R2-D2",
        Decimal("96"),
        Decimal("32"),
        Decimal("33"),
        "masculine",
        "Naboo",
        "Droid",
        ["A New Hope", "The Empire Strikes Back"],
    )
    assert droide.name == "R2-D2"
    assert droide.height == Decimal("96")
    assert isinstance(droide, Personaxes)

    texto = str(droide)
    assert "R2-D2" in texto
    assert "Naboo" in texto
    assert "A New Hope" in texto

def test_creacion_biologico_y_str():
    luke = Bioloxicos(
        "Luke Skywalker",
        Decimal("172"),
        Decimal("77"),
        Decimal("19"),
        "masculine",
        "Tatooine",
        "Human",
        ["A New Hope"],
        "blond",
        "fair",
        "blue",
        "male",
    )
    assert luke.hair_color == "blond"
    assert luke.eye_color == "blue"
    assert isinstance(luke, Personaxes)

    texto = str(luke)
    assert "Luke Skywalker" in texto
    assert "blond" in texto
    assert "blue" in texto

def test_decorador_comprobar_tipo_lanza_error():
    with pytest.raises(TypeError):
        Droides(
            1234,  # Error: se espera str
            Decimal("96"),
            Decimal("32"),
            Decimal("33"),
            "masculine",
            "Naboo",
            "Droid",
            ["A New Hope"],
        )

    with pytest.raises(TypeError):
        Droides(
            "C-3PO",
            "167",  # Error: se espera Decimal, no str
            Decimal("75"),
            Decimal("112"),
            "masculine",
            "Tatooine",
            "Droid",
            ["A New Hope"],
        )

def test_leer_archivo_csv():
    personajes = leer_archivo()
    assert len(personajes) > 0
    assert any(isinstance(p, Droides) for p in personajes)
    assert any(isinstance(p, Bioloxicos) for p in personajes)
    assert not all(isinstance(p, Droides) for p in personajes)
