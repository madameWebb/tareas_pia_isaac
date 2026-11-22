# Tarefa 58. Información dunha persoa

# Crea unha función chamada crear_persoa() que reciba os seguintes datos dunha persoa:

#     Nome.
#     Idade.
#     Altura en metros.
#     Se ten carné de conducir ou non.

# A función debe devolver unha cadea de texto coa información da persoa.

# Requisitos:

#     Engade type hints a todos os parámetros, para iso terás que identificar primeiro que tipo de dato sería o mellor para cada un deles.
#     Indica o tipo do valor que devolve a función.
#     Verifica o código, podes probar varios.
#     Executa a función e mostra o resultado.

# Nota:

# Nesta e na seguintes tarefas é interesante probar a introducir voluntariamente erros para ver como se comportan os verificadores, as mensaxes de erro e indicacións que proporcionan para logo sexa máis sinxelo todo con códigos fonte máis amplos.

def crear_persoa(nombre: str, edad: int, altura: float, carnet_conducir: bool) -> str:
    return f"Nombre: {nombre} | Edad: {edad} años | Altura: {altura} m | Carnet de conducir: {carnet_conducir}"

if __name__ == "__main__":
    personas: list[str] = [
        crear_persoa("Juana", 60, 1.50, True),
        crear_persoa("Abel", 27, 1.80, True),
        crear_persoa("Rodrigo", 13, 1.60, False),
        crear_persoa("Lina", 3, 1, False)
    ]

    # Prueba con errores voluntarios de tipo:
    error_tipo = crear_persoa(1234, "veinte", "muy alta", "sí")

    for persona in personas:
        print(persona)

    print(error_tipo)
