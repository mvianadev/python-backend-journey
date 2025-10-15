"""
✅ Ejercicio 3: Tabla de multiplicar
Crea: day03/multiplication_table.py

Pide un número al usuario (input())
Imprime su tabla de multiplicar del 1 al 10 usando for.
Pista: Convierte el input a int: n = int(input("Dame un número: "))
"""

n: int = int(input("Dame un numero: "))


for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
