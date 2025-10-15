"""
Ejercicio 5: FizzBuzz (DESAFÍO)
Crea: day03/fizzbuzz.py

Imprime los números del 1 al 30.
Para múltiplos de 3 imprime “Fizz”, para múltiplos de 5 imprime “Buzz”,
 para múltiplos de ambos imprime “FizzBuzz”.
Si no es múltiplo de ninguno, imprime el número.
"""

for i in range(1, 30 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
