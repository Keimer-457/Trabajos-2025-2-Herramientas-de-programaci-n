#Juan Londoño
# Y
#Keimer Moreno

#Codigo Fuerza Bruta con validaciones --------------------------------------------------------------

# Paso 1: Solicitar numero de usuarios (validando que sea un numero)
while True:
    num_usuarios = input("Cuantos usuarios desea registrar: ").strip()
    if num_usuarios.isdigit() and int(num_usuarios) > 0:
        num_usuarios = int(num_usuarios)
        break
    else:
        print("Por favor, ingrese un numero valido mayor que 0.")

# Paso 2: Crear diccionario para almacenar usuarios
usuarios = {}

for i in range(num_usuarios):
    print(f"\nRegistro del usuario {i+1}")

    # Validacion nombre (solo letras y espacios)
    while True:
        nombre = input("Ingrese el nombre: ").strip()
        if nombre.replace(" ", "").isalpha():
            break
        print("Nombre invalido. Solo se permiten letras y espacios.")

    # Validacion numero de cuenta bancaria (solo digitos y minimo 10)
    while True:
        cuenta = input("Ingrese el numero de cuenta bancaria: ").strip()
        if cuenta.isdigit() and len(cuenta) >= 10:
            break
        print("Numero de cuenta invalido. Debe contener solo numeros y minimo 10 digitos.")

    # Validacion clave de 3 digitos
    while True:
        clave = input("Ingrese clave de 3 digitos: ").strip()
        if clave.isdigit() and len(clave) == 3:
            print("Clave valida")
            break
        print("Clave invalida, intente nuevamente")

    # Guardamos en el diccionario
    usuarios[nombre] = {
        "cuenta": cuenta,
        "clave": clave
    }
    print("\nUsuario registrado correctamente\n")

# Paso 3: Solicitar el usuario a consultar
usuario_buscar = input("\nIngrese el nombre del usuario a consultar: ").strip()

if usuario_buscar in usuarios:
    clave_real = usuarios[usuario_buscar]["clave"]

    # Paso 4: Simular fuerza bruta
    print("\nIniciando ataque de fuerza bruta para encontrar la clave...")
    encontrada = False
    intentos = 0

    for intento in range(0, 1000):  # claves de 000 a 999
        intentos += 1
        clave_intento = str(intento).zfill(3)  # asegura formato 3 digitos

        if clave_intento == clave_real:
            print(f"Intento {intentos}: {clave_intento}  <-- ESTA AQUI ")
            encontrada = True
            print(f"\nClave encontrada: {clave_intento}")
            print(f"Total de intentos realizados: {intentos}")
            break
        else:
            print(f"Intento {intentos}: {clave_intento}")

    if not encontrada:
        print("No se encontro la clave (error en los datos).")

    # Paso 5: Mostrar la informacion completa
    print("\nInformacion del usuario consultado:")
    print(f"Nombre: {usuario_buscar}")
    print(f"N Cuenta: {usuarios[usuario_buscar]['cuenta']}")
    print(f"Clave: {usuarios[usuario_buscar]['clave']}")

else:
    print("\nEl usuario no esta registrado.")
