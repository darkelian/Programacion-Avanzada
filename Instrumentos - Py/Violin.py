from Instrumento import Instrumento

class Violin(Instrumento):
  def tocar(self):
    print("Tocando violin")
  def afinar(self):
    print("Afinando violin")
  def Tocar(self,nota):
    print("Tocando violin en:  ",nota)
    