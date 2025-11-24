

while True:
    try:
        OpcionA = float (input("Ingrese el primer numero"))
        OpcionB = float (input("Ingrese el segundo numero"))
    except ValueError:
        print ('Solo se permiten Numeros, vuelvelo a intentar.\n')
        continue

    Operacion = input ("Ingrese una de las opciones para operar (Sumar, Restar, Dividir, Multiplicar, Potenciar, Salir): ").lower ()

    if Operacion == "sumar":
        resultado = OpcionA + OpcionB
    elif Operacion == "restar" or Operacion == "diferencia":
        resultado = OpcionA - OpcionB
    elif Operacion == "multiplicar" and not ( OpcionA == 0 or OpcionB == 0):
        resultado = OpcionA * OpcionB
    elif Operacion == "dividir" and OpcionB != 0:
        resultado = OpcionA / OpcionB
    elif Operacion == "potenciar":
        try:
            resultado = OpcionA ** OpcionB
        except OverflowError:
            resultado = ('Error: El resultado es demasiado Grande')
        except ValueError:
            resultado = ('Error: Operacion invalida con estos Numeros')

    elif Operacion == "salir":
        print ('Programa finalizado')
        break
    else: resultado = "Operacion no valida, Error"

    print ('El resultado de la Operacion es:', resultado)
