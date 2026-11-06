#Os teléfonos dunha empresa teñen o seguinte formato prefixo-número-extension onde o prefixo é o código do país +34 (3 caracteres), e a extensión ten dous díxitos (por exemplo +34-913724710-56).

#Escribir un programa que pregunte por un número de teléfono con este formato e mostre por pantalla o número de teléfono sen o prefixo e a extensión.

#Usa slices


if __name__ == "__main__":
    
    import re
    
    tlf = input("Introduce el número de teléfono y la extensión, con el prefijo del pais delante y separado por -: ")

    def validar_tlfn(tlf):
        patron = r'^\+\d+-\d{9}-\d{3}$'
        return bool(re.match(patron, tlf))

    while validar_tlfn(tlf) is False:
    
        tlf = input("Formato incorrecto, inténtalo de nuevo: ")
    
    tlfno = tlf.split("-")

    print(tlfno[slice(1,2)])
    
