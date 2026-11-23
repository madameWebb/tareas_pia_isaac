# Tarefa 61. Star Wars

# Non seguinte ficheiro temos datos de personaxes de star wars:

#     por un lado temos os seres biolóxicos, que teñen as seguintes caracteristicas: 
# name, height, mass, hair_color, skin_color, eye_color, birth_year, sex, gender, homeworld, species, films v
#     por outro teremos os droides, que teñen as seguintes características: 
# name, height, mass, birth_year, gender, homeworld, films v

# O atributo films é unha lista separada por comas de películas. v

#     Crea as clases que creas necesarias e asigna un tipo de dato correcto a cada atributo no momento da lectura.  v
#     Implementa o método str v
#     Lee todas as liñas do ficheiro e crea unha instancia de un obxecto que represente ao personaxe e introduceos todos nunha única lista.

# Unha vez listo todo, fai código para:

#     Imprime o conxunto completo de personaxes.
#     Imprime só os personaxes que non sexan droids.

# Lmebra, usar type hints e demais.

from decimal import Decimal
from functools import wraps
from typing import Callable
import csv
from pathlib import Path

def comprobar_tipo(tipo_esperado: type) -> Callable:
    """Decorador que comprueba el tipo correcto."""
    def decorador(func: Callable) -> Callable:
        @wraps(func)
        def envoltura(self, valor: str | Decimal | list , *args, **kwargs):
            if not isinstance(valor, tipo_esperado):
                raise TypeError(
                    f"Se esperaba {tipo_esperado.__name__}, pero se recibió {type(valor).__name__}."
                )
            return func(self, valor, *args, **kwargs)
        return envoltura
    return decorador

class Personaxes:
    def __init__(self, name: str, height: Decimal, mass: Decimal, birth_year: Decimal, gender: str, homeworld: str, species: str, films: list[str] ):
        self.name = name
        self.height = height
        self.mass = mass
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.species = species
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
    def birth_year(self) -> Decimal:
        return self._birth_year
    
    @property
    def gender(self) -> str:
        return self._gender

    @property
    def homeworld(self) -> str:
        return self._homeworld

    @property
    def species(self) -> str:
        return self._species

    @property
    def films(self) -> list[str]:
        return self._films

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
    @comprobar_tipo(Decimal)
    def birth_year(self, valor: Decimal)-> None:
        self._birth_year = valor
            
    @gender.setter
    @comprobar_tipo(str)
    def gender(self, valor: str)-> None:
        self._gender = valor

    @homeworld.setter
    @comprobar_tipo(str)
    def homeworld(self, valor: str)-> None:
        self._homeworld= valor

    @species.setter
    @comprobar_tipo(str)
    def species(self, valor: str)-> None:
        self._species= valor
    
    @films.setter
    @comprobar_tipo(list)
    def films(self, valor: list[str])-> None:
        self._films = valor

    def __str__(self):
        cadena: str = ""
        for film in self.films:
            cadena += f"\n\t{film}"
        return f"\n Personaxe: {self.name}\n\n Películas: {cadena}\n\n Plameta de origen: {self.homeworld}\n Altura: {self.height}\n Peso: {self.mass} \n Año de nacimiento: {self.birth_year}\n Genero: {self.gender}\n Especie: {self.species}"
class Droides(Personaxes):
    def __init__(self, name: str, height: Decimal, mass: Decimal, birth_year: Decimal, gender: str, homeworld: str, species: str, films: list[str] ):          
        super().__init__(name, height, mass, birth_year, gender, homeworld, species, films)
    def __str__(self):
        cadena: str = super().__str__()
        
        return f"{cadena}\n__________________________________________"


class Bioloxicos(Personaxes):
    def __init__(self, name: str, height: Decimal, mass: Decimal, birth_year: Decimal, gender: str, homeworld: str, species:str, films: list[str], hair_color: str, skin_color: str, eye_color: str, sex: str ):          
        super().__init__(name, height, mass, birth_year, gender, homeworld, species, films)
        self.hair_color = hair_color 
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.sex = sex 

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
        self._skin_color = valor

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
        
        return f"{cadena}\n Color de pelo: {self.hair_color}\n Color de piel: {self.skin_color} \n color de ojos: {self.eye_color}\n Sexo biológico: {self.sex}\n__________________________________________"

def leer_archivo() -> list[Personaxes]:
    lista_personaxes: list[Personaxes] = []
    lista_aux: list[list[str | Decimal]] = []
    ruta_csv = Path(__file__).parent / "starwars.csv"
    with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo, delimiter=",", quotechar='"')
        claves: list[str] = next(lector)  # Salta o guarda la primera fila
        
        for fila in lector:
            lista_aux.append(["0" if x == "NA" or x == "none" else x for x in fila])
        for elemento in lista_aux:
            diccionario: dict[str, str | Decimal] = dict(zip(claves, elemento))
            films: list[str] = [f.strip() for f in str(diccionario["films"]).split(",")]
            
            for clave in ("height", "mass", "birth_year"):
                diccionario[clave] = Decimal(str(diccionario[clave]))
            
            if diccionario["species"] == "Droid":
                lista_personaxes.append(Droides(diccionario["name"], diccionario["height"], diccionario["mass"], diccionario["birth_year"], diccionario["gender"], diccionario["homeworld"], diccionario["species"], films))
            else:
                lista_personaxes.append(Bioloxicos(diccionario["name"], diccionario["height"], diccionario["mass"], diccionario["birth_year"], diccionario["gender"], diccionario["homeworld"], diccionario["species"], films, diccionario["hair_color"], diccionario["skin_color"], diccionario["eye_color"], diccionario["sex"]))
    return lista_personaxes

LISTA_PERSONAXES: list[Personaxes] = leer_archivo()

if __name__ == "__main__":
    print("\n\n\t\tStarwars, lista completa de personajes:\n\n______________________________________________________")
    try:
        for elemento in LISTA_PERSONAXES:
            print(elemento.__str__())
    except Exception as e:
        print(f"Error: {e}")
    
    # print("\n\n\t\tStarwars, lista de Droides:\n\n______________________________________________________")
    # try:
    #     for elemento in LISTA_PERSONAXES:
    #         if isinstance(elemento, Droides):
    #             print(elemento)
    # except Exception as e:
    #     print(f"Error: {e}")
    
    print("\n\n\t\tStarwars, lista personajes  no robots:\n\n______________________________________________________")
    try:
        for elemento in LISTA_PERSONAXES:
            if isinstance(elemento, Bioloxicos):
                print(elemento)  
    except Exception as e:
        print(f"Error: {e}")