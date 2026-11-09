#Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua) nunha lista, pregunte ao usuario a nota que sacou en cada materia e elimine da lista as materias aprobadas.

#Ao final o programa debe amosar por pantalla as materias que o usuario ten que repetir.

#Neste programa trátase de eliminar, é dicir, primeiro se mete todo e logo eliminamos… dalgun xeito
    
def agregar_notas(lista_materias : list[str]) -> tuple[dict[str, float], dict[str, float]]:
    diccionario_notas = {}
    diccionario_repetir = {}
    for elemento in lista_materias:
        nota = float(input(f"Escribe la nota que sacaste en {elemento}: "))
        diccionario_notas[elemento] = nota
        if nota < 5:
            diccionario_repetir[elemento] =nota
        
    return diccionario_notas, diccionario_repetir

if __name__ == "__main__":
    notas, repetidas = agregar_notas(["Matemáticas", "Física", "Química", "Historia", "Lingua"])
    repite = "ninguna"

    #if len(repetidas) == 0:
    if not repetidas:
        repite
    else:
        aux =[]
                    
        for clave, valor in repetidas.items():
            tupla = (clave, str(valor))
            aux.append(" : ".join(tupla))
            
        repite = ",".join(aux)
            
    print(f"Tienes que repetir: {repite}")
    