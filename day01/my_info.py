"""
Crea: day01/my_info.py

Tu tarea: Crea un programa que imprima TU información personal:

Nombre
Edad
País
Años de experiencia en QA
Objetivo de salario (en USD)
Si estás aprendiendo Python (True/False)
"""

name: str = "Mauricio"
age: int = 30
country: str = "Argentina"
years_experiance_qa: int = 2
salary: float = 2000
learning_python: bool = True

print("="*30)
print(f"Nombre: {name}")
print(f"Edad: {age}")
print(f"Pais: {country}")
print(f"Salario pretendido: {salary}")
print(f"Aprendiendo python: {learning_python}")
print("="*30)