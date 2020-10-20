from Instrumento import Instrumento

class Guitarra(Instrumento):

  def tocar(self):
    print("Tocando guitarra")
  def afinar(self):
    print("Afinando guitarra")
  def Tocar(self,nota):
    print("Tocando guitarra en: " + nota)