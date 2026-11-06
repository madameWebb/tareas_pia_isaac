#Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua) nunha lista e a mostre por pantalla coa mensaxe Eu estudo <materia>, onde <materia> é cada unha das materias da lista.



if __name__ == "__main__":

    lista = ["matemáticas", "lengua", "física", "química", "inglés"]
    cadena = ""

    for elemento in lista:
        cadena += elemento + ", "

    print("Yo estudio", cadena)
            
        
