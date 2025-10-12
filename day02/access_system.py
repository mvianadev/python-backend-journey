"""
✅ Ejercicio 4: Sistema de acceso (15 min)
Crea: day02/access_system.py

Escenario: Sistema que verifica si un usuario puede acceder.

Tu tarea:

Crea estas variables:
Python
age: int = 25
has_id: bool = True
is_banned: bool = False
El usuario puede acceder SI:
Es mayor de 18 Y
Tiene ID Y
NO está baneado
Imprime "Acceso permitido" o "Acceso denegado"
Usa operadores lógicos: and, not
Prueba cambiando los valores para verificar todos los casos.
"""

age: int = 24
has_id: bool = True
is_banned: bool = False

if age > 18 and has_id and not is_banned:
    print("Acceso permitido")
else:
    print("Acceso denegado")