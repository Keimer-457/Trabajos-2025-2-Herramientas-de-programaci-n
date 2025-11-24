"""
Programación Orientada a Objetos (POO):
  1. Abstracción: definir una plantilla general para todas las atracciones.
  2. Encapsulamiento: proteger los datos internos de cada objeto.
  3. Herencia: crear clases especializadas a partir de una clase base.
  4. Polimorfismo: usar métodos con el mismo nombre pero comportamientos distintos.

Se utiliza Kivy para construir una interfaz gráfica interactiva.

Autor: JDOS
Fecha: Mar 01/2024
"""

# PARTE 1: DEFINICIÓN DE LA CLASE BASE (ABSTRACCIÓN Y ENCAPSULAMIENTO)
# ==============================================================================
class Atraccion:
    """
    Clase base que representa una atracción genérica del parque.
    
    Abstracción: Define las características y comportamientos comunes a todas
    las atracciones, ocultando detalles innecesarios.
    
    Encapsulamiento: Los atributos comienzan con guión bajo (_) para indicar
    que son protegidos y deben manipularse mediante métodos públicos.
    """
    
    def __init__(self, nombre, capacidad, precio, duracion):
        """
        Constructor de la clase. Inicializa los atributos de una atracción.
        """
        self._nombre = nombre
        self._capacidad = capacidad
        self._precio = precio
        self._duracion = duracion
        self._en_funcionamiento = False  # Estado inicial: cerrada
        self._visitantes = 0             # Contador de visitantes del día
        self._ganancia = 0               # Ganancia acumulada del día

    def abrir(self):
        """
        Método público que cambia el estado de la atracción a 'abierta'.
        """
        self._en_funcionamiento = True
        return f"'{self._nombre}' ha sido abierta."

    def cerrar(self):
        """
        Método público que cambia el estado de la atracción a 'cerrada'.
        """
        self._en_funcionamiento = False
        return f"'{self._nombre}' ha sido cerrada."

    def operar(self, num_visitantes):
        """
        Simula el funcionamiento de la atracción con un número dado de visitantes.
        Este método será redefinido en las clases derivadas (polimorfismo).
        """
        if not self._en_funcionamiento:
            return f"Error: '{self._nombre}' está cerrada y no puede operar."
        if num_visitantes < 0:
            return "Error: el número de visitantes no puede ser negativo."
        if num_visitantes > self._capacidad:
            return f"Error: la capacidad máxima de '{self._nombre}' es {self._capacidad}."
        
        # Actualizar contadores
        self._visitantes += num_visitantes
        ganancia = num_visitantes * self._precio
        self._ganancia += ganancia
        return f"'{self._nombre}' atendió a {num_visitantes} personas. Ganancia: ${ganancia}"

    def actualizar_precio(self, nuevo_precio):
        """
        Permite modificar el precio de la atracción de forma controlada.
        """
        if nuevo_precio < 0:
            return "Error: el precio no puede ser negativo."
        self._precio = nuevo_precio
        return f"Precio de '{self._nombre}' actualizado a ${nuevo_precio}."

    def mostrar_info(self):
        """
        Devuelve una cadena con la información actual de la atracción.
        """
        estado = "Abierta" if self._en_funcionamiento else "Cerrada"
        return (
            f"\n--- {self._nombre} ---\n"
            f"Capacidad: {self._capacidad}\n"
            f"Precio: ${self._precio}\n"
            f"Duración: {self._duracion} minutos\n"
            f"Estado: {estado}\n"
            f"Visitantes hoy: {self._visitantes}\n"
            f"Ganancia hoy: ${self._ganancia}"
        )

    def estado_abierto(self):
        """
        Método de acceso para consultar el estado sin modificarlo.
        """
        return self._en_funcionamiento



# PARTE 2: CLASES DERIVADAS (HERENCIA Y POLIMORFISMO)
# ==============================================================================
class MontañaRusa(Atraccion):
    """
    Clase derivada que hereda de Atraccion e introduce un atributo específico:
    la altura máxima. Esto demuestra herencia.
    
    Además, redefine el método 'operar' para personalizar el mensaje,
    lo que ilustra polimorfismo.
    """
    
    def __init__(self, nombre, capacidad, precio, duracion, altura_max):
        # Llama al constructor de la clase base
        super().__init__(nombre, capacidad, precio, duracion)
        self._altura_max = altura_max

    def operar(self, num_visitantes):
        """
        Versión especializada del método operar.
        Polimorfismo: mismo nombre, comportamiento adaptado.
        """
        resultado = super().operar(num_visitantes)
        if "atendió a" in resultado:
            return resultado.replace(
                f"'{self._nombre}' atendió",
                f"Montaña rusa '{self._nombre}' (altura máxima: {self._altura_max} m) atendió"
            )
        return resultado


