"""
🚀 BONUS: Listas y break/continue
Crea: day03/list_break_continue.py

Dada una lista de números, imprime solo los positivos, omitiendo (con continue)
los negativos y deteniendo el bucle (con break) si encuentra un 0.
"""

lista_numero: list[int] = [1, -2, 5, -10, 2, 5, 7, 8, 0, 20]

for i in lista_numero:
    if i > 0:
        print(i)
    elif i == 0:
        break
    else:
        continue
