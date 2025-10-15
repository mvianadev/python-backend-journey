"""
✅ Ejercicio 2: Suma de una lista
Crea: day03/sum_list.py

Dada una lista de números, suma todos los elementos y muestra el resultado usando un bucle for.
Ejemplo: [5, 7, 2, 9] → Salida: 23
"""

lista: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total: int = 0

for num in lista:
    total += num

print(f"{lista} -> suma total: {total}")
