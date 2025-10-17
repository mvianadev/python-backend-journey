"""
Crea una función llamada presentarse() que:
- No reciba parámetros
- Imprima tu nombre, edad y objetivo profesional
- Usa f-strings
- Llámala 2 veces

Objetivo: Entender la estructura básica de una función
"""


def presentarse() -> None:
    """Funcion que sirve para presentarse"""
    nombre: str = "Mauricio"
    edad: int = 30
    objetivo: str = "Backend Developer con Python"

    print(f"Hola, me llamo {nombre}")
    print(f"Tengo {edad} años")
    print(f"Mi objetivo es ser {objetivo}")


presentarse()

presentarse()
