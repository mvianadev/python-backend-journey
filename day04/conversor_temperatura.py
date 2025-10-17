"""
Crea dos funciones:

1. celsius_a_fahrenheit(celsius: float) -> float
   - Fórmula: (celsius * 9/5) + 32

2. fahrenheit_a_celsius(fahrenheit: float) -> float
   - Fórmula: (fahrenheit - 32) * 5/9

Luego:
- Convierte 25°C a Fahrenheit
- Convierte 77°F a Celsius
- Imprime ambos resultados con formato
"""


def celsius_a_fahrenheit(celsius: float) -> float:
    """
        Convierte de celsius a fahrenheit.

    Args:
        celsius (float): temperatura en celsius

    Returns:
        float: Retorna fahrenheit, en float.
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """
        Convierte de fahrenheit a celsius.

    Args:
        fahrenheit (float): temperatura en farhenheit

    Returns:
        float: Retorna celcius, en float.
    """
    return (fahrenheit - 32) * 5 / 9


grados_celcius: float = 25
grados_fahrenheit: float = 77

resultado_celsius: float = fahrenheit_a_celsius(grados_fahrenheit)
resultado_fahrenheit: float = celsius_a_fahrenheit(grados_celcius)

print(f"{grados_celcius}°c a fahrenheit: {resultado_fahrenheit}°f")

print(f"{grados_fahrenheit}°f a cesius: {resultado_celsius}°c")