class CasaDelTerror(Atraccion):
    """
    Otra clase derivada que agrega el atributo 'nivel_miedo'.
    Herencia: reutiliza código de la clase base.
    Polimorfismo: redefine 'operar' con un mensaje temático.
    """
    
    def __init__(self, nombre, capacidad, precio, duracion, nivel_miedo):
        super().__init__(nombre, capacidad, precio, duracion)
        self._nivel_miedo = nivel_miedo

    def operar(self, num_visitantes):
        resultado = super().operar(num_visitantes)
        if "atendió a" in resultado:
            return resultado.replace(
                f"'{self._nombre}' atendió",
                f"Casa del terror '{self._nombre}' (nivel de miedo: {self._nivel_miedo}) atendió"
            )
        return resultado


class Carrusel(Atraccion):
    """
    Tercera clase derivada que incluye el tipo de música.
    Refuerza el concepto de herencia y polimorfismo.
    """
    
    def __init__(self, nombre, capacidad, precio, duracion, tipo_musica):
        super().__init__(nombre, capacidad, precio, duracion)
        self._tipo_musica = tipo_musica

    def operar(self, num_visitantes):
        resultado = super().operar(num_visitantes)
        if "atendió a" in resultado:
            return resultado.replace(
                f"'{self._nombre}' atendió",
                f"Carrusel '{self._nombre}' (música: {self._tipo_musica}) atendió"
            )
        return resultado



# PARTE 3: CLASE PARQUE (COMPOSICIÓN)
# ==============================================================================
class Parque:
    """
    Clase que gestiona un conjunto de atracciones.
    Usa composición: el parque "tiene" atracciones, pero no hereda de ellas.
    """
    
    def __init__(self, nombre):
        self._nombre = nombre
        self._atracciones = []  # Lista que contendrá objetos de tipo Atraccion

    def agregar_atraccion(self, atraccion):
        """
        Agrega una atracción al parque.
        """
        self._atracciones.append(atraccion)

    def buscar_atraccion(self, nombre):
        """
        Busca una atracción por su nombre y devuelve el objeto.
        """
        for atr in self._atracciones:
            if atr._nombre == nombre:
                return atr
        return None

    def abrir_todas(self):
        """
        Abre todas las atracciones del parque.
        """
        for atr in self._atracciones:
            atr.abrir()

    def cerrar_todas(self):
        """
        Cierra todas las atracciones del parque.
        """
        for atr in self._atracciones:
            atr.cerrar()

    def reporte_general(self):
        """
        Genera un informe consolidado con los datos de todas las atracciones.
        """
        total_visitantes = sum(atr._visitantes for atr in self._atracciones)
        total_ganancia = sum(atr._ganancia for atr in self._atracciones)
        
        print(f"\n{'='*60}")
        print(f"INFORME DEL PARQUE: {self._nombre}")
        print(f"Total de visitantes hoy: {total_visitantes}")
        print(f"Ganancia total hoy: ${total_ganancia}")
        print(f"{'='*60}")
        
        for atr in self._atracciones:
            print(atr.mostrar_info())
        
        print(f"{'='*60}")



# PARTE 4: INTERFAZ DE CONSOLA
# ==============================================================================
def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n" + "="*60)
    print("           PARQUE DE ATRACCIONES - MENÚ PRINCIPAL")
    print("="*60)
    print("1. Ver estado de todas las atracciones")
    print("2. Abrir una atracción específica")
    print("3. Cerrar una atracción específica")
    print("4. Operar una atracción (ingresar visitantes)")
    print("5. Cambiar el precio de una atracción")
    print("6. Abrir todas las atracciones")
    print("7. Cerrar todas las atracciones")
    print("8. Generar informe general del parque")
    print("9. Salir del programa")
    print("="*60)


