from Instrumento import Instrumento
class Bajo(Instrumento):
  def afinar(self):
    print("afinando bajo")
  def tocar(self):
    print("Tocando bajo")
  def Tocar(self,nota):
    print("Tocando bajo en:  ",nota)