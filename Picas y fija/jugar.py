""" 
Integrantes:
Elian Peña   20192020106
Dayana Acuña 20192020120
"""
# Importar librería para generar random
from random import randint 
# Metodo para generar Numero aleatorio
def generar_secreto(cantidad):
  secreto = []
  while True:
    d = randint(0, 9)
    if d not in secreto:
       secreto.append(d)
    if len(secreto) == cantidad:
        break
  return secreto

# Metodo para validar que los numeros no se repitan
def validar_numero(numero):
  if len(numero) == 1:
      return True
  else:
      if numero[0] in numero[1:]:
          return False
      else:
          return validar_numero(numero[1:])

class jugar:
  # Mensaje de bienvenida
  print('\t\t////////////////////////////////////////////////')
  print('\t\t//               Picas  y Fijas               //')
  print('\t\t------------------------------------------------')
  # Pedir nombre de usuario
  usuario = input("ingrese nombre de usuario : ")
  # Pedir numero de cifras para seleccionar nivel
  n = int(input("ingrese el numero de digitos para jugar: "))
  # Logica del juego para 3 cifras
  if (n == 3):
    f = open("archivos2.txt", "a")
    s = generar_secreto(3)
    ganador = False
    # For para recorrer la lista y comparar los digitos del usuario con el aleatorio
    for i in range(1, 11):
      print("\nJUGADA #{0} ".format(i))
      p = [int(x) for x in input("ingrese un numero: ")]
      if (len(p) > 3 or len(p) < 3):
        print("No se ingreso los digitos correspondientes")
        input("Presione una tecla para continuar ...")
        break
      if (p[0] == p[1] or p[0] == p[2] or p[1] == p[0] or p[1] == p[2] or p[2] == p[0] or p[2] == p[1]):
        print("Digito repetido")
        input("Presione una tecla para continuar ...")
        break
      print(p)
      fijas = 0
      for j in range(0,3):
        if s[j] == p[j]:
          fijas = fijas + 1
      if fijas == 3:
        print("\nGANASTE :) ")
        ganador = True
        picas=0
        f.write(usuario+"-"+str(ganador)+"-"+str(n)+"-"+str(i)+"-"+str(p)+"-"+str(fijas)+"-"+str(picas)+"\n")
        input("Presione una tecla para continuar ...")
        break

      picas = 0
      if s[0] != p[0] and (s[0] == p[1] or s[0] == p[2]):
         picas = picas + 1
      if s[1] != p[1] and (s[1] == p[0] or s[1] == p[2]):
         picas = picas + 1
      if s[2] != p[2] and (s[2] == p[0] or s[2] == p[1]):
         picas = picas + 1
      print("FIJAS: {0}, PICAS: {1}". format(fijas, picas))
      # Escribir los datos en el block de notas
      f.write(usuario+"-"+str(ganador)+"-"+str(n)+"-"+str(i)+"-"+str(p)+"-"+str(fijas)+"-"+str(picas)+"\n")
    if ganador == False:
        print("\nPERDISTE EL JUEGO :( ")
        input("Presione una tecla para continuar ...")
    f.close()
    
  # Logica del juego para 4 cifras
  if (n == 4):
    f = open("archivos2.txt", "a")
    s = generar_secreto(4)
    ganador = False
    # For para recorrer la lista y comparar los digitos del usuario con el aleatorio
    for i in range(1,16 ):
      print("\nJUGADA #{0} ".format (i))
      p = [int(x) for x in input("ingrese un numero: ")]
      if (len(p) >4 or len(p)<4): 
         print("No se ingreso los digitos correspondientes")
         input("Presione una tecla para continuar ...")
         break
      if (p[0] == p[1] or p[0] == p[2] or p[0] == p[3] or p[1] == p[0] or p[1] == p[2] or p[1] == p[3] or p[2] == p[0] or p[2] == p[1] or p[2] == p[3] or p[3] == p[0] or p[3] == p[1] or p[3] == p[2] ):
         print("Digito repetido")
         input("Presione una tecla para continuar ...")
         break
      print(p)
      fijas = 0
      for j in range(0,4):
        if s[j] == p[j]:
           fijas = fijas + 1  
      if fijas == 4 :
         print("\n GANASTE :)")
         ganador = True
         picas=0
         f.write(usuario+"-"+str(ganador)+"-"+str(n)+"-"+str(i)+"-"+str(p)+"-"+str(fijas)+"-"+str(picas)+"\n")
         input("Presione una tecla para continuar ...")
         break
      picas = 0
      if  s[0] != p[0] and (s[0] == p[1] or s[0] == p[2] or s[0] == p[3]):
         picas = picas + 1
      if  s[1] != p[1] and (s[1] == p[0] or s[1] == p[2] or s[1] == p[3]):
         picas = picas + 1
      if  s[2] != p[2] and (s[2] == p[0] or s[2] == p[1] or s[2] == p[3]):
         picas = picas + 1
      if  s [3] != p[3] and (s[3] == p[0] or s[3] == p[1] or s[3] == p[2]):
         picas = picas + 1  
      print("FIJAS: {0}, PICAS: {1}". format (fijas,picas))
    # Escribir los datos en el block de notas
      f.write(usuario+"-"+str(ganador)+"-"+str(n)+"-"+str(i)+"-"+str(p)+"-"+str(fijas)+"-"+str(picas)+"\n")     
    if ganador  == False:
        print ("\nPERDISTE EL JUEGO :( ")
        input("Presione una tecla para continuar ...")
        # Escribir los datos en el block de notas
    f.close()
    
  # Logica del juego para 5 cifras
  if(n == 5):
    f = open("archivos2.txt", "a")
    s = generar_secreto(5)
    ganador = False
    for i in range(1,24 ):
      print("\nJUGADA #{0} ".format (i))
      p = [int(x) for x in input("ingrese un numero: ")]
      if (len(p) >5 or len(p)<5): 
         print("No se ingreso los digitos correspondientes")
         input("Presione una tecla para continuar ...")
         break
      if (p[0] == p[1] or p[0] == p[2] or p[0] == p[3] or p[0] == p[4] or p[1] == p[0] or p[1] == p[2] or p[1] == p[3] or p[1] == p[4] or p[2] == p[0] or p[2] == p[1] or p[2] == p[3] or p[2] == p[4] or p[3] == p[0] or p[3] == p[1] or p[3] == p[2] or p[3] == p[4] or p[4] == p[0] or p[4] == p[1] or p[4] == p[2] or p[4] == p[3] ):
         print("Digito repetido")
         input("Presione una tecla para continuar ...")
         break
      print(p)
      fijas = 0
      for j in range(0,5):
        if s[j] == p[j]:
          fijas = fijas + 1
      if fijas == 5 :
         print("\n GANASTE :)")
         ganador = True
         picas=0
         f.write(usuario+"-"+str(ganador)+"-"+str(n)+"-"+str(i)+"-"+str(p)+"-"+str(fijas)+"-"+str(picas)+"\n")
         break
      picas = 0
      if  s[0] != p[0] and (s[0] == p[1] or s[0] == p[2] or s[0] == p[3] or s[0] == p[4]):
         picas = picas + 1
      if  s[1] != p[1] and (s[1] == p[0] or s[1] == p[2] or s[1] == p[3] or s[1] == p[4]):
         picas = picas + 1
      if  s[2] != p[2] and (s[2] == p[0] or s[2] == p[1] or s[2] == p[3] or s[2] == p[4] ):
         picas = picas + 1
      if  s[3] != p[3] and (s[3] == p[0] or s[3] == p[1] or s[3] == p[2] or s[3] == p[4]):
         picas = picas + 1
      if  s[4] != p[4] and (s[4] == p[0] or s[4] == p[1] or s[4] == p[2] or s[4] == p[3]):
         picas = picas + 1
      print("FIJAS: {0}, PICAS: {1}". format (fijas,picas))
      # Escribir los datos en el block de notas
      f.write(usuario+"-"+str(ganador)+"-"+str(n)+"-"+str(i)+"-"+str(p)+"-"+str(fijas)+"-"+str(picas)+"\n")  
    if ganador  == False:
       print ("\nPERDISTE EL JUEGO :( ")
       input("Presione una tecla para continuar ...")    
    f.close()
  # Imprimir mensajes por digitaciones erroneas
  if (n > 5 or n < 3):
     print("juego solo disponible para 3 y 4 digitos :)") 
     input("Presione una tecla para continuar ...")