def main():
    """
    Función principal que ejecuta el programa interactivo.
    Crea el parque, agrega atracciones y gestiona la interacción con el usuario.
    """
    # Crear el parque y agregar atracciones de ejemplo
    parque = Parque("Aventura Familiar")
    parque.agregar_atraccion(MontañaRusa("Dragón Veloz", 20, 15000, 3, 35))
    parque.agregar_atraccion(CasaDelTerror("Mansión Embrujada", 15, 12000, 5, 8))
    parque.agregar_atraccion(Carrusel("Carrusel Infantil", 25, 8000, 4, "clásica"))
    
    # Obtener lista de nombres para facilitar la selección
    nombres_atracciones = [atr._nombre for atr in parque._atracciones]

    # Bucle principal del programa
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción (1-9): "))
        except ValueError:
            print("Error: Por favor ingrese un número entero entre 1 y 9.")
            continue

        if opcion == 1:
            # Mostrar estado de todas las atracciones
            print("\n--- ESTADO ACTUAL DE LAS ATRACCIONES ---")
            for atr in parque._atracciones:
                print(atr.mostrar_info())

        elif opcion == 2:
            # Abrir una atracción específica
            print("\nAtracciones disponibles:")
            for i, nombre in enumerate(nombres_atracciones, 1):
                print(f"{i}. {nombre}")
            try:
                idx = int(input("Ingrese el número de la atracción a abrir: ")) - 1
                if 0 <= idx < len(nombres_atracciones):
                    atraccion = parque.buscar_atraccion(nombres_atracciones[idx])
                    print(atraccion.abrir())
                else:
                    print("Error: Número de atracción inválido.")
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == 3:
            # Cerrar una atracción específica
            print("\nAtracciones disponibles:")
            for i, nombre in enumerate(nombres_atracciones, 1):
                print(f"{i}. {nombre}")
            try:
                idx = int(input("Ingrese el número de la atracción a cerrar: ")) - 1
                if 0 <= idx < len(nombres_atracciones):
                    atraccion = parque.buscar_atraccion(nombres_atracciones[idx])
                    print(atraccion.cerrar())
                else:
                    print("Error: Número de atracción inválido.")
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == 4:
            # Operar una atracción
            print("\nAtracciones disponibles:")
            for i, nombre in enumerate(nombres_atracciones, 1):
                print(f"{i}. {nombre}")
            try:
                idx = int(input("Seleccione la atracción a operar: ")) - 1
                if 0 <= idx < len(nombres_atracciones):
                    nombre = nombres_atracciones[idx]
                    num_visitantes = int(input(f"Ingrese el número de visitantes para '{nombre}': "))
                    atraccion = parque.buscar_atraccion(nombre)
                    resultado = atraccion.operar(num_visitantes)
                    print(resultado)
                else:
                    print("Error: Número de atracción inválido.")
            except ValueError:
                print("Error: Ingrese números válidos.")

        elif opcion == 5:
            # Cambiar el precio de una atracción
            print("\nAtracciones disponibles:")
            for i, nombre in enumerate(nombres_atracciones, 1):
                print(f"{i}. {nombre}")
            try:
                idx = int(input("Seleccione la atracción para cambiar su precio: ")) - 1
                if 0 <= idx < len(nombres_atracciones):
                    nombre = nombres_atracciones[idx]
                    nuevo_precio = int(input(f"Ingrese el nuevo precio para '{nombre}': "))
                    atraccion = parque.buscar_atraccion(nombre)
                    resultado = atraccion.actualizar_precio(nuevo_precio)
                    print(resultado)
                else:
                    print("Error: Número de atracción inválido.")
            except ValueError:
                print("Error: Ingrese un número entero válido.")

        elif opcion == 6:
            # Abrir todas las atracciones
            parque.abrir_todas()
            print("Todas las atracciones han sido abiertas.")

        elif opcion == 7:
            # Cerrar todas las atracciones
            parque.cerrar_todas()
            print("Todas las atracciones han sido cerradas.")

        elif opcion == 8:
            # Generar informe general
            parque.reporte_general()

        elif opcion == 9:
            # Salir del programa
            print("Gracias por usar el sistema del Parque de Atracciones. ¡Hasta pronto!")
            break

        else:
            print("Error: Opción no válida. Por favor seleccione un número entre 1 y 9.")



# PUNTO DE ENTRADA DEL PROGRAMA
# ==============================================================================
if __name__ == "__main__":
    """
    Este bloque se ejecuta solo si el archivo se corre directamente.
    Llama a la función principal para iniciar la interacción.
    """
    main()