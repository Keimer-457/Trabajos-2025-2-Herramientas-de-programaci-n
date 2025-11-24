# Keimer Duvan Moreno Murillo : 1077436457
# Juan Sebastián Londoño : 1065871157

# ----------------------------------------------
# Ejercicio práctico de Programación Orientada a Objetos (POO)
# Tema: Polimorfismo
# Lenguaje: Python
# ----------------------------------------------

# Clase base o padre
class Vehiculo:
    def avanzar(self):
        print("El vehículo avanza.")

# Clases hijas que heredan de Vehiculo
# Cada una redefine el método avanzar()
class Carro(Vehiculo):
    def avanzar(self):
        print("El carro está rodando por la carretera.")

class Avion(Vehiculo):
    def avanzar(self):
        print("El avión despega y vuela en el cielo.")

class Barco(Vehiculo):
    def avanzar(self):
        print("El barco navega por el mar.")

# Lista que contiene distintos tipos de vehículos
vehiculos = [Carro(), Avion(), Barco()]

# ----------------------------------------------
# Aquí se demuestra el POLIMORFISMO:
# Se llama al mismo método 'avanzar()' en diferentes objetos.
# Cada uno ejecuta su propia versión del método.
# ----------------------------------------------
for v in vehiculos:
    v.avanzar()
