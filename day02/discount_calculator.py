"""
Crea: day02/discount_calculator.py

Escenario: Una tienda aplica descuentos según la edad del cliente.

Reglas de negocio:

Menores de 18 años: 20% de descuento
Entre 18 y 65 años: Sin descuento (0%)
Mayores de 65 años: 30% de descuento
Tu tarea:

Crea estas variables:
Python
price: float = 100.0
age: int = 70  # Cambia este valor para probar
Calcula el descuento según la edad (usa if/elif/else)
Calcula el precio final
Imprime un output como este:
Code
==============================
CALCULADORA DE DESCUENTOS
==============================
Precio original: $100.00
Edad del cliente: 70
Descuento aplicado: 30%
Precio final: $70.00
==============================
"""

price: float = 100.0
age: int = 70  # Cambiar este valor para probar
final_price: float = 0
discount: float = 0

if age < 18:
    discount = 0.20
elif age >= 18 and age < 65:
    discount = 0
elif age > 65:
    discount = 0.30

final_price = price * (1 - discount)

print("="*30)
print("CALCULADORA DE DESCUENTOS")
print("="*30)
print(f"Precio original: {price:.2f}$")
print(f"Edad del cliente: {age}")
print(f"Descuento aplicado: {discount * 100:.0f}%")
print(f"Precio final: {final_price:.2f}$")
print("="*30)