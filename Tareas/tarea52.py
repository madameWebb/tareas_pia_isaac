# Calcula a distancia de Hamming entre dúas cadeas de ADN. Neste caso, a clase coa que tes que traballar a que representa á cadea de ADN.

# O teu corpo está formado por células que conteñen ADN. Esas células desgastanse regularmente e necesitan ser substituídas, o que conseguen dividíndose en células fillas. De feito, o corpo humano medio experimenta uns 10 trillóns de divisións celulares ao longo da vida.

# Cando as células se dividen, o seu ADN tamén se replica. Ás veces durante este proceso ocorren erros e as pezas de ADN son codificadas coa información incorrecta. Se comparamos dúas cadeas de ADN e contamos as diferenzas entre elas podemos ver cantos erros se produciron. Isto é coñecido como a “distancia de Hamming”.

# Lemos o ADN usando as letras C,A,G e T. Dúas cadeas poden verse así:

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# ^ ^ ^ ^ ^ ^ ^^

# Teñen 7 diferenzas, polo que a Distancia de Hamming é 7.

# A distancia de Hamming é útil para moitas cousas da ciencia, por exemplo informática, polo que non está de máis coñecela.
# Notas de implantación

# A distancia de Hamming só se define para secuencias de igual lonxitude, polo que un intento de calculala entre secuencias de diferentes lonxitudes non debería funcionar.
# Ampliación:

# Serías capaz de implemenar que a distancia Hamming entre dúas cadeas de ADN sexa o que se obteña cando se produce a resta entre dúas cadeas? (metodo sub)

class ADN:
    def __init__(self, cadena: str):
        self.cadena_adn = cadena
        
    @property
    def cadena_adn(self) -> str:
        return self._cadena_adn

    @cadena_adn.setter
    def cadena_adn(self, cadena: str) -> None:
        cadena = cadena.upper()
        validas = set("CAGT")
        if all(letra in validas for letra in cadena):
            self._cadena_adn = cadena
        else:
            raise ValueError("La cadena contiene letras no válidas")

    def comparar_cadenas(self, cadena: ADN)->int:
        secuencia_1 = self.cadena_adn
        secuencia_2 = cadena.cadena_adn
        hamming = 0
        if len(secuencia_1) == len(secuencia_2):
            comparacion = zip(secuencia_1, secuencia_2)
            for letra_1, letra_2 in comparacion:
                if letra_1 != letra_2:
                    hamming +=1
        else:
            raise ValueError("las cadenas no miden lo mismo")
        return hamming

    def __sub__(self, cadena: ADN)->int:
            secuencia_1 = self.cadena_adn
            secuencia_2 = cadena.cadena_adn
            hamming = 0
            if len(secuencia_1) == len(secuencia_2):
                comparacion = zip(secuencia_1, secuencia_2)
                for letra_1, letra_2 in comparacion:
                    if letra_1 != letra_2:
                        hamming +=1
            else:
                raise ValueError("las cadenas no miden lo mismo")
            return hamming


if __name__ == "__main__":
    adn1 = "abcdefghaijk"
    adn2 = "gasdfdkjlaej"

    adn3 = "cagtgtaccaa"
    adn4 = "acgtgatccag"

    lista = [adn1, adn2, adn3, adn4]
    adn_valido:list[ADN] = []
    
    for elemento in lista:
        try: 
            adn=ADN(elemento)
            adn_valido.append(adn)
        except ValueError as e:
            print(f"Excepción capturada en {elemento}: {e}")

    if len(adn_valido) >= 2:
        try:
            for i in range(len(adn_valido) - 1):
                hamming = adn_valido[i].comparar_cadenas(adn_valido[i+1])
                print(hamming)
        except ValueError as e:
                    print(f"Excepción capturada en {adn_valido[i]} y {adn_valido[i+1]}: {e}") 
        try:
            for i in range(len(adn_valido) - 1):
                hamming = adn_valido[i] - adn_valido[i+1]
                print(hamming)
        except ValueError as e:
                    print(f"Excepción capturada en {adn_valido[i]} y {adn_valido[i+1]}: {e}")        
                