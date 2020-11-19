# Pedir la categoria para conocer el ganador
categoria = input("Selecciona una categoria: ")  
# Arreglo para guardar los intentos
intentos = []
turno = 20
# Abrir archivo.txt
t = open("archivos2.txt", "r")
# Ciclo for para recorrer el archivo linea por linea 
for c in t.readlines():
    # Lista para hacer comparaciones   
    x = [str(x) for x in c.split("-")] 
    if (x[1] =='true' and  x[2] == str(categoria)): 
         # Agregar numero de intentos a la lista intentos
         intentos.append(int(x[3]))  
# Ciclo for para determinar cual es el menor numero de intentos de cada categoria 
for i in range(0, len(intentos)):
    if (intentos[i] < turno):
         turno = intentos[i]              
t.close() 
p = open("archivos2.txt", "r")
ganador = []  
 # ciclo para imprimir al ganador de la categoria    
for b in p.readlines():  
    y = [str(y) for y in b.split("-")]
    if(y[1] == 'true' and y[2] == str(categoria) and y[3] == str(turno)): 
        ganador.append(y[0]+" con "+y[3]+" intentos")  
        print("El ganador de la categoria "+str(categoria)+" es: ") 
        print(ganador) 
        exit()
print("no hay un ganador en esta categoria")      
p.close()


  
