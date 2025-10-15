"""
📋 Enunciado
Escribe un programa que:

Pida al usuario 5 números enteros (usa un bucle).
Guarde esos números en una lista.
Imprima:
La lista completa
La suma de todos los números
El promedio
El número más grande y el más pequeño
Cuántos son pares y cuántos impares
Si hay algún número igual a cero, imprime "¡Cuidado, hay un cero!"
"""

lista_de_numeros: list[int] = []
total: int = 0
par: int = 0
inpar: int = 0

for i in range(5):
    lista_de_numeros.append(int(input("Ingresa un numero: ")))

num_peq = lista_de_numeros[0]
num_gran = lista_de_numeros[0]

for num in lista_de_numeros:
    total += num
    if num < num_peq:
        num_peq = num
    if num > num_gran:
        num_gran = num

    if num % 2 == 0:
        par += 1
    else:
        inpar += 1

    if num == 0:
        print("¡Cuidado, hay un cero!")

# Calcular promedio
promedio: float = total / len(lista_de_numeros)

# Mostrar resultados
print("\n📋 Resultados:")
print("Lista completa:", lista_de_numeros)
print("Suma total:", total)
print("Promedio:", promedio)
print("Número más pequeño:", num_peq)
print("Número más grande:", num_gran)
print("Cantidad de pares:", par)
print("Cantidad de impares:", inpar)
