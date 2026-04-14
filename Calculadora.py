#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║        CALCULADORA INTERACTIVA           ║
║  Suma · Resta · Multiplicación · División║
║  Logaritmos · Potencias · Raíces         ║
╚══════════════════════════════════════════╝
"""

import math
import os


# ── Utilidades ──────────────────────────────────────────────────────────────

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def fmt(valor):
    """Formatea un número: entero si no tiene decimales, float si los tiene."""
    if isinstance(valor, complex):
        return str(valor)
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.10g}"


def pedir_numero(mensaje="  Ingresa un número: "):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠  Entrada inválida. Escribe un número.\n")


def pedir_base_log():
    while True:
        base = pedir_numero("  Base del logaritmo: ")
        if base <= 0 or base == 1:
            print("  ⚠  La base debe ser > 0 y distinta de 1.\n")
        else:
            return base


# ── Banner y menús ───────────────────────────────────────────────────────────

BANNER = """
╔══════════════════════════════════════════╗
║        CALCULADORA INTERACTIVA           ║
╚══════════════════════════════════════════╝"""

MENU_PRINCIPAL = """
  ┌─────────────────────────────────────┐
  │  OPERACIONES DISPONIBLES            │
  ├─────────────────────────────────────┤
  │  [1]  Suma             a + b        │
  │  [2]  Resta            a - b        │
  │  [3]  Multiplicación   a × b        │
  │  [4]  División         a ÷ b        │
  │  [5]  Potencia         a ^ b        │
  │  [6]  Raíz cuadrada    √a           │
  │  [7]  Raíz n-ésima     ⁿ√a          │
  │  [8]  Logaritmo base b log_b(a)     │
  │  [9]  Logaritmo base 10 log(a)      │
  │  [10] Logaritmo natural  ln(a)      │
  │  [11] Historial                     │
  │  [0]  Salir                         │
  └─────────────────────────────────────┘
"""


# ── Operaciones ──────────────────────────────────────────────────────────────

def op_suma():
    a = pedir_numero("  a = ")
    b = pedir_numero("  b = ")
    resultado = a + b
    expresion = f"{fmt(a)} + {fmt(b)}"
    return resultado, expresion


def op_resta():
    a = pedir_numero("  a = ")
    b = pedir_numero("  b = ")
    resultado = a - b
    expresion = f"{fmt(a)} - {fmt(b)}"
    return resultado, expresion


def op_multiplicacion():
    a = pedir_numero("  a = ")
    b = pedir_numero("  b = ")
    resultado = a * b
    expresion = f"{fmt(a)} × {fmt(b)}"
    return resultado, expresion


def op_division():
    a = pedir_numero("  a = ")
    while True:
        b = pedir_numero("  b = ")
        if b != 0:
            break
        print("  ⚠  No se puede dividir entre cero.\n")
    resultado = a / b
    expresion = f"{fmt(a)} ÷ {fmt(b)}"
    return resultado, expresion


def op_potencia():
    a = pedir_numero("  base a = ")
    b = pedir_numero("  exponente b = ")
    resultado = a ** b
    expresion = f"{fmt(a)} ^ {fmt(b)}"
    return resultado, expresion


def op_raiz_cuadrada():
    while True:
        a = pedir_numero("  a = ")
        if a >= 0:
            break
        print("  ⚠  La raíz cuadrada de un número negativo no es real.\n")
    resultado = math.sqrt(a)
    expresion = f"√{fmt(a)}"
    return resultado, expresion


def op_raiz_nesima():
    while True:
        a = pedir_numero("  radicando a = ")
        n = pedir_numero("  índice n = ")
        if n == 0:
            print("  ⚠  El índice no puede ser 0.\n")
            continue
        if a < 0 and n % 2 == 0:
            print("  ⚠  Raíz de índice par de número negativo no es real.\n")
            continue
        break
    signo = -1 if a < 0 else 1
    resultado = signo * (abs(a) ** (1 / n))
    expresion = f"{fmt(n)}√{fmt(a)}"
    return resultado, expresion


def op_log_base_b():
    while True:
        a = pedir_numero("  argumento a = ")
        if a > 0:
            break
        print("  ⚠  El argumento del logaritmo debe ser > 0.\n")
    base = pedir_base_log()
    resultado = math.log(a, base)
    expresion = f"log_{fmt(base)}({fmt(a)})"
    return resultado, expresion


def op_log10():
    while True:
        a = pedir_numero("  a = ")
        if a > 0:
            break
        print("  ⚠  El argumento debe ser > 0.\n")
    resultado = math.log10(a)
    expresion = f"log₁₀({fmt(a)})"
    return resultado, expresion


def op_ln():
    while True:
        a = pedir_numero("  a = ")
        if a > 0:
            break
        print("  ⚠  El argumento debe ser > 0.\n")
    resultado = math.log(a)
    expresion = f"ln({fmt(a)})"
    return resultado, expresion


# ── Historial ────────────────────────────────────────────────────────────────

def mostrar_historial(historial):
    print("\n  ┌─────────────────────────────────────┐")
    print("  │  HISTORIAL DE OPERACIONES           │")
    print("  ├─────────────────────────────────────┤")
    if not historial:
        print("  │  (vacío)                            │")
    else:
        for i, (expr, res) in enumerate(historial, 1):
            linea = f"  {i:>2}. {expr} = {fmt(res)}"
            print(linea[:45])
    print("  └─────────────────────────────────────┘\n")


# ── Bucle principal ──────────────────────────────────────────────────────────

def ejecutar_operacion(opcion):
    operaciones = {
        "1": op_suma,
        "2": op_resta,
        "3": op_multiplicacion,
        "4": op_division,
        "5": op_potencia,
        "6": op_raiz_cuadrada,
        "7": op_raiz_nesima,
        "8": op_log_base_b,
        "9": op_log10,
        "10": op_ln,
    }
    return operaciones[opcion]()


def main():
    historial = []

    while True:
        limpiar_pantalla()
        print(BANNER)
        print(MENU_PRINCIPAL)

        opcion = input("  Elige una opción: ").strip()

        if opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break

        if opcion == "11":
            limpiar_pantalla()
            print(BANNER)
            mostrar_historial(historial)
            input("  Pulsa Enter para continuar...")
            continue

        if opcion not in [str(i) for i in range(1, 11)]:
            input("  ⚠  Opción no válida. Pulsa Enter para continuar...")
            continue

        limpiar_pantalla()
        print(BANNER)
        print()

        nombres = {
            "1": "SUMA", "2": "RESTA", "3": "MULTIPLICACIÓN", "4": "DIVISIÓN",
            "5": "POTENCIA", "6": "RAÍZ CUADRADA", "7": "RAÍZ N-ÉSIMA",
            "8": "LOGARITMO BASE b", "9": "LOGARITMO BASE 10", "10": "LOGARITMO NATURAL",
        }
        print(f"  ── {nombres[opcion]} ──\n")

        try:
            resultado, expresion = ejecutar_operacion(opcion)
            historial.append((expresion, resultado))
            print(f"\n  ✓  {expresion} = {fmt(resultado)}\n")
        except Exception as e:
            print(f"\n  ✗  Error: {e}\n")

        input("  Pulsa Enter para continuar...")


if __name__ == "__main__":
    main()
