#Os alumnos dun curso dividíronse en dous grupos A e B de acordo ao sexo e o nome.

#    O grupo A esta formado polas mulleres cun nome anterior á M e os homes cun nome posterior á N
#    O grupo B esta formado polo resto.

#Escribir un programa que pregunte ao usuario o seu nome e sexo, e mostre por pantalla o grupo que lle corresponde.

#Ten en conta que os operadores maior que menor que tamén funcionan con cadenas de caracteres.

if __name__ == "__main__":
    
    nombre= input("Escribe tu nombre: ")
    sexo= input("Escribe tu sexo: ")

    if nombre[0].lower() <= "m" and sexo == "mujer":
        print("Grupo A")
    elif nombre[0].lower() >= "n" and sexo == "hombre":
        print("Grupo A")
    else:
        print("Grupo B")
