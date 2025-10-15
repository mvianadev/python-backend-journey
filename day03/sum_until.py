"""
✅ Ejercicio 6: Suma hasta número (while)
Crea: day03/sum_until.py

Pide un número al usuario.
Suma todos los números desde 1 hasta ese número (inclusive) usando while.
Muestra el resultado.
"""

number: int = int(input("Ingresa un número: "))
i: int = 0
total: int = 0

while i < number:
    i += 1
    total += i


print(f"La suma de 1 hasta {number} es: {total}")
