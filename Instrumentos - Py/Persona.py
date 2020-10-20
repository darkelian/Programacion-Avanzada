from abc import ABCMeta,abstractmethod

class Persona(metaclass = ABCMeta):
  def __init__(self,nombre):
    self.nombre = nombre
  def presentar(self):
    print("Hola mi nombre es",self.nombre)