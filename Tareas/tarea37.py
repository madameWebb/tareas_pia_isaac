# Escribir un programa que garde nunha variable o dicionario:

# {'Euro':'€', ' Dollar':'$', ' Yen':'¥'}

# Logo hai que preguntar ao usuario por unha divisa e mostre o seu símbolo ou unha mensaxe de aviso de que non traballamos con esa divisa
if __name__ == "__main__":
    divisas = {
        "Euro":"€",
        "Dolar": "$",
        "Yen": "¥"
    }

    divisa = input("Pide tu divisa: ").capitalize()

    if divisa in divisas:

        print(divisas[divisa])

    else:
        print("No trabajamos con esa divisa")