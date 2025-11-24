# - Muestra dos opciones al inicio.
# - Opción 1 (60%): usa while, lista, trigonometría y cálculos.
# - Opción 2 (40%): submenú con tres funciones.
# - Funciona correctamente en cualquier lugar hastra en el CMD por el encapsulado del Menu
# Grupo de 2 Personas: [Keimer Duvan Moreno \ Juan Sebastian Londoño]

import math

# -------------------- FUNCIONES --------------------
def contar_caracteres(texto):
    """Cuenta la cantidad de caracteres de un texto."""
    return len(texto)

def factorial(n):
    """Calcula el factorial de un número entero."""
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def sumar_hasta_n(n):
    """Suma todos los números del 1 hasta n."""
    return sum(range(1, n+1))

# -------------------- MENÚ PRINCIPAL --------------------
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Opción 1: Operaciones con números")
    print("2. Opción 2: Submenú de funciones")
    print("3. Salir")
    opcion = input("Elige una opción (1-3): ")

    # -------------------- OPCIÓN 1 --------------------
    if opcion == "1":
        print("\nHas elegido la Opción 1: Operaciones con números")

        lista = []
        while len(lista) < 2:
            datos = input("Ingrese al menos dos números separados por espacio: ").split()
            for d in datos:
                try:
                    lista.append(float(d))
                except:
                    print(f"'{d}' no es un número válido.")

        n1 = lista[0]
        n2 = lista[1]

        # Convertimos los valores a radianes para cálculos trigonométricos correctos
        n1_rad = math.radians(n1)
        n2_rad = math.radians(n2)

        # Mostrar todos los números ingresados
        print("\nNúmeros ingresados:", lista)

        print("\nResultados (con valores en grados convertidos a radianes):")
        print(f"Seno del segundo número ({n2}°):", round(math.sin(n2_rad), 4))
        print(f"Tangente del primero ({n1}°):", round(math.tan(n1_rad), 4))
        print(f"Residuo entre el primero y segundo: {n1 % n2}")

        multiplos3 = [n for n in lista if n % 3 == 0]
        if multiplos3:
            print("Múltiplos de 3:", multiplos3)
        else:
            print("No hay múltiplos de 3.")

    # -------------------- OPCIÓN 2 --------------------
    elif opcion == "2":
        print("\nHas elegido la Opción 2: Submenú de funciones")
        print("1. Contar caracteres")
        print("2. Calcular factorial")
        print("3. Sumar del 1 al N")
        subopcion = input("Elige una opción del submenú (1-3): ")

        if subopcion == "1":
            print("\nElegiste la opción 1: Contar caracteres")
            texto = input("Ingrese un texto: ")
            print("El texto tiene", contar_caracteres(texto), "caracteres.")

        elif subopcion == "2":
            print("\nElegiste la opción 2: Calcular factorial")
            n = int(input("Ingrese un número entero: "))
            print("El factorial de", n, "es:", factorial(n))

        elif subopcion == "3":
            print("\nElegiste la opción 3: Sumar del 1 al N")
            n = int(input("Ingrese un número entero: "))
            print("La suma del 1 al", n, "es:", sumar_hasta_n(n))

        else:
            print("La opción del submenú no es válida.")

    # -------------------- SALIR --------------------
    elif opcion == "3":
        print("\nSaliendo del programa...")
        break

    # -------------------- OPCIÓN INVÁLIDA --------------------
    else:
        print("\nLa opción elegida no es válida.")
