#Escribir un programa que pida ao usuario un número enteiro e mostre por pantalla se é un número primo ou non. Para iso basta que tentes dividir o número polos números menores a n/2. Se algún deles divide de xeito exacto ao número entón non é primo, noutro caso debes seguir ata o final.

#Se chegas ata o último divisor e non houbo ningún deles que dividise o número enteiro orixinal entón tes un número primo.

if __name__ == "__main__":
    primo = int(input("Escribe un número: "))
    
    # O 0 e o 1 non son primos
    if primo <= 1:
        print("Non é primo")
    else:
        divisor = int(primo / 2)
        es_primo = True  # Asumimos inicialmente que é primo
        
        # Facemos o bucle mentres o divisor sexa maior ou igual a 2
        while divisor >= 2:
            if primo % divisor == 0:
                es_primo = False  # Atopamos un divisor exacto, xa non é primo
                break  # Saímos do bucle porque xa sabemos que non é primo
            divisor = divisor - 1
            
        if es_primo:
            print("Es primo")
        else:
            print("No es primo")
        
            
        
