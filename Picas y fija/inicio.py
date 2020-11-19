import os
class inicio:
    
    def menu():
        #os.system('cls') # NOTA para windows tienes que cambiar clear por cls
        print("Selecciona una opción")
        print("\t1 - Jugar")
        print("\t2 - Campeones")
        print("\t3 - Salir")

    while True:
        # Mostramos el menu
        menu()

    # solicituamos una opción al usuario
        opcionMenu = input("Ingresa una opcion >> ")
        if opcionMenu == "1":
            from jugar import jugar
        elif opcionMenu == "2":
            from jugador import jugador  
        elif opcionMenu == "3":
            break
        else:
            print("")
            input("Opcion incorrecta :(...\npulsa una tecla para continuar")
