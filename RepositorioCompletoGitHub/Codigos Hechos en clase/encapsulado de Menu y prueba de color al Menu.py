def Menu ():
  while True:
    print ("         ")
    print ("\033[96m---MENU---\033[")
    print ("         ")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicacion")
    print ("4. Salir")

    opcion = input ("Elige una opcion: ")

    if opcion == "1":
        print ("\nelegiste la opcion 1: ")
        try:
          var1 = float(input("Ingrese el primer numero: "))
          var2 = float(input("Ingrese el segundo numero: "))
          print ("La suma es: ", var1 + var2)
        except ValueError:
            print("Entrada no válida. Por favor ingrese números.")
            print("-"*20)
            print("-"*20)
            print("-"*20)
    elif opcion == "2":
        print ("\nelegiste la opcion 2: ")
        try:
          var1 = float (input("Ingrese el primer numero: "))
          var2 = float (input("Ingrese el segundo numero: "))
          print ("La resta es: ", var1 - var2)
        except ValueError:
            print("Entrada no válida. Por favor ingrese números.")
            print("-"*20)
            print("-"*20)
            print("-"*20)
    elif opcion == "3":
        print ("\nelegiste la opcion 3: ")
        try:
          var1 = float (input("Ingrese el primer numero: "))
          var2 = float (input("Ingrese el segundo numero: "))
          print ("La multiplicacion es: ", var1 * var2)
        except ValueError:
            print("Entrada no válida. Por favor ingrese números.")
            print("-"*20)
            print("-"*20)
            print("-"*20)
    elif opcion == "4":
        print ("Saliste del programa")
        break
    else:
        print ("Opcion no valida")
        print("-"*20)
        print("-"*20)


Menu()
