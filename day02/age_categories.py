"""
✅ Ejercicio 2: Categorías de edad (10 min)
Crea: day02/age_categories.py

Tu tarea:

Crea una variable age con cualquier valor
Usa if/elif/else para imprimir:
Si age < 13: "Niño"
Si age < 18: "Adolescente"
Si age < 65: "Adulto"
Si no: "Adulto mayor"
"""

age: int = 36

if age < 13:
    print("Eres un niño")
elif age < 18:
    print("Eres un adolescente")
elif age < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")