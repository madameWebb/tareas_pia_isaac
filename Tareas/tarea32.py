#Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua) nunha lista, pregunte ao usuario a nota que sacou en cada materia, e despois as amose por pantalla coa mensaxe En sacaches un onde é cada unha das materias da lista e cada unha das correspondentes notas introducidas polo usuario.


if __name__ == "__main__":

    lista = ["matemáticas", "lengua", "física", "química", "inglés"]
    diccionario = {}
    nota = 0

    for elemento in lista:
        nota = float(input("Que nota sacaste en " + elemento + "? "))
        diccionario[elemento] = nota

    for indice, valor in diccionario.items():
        print("sacaste un ", valor, " en ", indice)
            
        
