import os
# Se define el nombre de la carpeta o directorio a crear
directorio = "D:/braya/Documents/SEMESTRE 2020-3/PROGRAMACIÓN AVANZADA/Reto2.0/dir_prueba"
try:
    os.mkdir(directorio)
except OSError:
    print("La creación del directorio %s falló" % directorio)
else:
    print("Se ha creado el directorio: %s " % directorio)