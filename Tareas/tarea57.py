# Tarefa 57. Decorador para comprobar os permisos dun usuario

# Queremos desenvolver un pequeno sistema de control de acceso utilizando decoradores.

# Crea un decorador chamado comprobar_permisos que comprobe se un usuario ten permisos para executar unha determinada función.

# O decorador debe cumprir os seguintes requisitos:

#     Debe recibir como parámetro o rol necesario para executar a función.
#     A función decorada recibirá como primeiro argumento o nome dun usuario.
#     Se o rol do usuario coincide co rol requirido, executarase a función.
#     Se o usuario non ten os permisos necesarios, lanzarase unha excepción (ErrorPermisos).
#     Se o usuario ten permisos, a función devolverá o resultado correspondente.

# Para realizar o exercicio, considera os seguintes usuarios:
# Usuario 	Rol
# Ana 	administrador
# Pedro 	usuario
# María 	administrador
# Xoán 	usuario

# Crea unha función chamada eliminar_datos que só poida ser executada por usuarios co rol de administrador. A función non fará en realidade nada, con que imprima un “por aquí pasei” chega.

# Lembra facer os test.

from functools import wraps
from typing import Callable


def comprobar_permisos(rol: str) -> Callable:
    """Decorador que comprueba si el usuario tiene el rol requerido."""
    def decorador(func: Callable) -> Callable:
        @wraps(func)
        def envoltura(usuario: str, *args, **kwargs):
            rol_usuario = USUARIOS.get(usuario)
            if rol_usuario != rol:
                raise ErrorPermisos(f"El usuario '{usuario}' no tiene permisos de '{rol}'.")
            return func(usuario, *args, **kwargs)
        return envoltura
    return decorador

USUARIOS: dict[str, str] = {"Ana": "administrador",
                                "Pedro": "usuario",
                                "María": "administrador",
                                "Xoán": "usuario"
                                }

@comprobar_permisos("administrador")
def eliminar_datos(nombre: str) -> None:
    print("Pasé por aquí")

class ErrorPermisos(Exception):
    pass

if __name__ == "__main__":
  
    for nombre in USUARIOS: #Es lo mismo que usar USUARIOS.keys()
        try:
            eliminar_datos(nombre)
        except ErrorPermisos as e:
            print(f"Acceso denegado: {e}")