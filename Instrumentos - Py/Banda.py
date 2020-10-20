from Musico import Musico
from Persona import Persona
from Violin import Violin
from Bajo import Bajo
from  Guitarra import Guitarra
import random
Musicos = []
class Banda():
  def agregarMusico(self,nombre):
    m=Musico(nombre)
    Musicos.append(m)
  def generarInstrumento(self):
    opc=random.randrange(3)
    if(opc==0):
      return Guitarra()
    elif(opc==1):
      return Bajo()
    elif(opc==2):
      return Violin()
  def presentarBanda(self):
    for cantante in Musicos:
      cantante.presentar()
      cantante.tocar(self.generarInstrumento())