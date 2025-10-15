"""
Crea: day02/number_comparator.py

Tu tarea:

Crea dos variables: a = 10 y b = 20
Imprime si son iguales o diferentes
Imprime cuál es mayor
Usa operadores: ==, !=, >, <
Ejemplo de output esperado:

Code
¿10 es igual a 20? False
¿10 es diferente de 20? True
20 es mayor que 10
"""

a: int = 10
b: int = 20

print(f"¿{a} es igual a {b}? {a == b}")  # type: ignore
print(f"¿{a} es diferente de {b}? {a != b}")  # type: ignore

if a > b:
    print(f"{a} es mayor que {b}")
elif b > a:
    print(f"{b} es mayor que {a}")
else:
    print(f"{a} y {b} son iguales")
