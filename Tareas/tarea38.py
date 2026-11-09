#Escribir un programa que pregunte ao usuario o seu nome, idade, dirección e teléfono e o garde todos os datosnun dicionario.

#Posteriormente debe amosar por pantalla a mensaxe: <nome> ten x anos, vive en <dir> e o seu número de teléfono é <num>.



def agregar_datos(lista_datos : list[str]) -> tuple[dict[str, str]]:
    diccionario_datos = {}
    for elemento in lista_datos:
        dato = input(f"Escribe la nota que sacaste en {elemento}: ")
        diccionario_datos[elemento] = dato
                
    return diccionario_datos

if __name__ == "__main__":
    datos_user = agregar_datos(["nombre", "edad", "dirección", "teléfono"])

    
            
    print(f"{datos_user["nombre"]} tiene {datos_user["edad"]} años, vive en {datos_user["dirección"]}, su número de telefono es {datos_user["teléfono"]}")