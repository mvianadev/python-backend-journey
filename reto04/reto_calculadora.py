"""
RETO 04: Calculadora con Funciones

Crea un programa con las siguientes funciones:

1. sumar(a: float, b: float) -> float
2. restar(a: float, b: float) -> float
3. multiplicar(a: float, b: float) -> float
4. dividir(a: float, b: float) -> float
   - Valida división por cero y retorna 0.0 con mensaje

5. potencia(base: float, exponente: int) -> float

6. mostrar_menu() -> None
   - Imprime las opciones disponibles:
     [1] Sumar
     [2] Restar
     [3] Multiplicar
     [4] Dividir
     [5] Potencia
     [0] Salir

7. ejecutar_calculadora() -> None
   - Función principal que:
     * Muestra el menú
     * Pide al usuario la operación
     * Pide los números necesarios
     * Ejecuta la operación correspondiente
     * Muestra el resultado
     * Repite hasta que el usuario elija salir

Requisitos:
- Type hints en todas las funciones
- Docstrings descriptivos
- Validación de entrada
- Formato de salida profesional

Ejemplo de flujo:
=== CALCULADORA ===
[1] Sumar
[2] Restar
...
Elige operación: 1
Primer número: 15
Segundo número: 7
Resultado: 15 + 7 = 22

¿Otra operación? [s/n]: n
¡Gracias por usar la calculadora!
"""

from typing import Callable, Optional


def sumar(a: float, b: float) -> float:
    """
    Realiza una suma.

    Args:
        a (float):
        b (float):
            recibe dos parametros para realizar la suma.

    Returns:
        float: devuelve la suma entre a y b
    """
    return a + b


def restar(a: float, b: float) -> float:
    """
    Realiza una resta.

    Args:
        a (float):
        b (float):
            recibe dos parametros para realizar la resta.

    Returns:
        float: devuelve la resta entre a y b
    """
    return a - b


def multiplicar(a: float, b: float) -> float:
    """
    Realiza una resta.

    Args:
        a (float):
        b (float):
            recibe dos parametros para realizar la multiplicación.

    Returns:
        float: devuelve la multiplicación entre a y b
    """
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Realiza una division.

    Args:
        a (float):
        b (float):
            recibe dos parametros para realizar la division.

    Returns:
        float: devuelve la division entre a y b

    Note:
        Se revisa si el segundo parametro (b) es cero
        en ese caso se devuelve 0.0
    """
    if b == 0:
        return 0.0
    return a / b


def potencia(base: float, exponente: float) -> float:
    """
    Realiza una potenciación.

    Args:
        a (float):
        b (float):
            recibe dos parametros para realizar la potencia entre a**b.

    Returns:
        float: devuelve la potenciación de a**b
    """
    return base ** int(exponente)


def mostrar_menu() -> None:
    """Imprime el menú principal de la calculadora en consola."""
    print(
        "[1] Sumar\n[2] Restar\n[3] Multiplicar\n[4] Dividir\n[5] Potencia\n[0] Salir"
    )


operaciones: dict[int, Callable[[float, float], float]] = {
    1: sumar,
    2: restar,
    3: multiplicar,
    4: dividir,
    5: potencia,
}

simbolos: dict[int, str] = {
    1: "+",
    2: "-",
    3: "*",
    4: "/",
    5: "**",
}


def ejecutar_calculadora() -> None:
    """
    Ejecuta el flujo principal de la calculadora interactiva.

    Muestra un menú de operaciones matemáticas disponibles, solicita al usuario
    que seleccione una opción y que ingrese los números necesarios. Luego ejecuta
    la operación correspondiente y muestra el resultado en formato profesional.

    El programa se repite hasta que el usuario elige salir.

    Operaciones disponibles:
        [1] Sumar
        [2] Restar
        [3] Multiplicar
        [4] Dividir (retorna 0.0 si el divisor es cero)
        [5] Potencia (el exponente se interpreta como entero)
        [0] Salir

    Requiere:
        - Validación de entradas numéricas.
        - Manejo de errores por entradas inválidas.
        - Diccionario de funciones y símbolos definidos previamente.

    Returns:
        None
    """
    while True:
        mostrar_menu()
        try:
            operacion = int(input("Elige operación: "))
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")
            continue

        if operacion == 0:
            print("¡Gracias por usar la calculadora!")
            break

        funcion: Optional[Callable[[float, float], float]] = operaciones.get(operacion)
        simbolo = simbolos.get(operacion, "?")

        if funcion is None:
            print("Opción inválida.")
            continue

        try:
            numero_uno = float(input("Primer número: "))
            numero_dos = float(input("Segundo número: "))
            resultado = funcion(numero_uno, numero_dos)
            simbolo = simbolos.get(operacion, "?")
            print(
                f"\nResultado: {numero_uno} {simbolo} {numero_dos} = {resultado:.2f}\n"
            )
        except ValueError:
            print("Entrada inválida. Debe ser un número decimal.")

        continuar = input("¿Otra operación? [s/n]: ").strip().lower()
        if continuar in ("s", "n"):
            break
        print("Entrada inválida. Por favor ingrese 's' para sí o 'n' para no.")

        if continuar != "s":
            print("¡Gracias por usar la calculadora!")
            break


ejecutar_calculadora()
