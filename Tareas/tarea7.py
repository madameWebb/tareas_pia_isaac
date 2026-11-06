#Escribir un programa que pregunte o nome completo do usuario na consola e despois mostre por pantalla o nome completo do usuario tres veces: 
# - unha con todas as letras minúsculas 
# - outra con todas as letras maiúsculas 
# - outra só coa primeira letra do nome e dos apelidos en maiúscula. 
# O usuario pode introducir o seu nome combinando maiúsculas e minúsculas como queira.

if __name__ == "__main__":
    nombre = input("Introduce tu nombre y apellidos: ")
    lista = nombre.split()
    #print(lista)

    print(nombre.lower())
    print(nombre.upper())
    print(nombre.title())

    for indice, valor in enumerate(lista):
        lista[indice] = lista[indice].capitalize()

    print(" ".join(lista))