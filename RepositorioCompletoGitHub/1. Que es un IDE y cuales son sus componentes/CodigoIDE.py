numeros = [10, 25, 37, 50, 99]
nombres = ["Ana", "Pedro", "Lucia", "Carlos"]
titulos = ("Matrix", "Inception", "Interstellar")  

# Booleanos
activo, inactivo = True, False

print("Numeros:", numeros)
print("Nombres:", nombres)
print("Titulos:", titulos)
print("Estados:", activo, inactivo)

# append
numeros.append(77)
nombres.append("Sofia")
print("\nDespues de append:", numeros, nombres)

# count
print("\nVeces que aparece 37:", numeros.count(37))

# slicing
print("Primeros 3 numeros:", numeros[:3])
print("Ultimos 2 nombres:", nombres[-2:])

# Uso de lower y upper sin ciclos
print("\nLista nombres en minusculas:", list(map(str.lower, nombres)))
print("Lista nombres en mayusculas:", list(map(str.upper, nombres)))

# Para la tupla también:
print("Titulos en mayusculas:", tuple(map(str.upper, titulos)))

# Lista vacía y string a lista
print("Lista vacia:", [])
print("String a lista:", list("Python"))

print("Primer titulo en minuscula:", titulos[0].lower())
