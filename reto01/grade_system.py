"""
🏆 RETO: Sistema de Calificaciones Escolar
📋 Descripción
Crea un programa que calcule la calificación final de un estudiante y determine si aprueba o reprueba la materia.

🎯 Requisitos
Crea el archivo: reto01/grade_system.py

Datos de entrada (variables):
Python
student_name: str = "Mauricio"
exam1: float = 85.5
exam2: float = 92.0
exam3: float = 78.0
attendance: int = 85  # Porcentaje de asistencia
Reglas de negocio:
Calcular promedio de los 3 exámenes

Determinar calificación por letra:

90-100: A (Excelente)
80-89: B (Muy bueno)
70-79: C (Bueno)
60-69: D (Regular)
0-59: F (Reprobado)
Condiciones para aprobar:

Promedio >= 60 Y Asistencia >= 80%

Bonus (+5 puntos):
Si promedio >= 90 Y asistencia >= 95%
Aplicar bonus ANTES de calcular la letra

🎯 Desafíos adicionales (opcionales):
Prueba con 3 estudiantes diferentes (cambia los valores)
Agrega validación: Si asistencia > 100 o < 0, imprime "Error: Asistencia inválida"
Si promedio < 50, imprime un mensaje de "Necesita tutoría"
"""

student_name: str = "Mauricio"
exam1: float = 85.5
exam2: float = 92.0
exam3: float = 78.0
attendance: int = 85
bonus_applied: bool = False

# Calcular promedio
average: float = (exam1 + exam2 + exam3) / 3

# Aplicar bonus ANTES de calcular letra
if average >= 90 and attendance >= 95:
    average += 5
    bonus_applied = True

# Validación de asistencia
if attendance > 100 or attendance < 0:
    print("Error: Asistencia inválida")
else:
    # Calcular letra SIEMPRE (independiente de si aprueba)
    if average >= 90:
        grade = "A (Excelente)"
    elif average >= 80:
        grade = "B (Muy bueno)"
    elif average >= 70:
        grade = "C (Bueno)"
    elif average >= 60:
        grade = "D (Regular)"
    else:
        grade = "F (Reprobado)"
    
    # Determinar estado (aprobado/reprobado)
    if average >= 60 and attendance >= 80:
        state = "APROBADO"
    else:
        state = "REPROBADO"
    
    # Output
    print("="*40)
    print("SISTEMA DE CALIFICACIONES")
    print("="*40)
    print(f"Estudiante: {student_name}")  # ✅ Faltaba esto
    print("-"*40)
    print(f"Bonus aplicado: {'Si' if bonus_applied else 'no'}")
    print(f"Examen 1: {exam1:.2f}")
    print(f"Examen 2: {exam2:.2f}")
    print(f"Examen 3: {exam3:.2f}")
    print(f"Promedio: {average:.2f}")
    print(f"Asistencia: {attendance}%")
    print(f"Calificación: {grade}")
    print(f"Estado: {state}")
    
    # Mensaje de tutoría
    if average < 50:
        print("Necesita tutoría")
    
    print("="*40)