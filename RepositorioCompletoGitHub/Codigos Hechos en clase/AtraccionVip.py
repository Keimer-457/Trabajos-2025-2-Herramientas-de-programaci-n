class Atraccion:
  def __init__(self):
    self.tipo   = "Atraccion general"
    self.tipo2  = ", Especial"
    self.tipo3  = "y VIP"

class Juego:
  def __init__(self):
    self.tipo = "Juego mecanico"

class Parque(Juego,Atraccion,):
  def __init__(self):
    Atraccion.__init__(self)
    self.tipo_padre1 = self.tipo
    self.tipo2 = self.tipo2
    self.tipo3 = self.tipo3
    Juego.__init__(self)
    self.tipo_padre2 = self.tipo

obj = Parque()
print("Tipo desde Atraccion: ", obj.tipo_padre1,obj.tipo2,obj.tipo3)
print("Tipo desde Juego: ", obj.tipo_padre2)
