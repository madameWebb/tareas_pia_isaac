# Tarefa 61. Star Wars

# Non seguinte ficheiro temos datos de personaxes de star wars:

#     por un lado temos os seres biolóxicos, que teñen as seguintes caracteristicas: 
# name, height, mass, hair_color, skin_color, eye_color, birth_year, sex, gender, homeworld, species, films v
#     por outro teremos os droides, que teñen as seguintes características: 
# name, height, mass, birth_year, gender, homeworld, films v

# O atributo films é unha lista separada por comas de películas. v

#     Crea as clases que creas necesarias e asigna un tipo de dato correcto a cada atributo no momento da lectura.  v
#     Implementa o método str 
#     Lee todas as liñas do ficheiro e crea unha instancia de un obxecto que represente ao personaxe e introduceos todos nunha única lista.

# Unha vez listo todo, fai código para:

#     Imprime o conxunto completo de personaxes.
#     Imprime só os personaxes que non sexan droids.

# Lmebra, usar type hints e demais.

from decimal import Decimal
from functools import wraps
from typing import Callable
import csv

def comprobar_tipo(tipo_esperado: type) -> Callable:
    """Decorador que comprueba el tipo correcto."""
    def decorador(func: Callable) -> Callable:
        @wraps(func)
        def envoltura(self, valor: str | Decimal | list[str] , *args, **kwargs):
            if not isinstance(valor, tipo_esperado):
                raise TypeError(
                    f"Se esperaba {tipo_esperado.__name__}, pero se recibió {type(valor).__name__}."
                )
            return func(self, valor, *args, **kwargs)
        return envoltura
    return decorador

class Personaxes:
    def __init__(self, name: str, height: Decimal, mass: Decimal, birth_year: int, gender: str, homeworld: str, films: list[str] ):
        self.name = name
        self.height = height
        self.mass = mass
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.films = films

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def height(self) -> Decimal:
        return self._height
    
    @property
    def mass(self) -> Decimal:
        return self._mass
    
    @property
    def birth_year(self) -> int:
        return self._birth_year
    
    @property
    def gender(self) -> str:
        return self._gender

    @property
    def homeworld(self) -> str:
        return self._homeworld

    @property
    def films(self) -> list[str]:
        return self._name

    @name.setter
    @comprobar_tipo(str)
    def name(self, valor: str)-> None:
        self._name = valor

    @height.setter
    @comprobar_tipo(Decimal)
    def height(self, valor: Decimal)-> None:
        self._height = valor

    @mass.setter
    @comprobar_tipo(Decimal)
    def mass(self, valor: Decimal)-> None:
        self._mass = valor

    @birth_year.setter
    @comprobar_tipo(int)
    def birth_year(self, valor: int)-> None:
        self._birth_year = valor
            
    @gender.setter
    @comprobar_tipo(str)
    def gender(self, valor: str)-> None:
        self._gender = valor

    @homeworld.setter
    @comprobar_tipo(str)
    def homeworld(self, valor: str)-> None:
        self._homeworld= valor
    
    @films.setter
    @comprobar_tipo(list[str])
    def films(self, valor: list[str])-> None:
        self._films = valor

    def __str__(self):
        cadena: str = ""
        for film in self.films:
            cadena = f"{film}\n"
        return f"Personaxe: {self.name}\n Películas: {cadena}\n Plameta de origen: {self.homeworld}\n Altura: {self.height}\n Peso: {self.mass} \n Año de nacimiento: {self.birth_year}\n Genero: {self.gender}\n"
        


class Droides(Personaxes):
    def __init__(self, name: str, height: Decimal, mass: Decimal, birth_year: int, gender: str, homeworld: str, films: list[str] ):          
        super()._init__(self, name, height, mass, birth_year, gender, homeworld, films)

class Bioloxicos(Personaxes):
    def __init__(self, name: str, height: Decimal, mass: Decimal, birth_year: int, gender: str, homeworld: str, films: list[str], hair_color: str, skin_color: str, eye_color: str, sex: str ):          
        super()._init__(self, name, height, mass, birth_year, gender, homeworld, films)
        self._hair_color = hair_color 
        self._skin_color = skin_color
        self._eye_color = eye_color
        self._sex = sex 

    @property
    def hair_color(self) -> str:
        return self._hair_color
    
    @property
    def skin_color(self) -> str:
        return self._skin_color
    
    @property
    def eye_color(self) -> str:
        return self._eye_color
    
    @property
    def sex(self) -> str:
        return self._sex

    @hair_color.setter
    @comprobar_tipo(str)
    def hair_color(self, valor: str)-> None:
        self._hair_color = valor

    @skin_color.setter
    @comprobar_tipo(str)
    def skin_color(self, valor: str)-> None:
        self._skin_color = valorPersonaxe: 

    @eye_color.setter
    @comprobar_tipo(str)
    def eye_color(self, valor: str)-> None:
        self._eye_color = valor

    @sex.setter
    @comprobar_tipo(str)
    def sex(self, valor: str)-> None:
        self._sex = valor

    def __str__(self):
        cadena: str = super().__str__()
        
        return f"{cadena}\n Color de pelo: {self.hair_color}\n Color de piel: {self.skin_color} \n color de ojos: {self.eye_color}\n Sexo biológico: {self.sex}"

#     with open('eggs.csv', newline='') as csvfile:
# ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# ...     for row in spamreader:
# ...         print(', '.join(row))