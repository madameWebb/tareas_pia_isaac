# Escribir un programa que pregunte ao usuario polo número de horas traballadas e o custo por hora. Despois debe mostrar por pantalla a paga que lle corresponde.

if __name__ == "__main__":
    horas = input("Ecribe el número de horas trabajadas: ")
    coste = input("Escribe el coste por hora trabajada: ")
    paga = float(horas) * float(coste)
    print("Debes cobrar: ", paga)