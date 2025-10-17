"""
Crea tres funciones:

1. es_par(numero: int) -> bool
   - Retorna True si el número es par

2. es_primo(numero: int) -> bool
   - Retorna True si el número es primo
   - Tip: Un número primo solo es divisible por 1 y sí mismo

3. analizar_numero(numero: int) -> None
   - Usa las dos funciones anteriores
   - Imprime si el número es par/impar y si es primo

Prueba con: 2, 7, 10, 13, 20
"""

import math


def es_par(numero: int) -> bool:
    """
    Verifica si un número es par.

    Args:
        numero (int): Número entero a evaluar.

    Returns:
        bool: True si el número es par, False si es impar.
    """
    return numero % 2 == 0


def es_primo(numero: int) -> bool:
    """
    Determina si un número es primo.

    Un número primo es aquel que solo es divisible por 1 y por sí mismo.

    Args:
        numero (int): Número entero a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.

    Note:
        Utiliza optimizaciones matemáticas para mejorar la eficiencia:
        - Solo verifica divisores hasta la raíz cuadrada
        - Excluye números pares después del 2
        - Maneja casos especiales (0, 1, 2)

    Examples:
        >>> es_primo(7)
        True
        >>> es_primo(10)
        False
        >>> es_primo(2)
        True
    """
    if numero <= 1:
        return False  # 0 y 1 no son primos
    if numero == 2:
        return True  # 2 es el único primo par
    if numero % 2 == 0:
        return False  # otros números pares no son primos

    raiz = int(math.sqrt(numero)) + 1
    for i in range(3, raiz, 2):
        if numero % i == 0:
            return False
    return True


def analizar_numero(numero: int) -> None:
    """
    Analiza si un número es par/impar y si es primo.

    Utiliza las funciones es_par() y es_primo() para determinar
    las características del número e imprime el resultado.

    Args:
        numero (int): Número entero a analizar.

    Returns:
        None: Esta función solo imprime el resultado, no retorna valores.

    Examples:
        >>> analizar_numero(7)
        El número 7 es impar y es primo
        >>> analizar_numero(10)
        El número 10 es par y no es primo
    """
    par = es_par(numero)
    primo = es_primo(numero)

    tipo = "par" if par else "impar"
    estado_primo = "es primo" if primo else "no es primo"

    print(f"El número {numero} es {tipo} y {estado_primo}")


numeros: list[int] = [1, 2, 3, 20, 17, 29, 50, 79]

for num in numeros:
    analizar_numero(num)
