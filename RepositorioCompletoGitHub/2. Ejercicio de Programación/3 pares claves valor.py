# 1. CREAR UN DICCIONARIO CON 3 PARES CLAVE-VALOR
mi_diccionario = {
    "nombre": "Juan",
    "edad": 31,
    "ciudad": "Bogotá"
}

print("1) Diccionario inicial:", mi_diccionario)

# 2. ADICIONAR UN ELEMENTO AL DICCIONARIO

mi_diccionario["profesion"] = "Estudiante"
print("2) El Diccionario después de adicionar:", mi_diccionario)

# 3. ELIMINAR UN ELEMENTO DEL DICCIONARIO

del mi_diccionario["edad"]
print("3) Diccionario después de eliminar:", mi_diccionario)

# 4. USO DEL INPUT PARA SOLICITAR INFORMACIÓN

nombre_usuario = input("4) Ingrese su nombre: ")
print("Hola yo soy :", nombre_usuario)

# 5. BUCLES FOR

# a) Bucle for normal recorriendo una lista
print("\n5a) Bucle for normal:")
for fruta in ["Manzana", "Banano", "Serpiente"]:
    print(fruta)

# b) Bucle for con paso usando range(inicio, fin, paso)
print("\n5b) Bucle for con el paso:")
for i in range(0, 10, 2):
    print(i)

# c) Bucle for con un solo argumento en range(fin)
print("\n5c) Bucle for con un solo argumento:")
for i in range(5):
    print(i)
