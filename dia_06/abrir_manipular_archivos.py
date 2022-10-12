mi_archivo = open('prueba.txt')
# print(mi_archivo.read())
# una_linea = mi_archivo.readline()
# print(mi_archivo.readline())
# for l in mi_archivo:
#     print('aqui dice : ' + l)
# todas = mi_archivo.readlines()
# todas = todas.pop()
# print(todas)
# mi_archivo.close()

                                #  CREAR Y ESCRIBIR ARCHIVOS

# r = solo lectura 
# w = solo escritura 
# a = solo escribir al final del archivo

# archivo = open('prubea1.txt', 'a')
# lista = ['hola','mundo','awui','estoy']
# for p in lista:
    # archivo.writelines(p + "\n")
# archivo.write('bienvenido')    
# archivo.close() 

                                # DIRECTORIOS
import os
# ruta = os.getcwd()#para saber en que caperta estas
# ruta = os.chdir()#para buscar otros archivos
# ruta = os.makedirs()#para crear otra carpeta
# ruta = '//home//lich/Desktop//curso_python//dia_06//prueba.txt'
# elemento = os.path.dirname(ruta)
# elemento = os.path.split(ruta)
# os.rmdir()#para eliminar carpetas
# print(elemento)  
# archivo = open()
# # print(ruta)
# from pathlib import Path

# carpeta = Path('//home//lich/Desktop//profile') / 'otro_archivo.txt'

# mi_archivo = open(carpeta)
# print(mi_archivo.read())

                                #PATHLIB

# from pathlib import Path,PureWindowsPath

# carpeta = Path('//home//lich/Desktop//curso_python//dia_06//prueba.txt')

# ruta_windos = PureWindowsPath(carpeta)
# print(ruta_windos)
# if not carpeta.exists():
#     print("este archivo exite")
# else:
#     print("genial, existe")

# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)

                            # PATH

from pathlib import Path

# base = Path.home()
# guia = Path(base, "Europa", "Espana",Path("Barcelona", "Sagrada_familia.txt"))
# # guia2 = guia.with_name("La_pedreda.txt")
# print(guia.parent)
# guia = Path(Path.home(),"Europa")
# for txt in Path(guia).glob('**//.txt'):
#     print(txt)
# guia = Path("Europa", "Espana","Barcelona", "Sagrada_familia.txt")
# en_europa = guia.relative_to(Path('Europa'))
# en_espania = guia.relative_to(Path('Europa', 'Espana'))
# print(en_espania)
# print(en_espania)

                                # LIMPIAR LA CONSOLA
from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('clear')
print(f"Tu nombre es {nombre} y tienes {edad} anios")


