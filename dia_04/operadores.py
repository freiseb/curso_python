#   OPERACIONES DE COMPARACION
# mi_bool = 10==25 #igauladad
# mi_bool1 = 100!=99 #es para saber si son diferentes 
# print(mi_bool)

#   OPERADORES LOGICOS
    #and (Debe cumplirse)
    #on (solo una debe cumplirse)
    #not (no debe cumplirse)
#ejem
# mi_bool = (4 < 5) and (5 > 6)
# print(mi_bool)

# mi_bool1 = 10 == 10 or 3==3
# print(mi_bool1)
# texto = "esta frase es un breve"
# mi_booltexto = ("fase" in texto) or ('python' in texto)

# mi_bool2 = not ('a' != 'a') 

    #CONTROL DE FLUJOS
    #if (si se cumple sigue)
    #else (si no se cumple)
    #elif(si nose cumple, pero hay como agregar mas)
#ejem
# if 10 > 9:
#     print('Es correcto')
# else:
#     print('No es correxto')
    
# mascota = "perro"
# if mascota == "gato":
#     print('tienes un gato')
# elif mascota == "perro":
#     print('Tienes un perro')
# elif mascota == 'pez':
#     print('tienes un pez')
# else:
#     print('no se que animal es')

# edad = 15
# if edad < 18:
#     print("Eres menor de edad")
#     if calificacion >= 7:
#         print('Aprobado')
#     else:
#         print('no has probado')
# else:
#     print('Eres adulto')


    #INTRODUCCION A LOOP
        #LOOP FOR 
    #EJEM
# lista = ['a', 'b', 'c']
# for letra in lista:
#     numero_letra = lista.index(letra) + 1
#     print(f"letra {numero_letra}: {letra}")
    
    
# lista2 = ['juan', 'laura', 'fede', 'luis', 'julia']
# for nombre in lista2:
#     if nombre.startswith('l'): #starswith que es para ver si comienza con cualquier caracter
#         print(nombre)
#     else:
#         print("Nombre que o comienza con l")
    
    
# numeros = [1, 2, 3, 4, 5] 
# mi_valor = 0
# for numero in numeros:
#     mi_valor = mi_valor + numero
    
#     print(mi_valor)

# dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
# for item in dic.items():
#     print(item)
    
# dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
# for a,b in dic.items():
#     print(a,b)

    #LOOP WHILE
#ejem
# monedas = 5
# while monedas > 0:
#     print(f"teno {monedas} monedas")
#     monedas -= 1 
# else:
#     print("no tengo mas dinero")

# respuesta = "s"
# while respuesta == "s":
#     respuesta = input("quieres seguir? (s/n)") #pass sirve para reservar un espacio 
# else:                                          #
#     print("Gracais")
    
# nombre = input("TU nombre: ")
# for letra in nombre:
#     if letra == 'r':
#         break #sirve para interrupir y (continue sirve para que continue pero se salta la letra)
#     print(letra) 
    
    #RANGO(RANGE)
#EJEM
#
# for numero in range(5):
#     print(numero)
    
# lista = list(range(1.101))
# print(lista)

    #ENUMADOR
# #ejem
# lista = ['a', 'b', 'c']
# for indice, item in enumerate(lista):
#     print(item)
    
# for indice, item in enumerate(range(50, 55)):
#     print(item)
    
# mis_tuples = list(enumerate(lista))
# print(mis_tuples)

#     #ZIP
# #   EJEM
# nombres = ['ana', 'hugo', 'valeria']
# edades = [65, 39,43]

# combinados = list(zip(nombres, edades))
# for nombre, edad in combinados:
#     print(f"{nombre} tiene {edad} anios  ")    

    #MIN
#ejem

# lista = [58, 96, 72, 64, 35]
# print(f"El menos es {min(lista)} y el mayor es {max(lista)}")
# min(dic.values())


    #   RANDOM
#ejem
from random import * 
aleatorio = randint(1,50)
print(aleatorio)

aleatorio1 = round(uniform(1,5),1)#para sacar desimales
aleatorio2 = random()#para usar con fracciones
colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio3 = choice(colores)#para hacer con strins
print(aleatorio3)

numeros = list(range(5,50,5))
shuffle(numeros)#para mesclar numeros, no hay como ocupa con strin y ni en listas
print(numeros)

