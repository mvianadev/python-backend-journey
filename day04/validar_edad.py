"""
Crea una función puede_votar(edad: int) -> bool que:
- Retorne True si edad >= 18
- Retorne False si edad < 18

Crea otra función validar_entrada_cine(edad: int) -> str que:
- Si edad < 0: retorna "Edad inválida"
- Si edad < 13: retorna "Entrada: Niño - $5"
- Si edad < 18: retorna "Entrada: Adolescente - $8"
- Si edad >= 65: retorna "Entrada: Adulto Mayor - $6"
- Si no: retorna "Entrada: Adulto - $10"

Prueba con edades: -5, 10, 15, 25, 70
"""


def puede_votar(edad: int) -> bool:
    """
    Verifica si una persona puede votar.

    Args:
        edad (int): edad de la persona que va a votar.
    Returns:
        bool: retorna True si es mayor de 18 o retorna False si es menor de 18
    """
    return edad >= 18


def validar_entrada_cine(edad: int) -> str:
    """
    Verifica el valor de una entrada.

    Args:
        edad (int): edad de la persona que va al cine.
    Returns:
        str: retorna valores de precio de entrada para el cine [5, 8, 6, 10] o Edad inválida
    """
    if edad < 0:
        return "Edad invalida"
    elif edad < 13:
        return "Entrada: Niño - $5"
    elif edad < 18:
        return "Entrada: Adolescente - $8"
    elif edad >= 65:
        return "Entrada: Adulto Mayor - $6"

    return "Entrada: Adulto - $10"


lista_edad: list[int] = [-5, 10, 15, 25, 70]

print("=" * 30)
print("Validar edad para votar: ")
print("=" * 30)

for x in lista_edad:
    print(f"{x} puede votar: {puede_votar(x)}")

print("=" * 30)
print("Costo de entrada para el cine: ")
print("=" * 30)

for y in lista_edad:
    if y > 0:
        print(f"{validar_entrada_cine(y)}, edad: {y}")
    else:
        print(validar_entrada_cine(y))
