"""
Crea una función obtener_estadisticas(numeros: list[int]) -> tuple[int, int, float]:
que retorne:
1. El valor máximo
2. El valor mínimo
3. El promedio

Validación:
- Si la lista está vacía, retorna (0, 0, 0.0)

Prueba con: [15, 42, 8, 23, 50, 31]
Imprime: "Max: X, Min: Y, Promedio: Z"
"""


def obtener_estadisticas(numeros: list[int]) -> tuple[int, int, float]:
    """
    Calcula estadísticas básicas de una lista de números enteros.

    Args:
        numeros (list[int]): Lista de números enteros para analizar.

    Returns:
        tuple[int, int, float]: Tupla con (máximo, mínimo, promedio).
            - int: Valor máximo de la lista
            - int: Valor mínimo de la lista
            - float: Promedio aritmético de los valores

    Note:
        Si la lista está vacía, retorna (0, 0, 0.0).
    """
    if len(numeros) == 0:
        return 0, 0, 0.0
    return max(numeros), min(numeros), sum(numeros) / len(numeros)


lista_numeros: list[int] = [15, 42, 8, 23, 50, 31]
maximo, minimo, promedio = obtener_estadisticas(lista_numeros)

print(obtener_estadisticas([]))
print(f"Max: {maximo}, Min: {minimo}, Promedio: {promedio:.2f}")
