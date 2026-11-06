#Escribir un programa que almacene a cadea de caracteres contrasinal nunha variable, pregunte ao usuario polo contrasinal ata que introduza o contrasinal correcto.

#Parecido a un dos anteriores, pero neste caso se trata de conseguir mediante un bucle a repetición ata acertar co contrasinal

if __name__ == "__main__":

    contrasinal ="Iivg123!"
    
    autenticar = input("Escribe la contraseña: ")
    
    while autenticar != contrasinal:
        autenticar = input("Contraseña incorrecta, vuelve a introducirla: ")
            
        
