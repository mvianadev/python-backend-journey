"""
Crea una función calcular_area_rectangulo() que:
- Reciba base y altura como parámetros (float)
- Retorne el área (base * altura)
- Agrega type hints
- Incluye un docstring

Luego:
- Calcula el área de un rectángulo de 5.5 x 3.2
- Imprime el resultado formateado a 2 decimales
"""


def calcular_area_rectangulo(b: float, a: float) -> float:
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): Base del rectángulo
        altura (float): Altura del rectángulo

    Returns:
        float: Área del rectángulo (base * altura)
    """
    return b * a


altura: float = 5.5
base: float = 3.2
area: float = calcular_area_rectangulo(altura, base)
print(f"El área de un rectángulo de base {base} y altura {altura} es: {area:.2f} m2")
