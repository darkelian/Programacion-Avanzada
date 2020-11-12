def menu():
  print("""
  Elija una opción
  1) Registrar jugador
  2) Jugar
  3) Salir
  """)
opcion = input("Seleccione algo : ")
if opcion =="1":
    print(":)")   
   #from jugador import Persona
    #jugador=Persona()
    #jugador.imprimir()
    #menu()
    break
if opcion=="2":
    #from jugar import jugar
    break
if opcion =="3":
    print("¡Gracias or probar nuestro juego!")
    exit()
    break
else:
    print("Opción inválida, intente nuevamente")
    menu()
