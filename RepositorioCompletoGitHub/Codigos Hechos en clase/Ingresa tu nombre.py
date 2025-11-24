def pablito ():

  print ("Hola estudiantes")
  a = input ("Ingrese su nombre: ")
  print (f"hola {a} como estas?")
  b = 5
  c = float (input("ingrese un numero entero: "))
  print (f"El resultado de 5 * {c} es: ")
  print (b*c)
  print (b*a)
  print (50*"-")

def elnegritodelwasa ():
  while True:
    el = input ("eres : ")
    if el in ["si", "no"]:
      print ("si")
      break
  else: print ("solo si o no ")
pablito ()
elnegritodelwasa ()

def holaquehace (a,b):

  print (" el valor del numero es: ",a)
  print (" el valor del numero es: ",b)
  print (" el resultado de la resta es: ",a-b)
  print (a-b)

holaquehace (a=5,b=5)

def Prueba (a=3,b=7):

  print (" el valor del numero es: ",a)
  print (" el valor del numero es: ",b)
  print (" el resultado de la multiplicacion es: ",a*b)
  print (a*b)

Prueba (b=2)
