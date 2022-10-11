# mi_texto = "Esta es una prueba"
# resultado = mi_texto[0]
# print(resultado)

# mi_texto = "Esta es una prueba"
# resultado = mi_texto.index("a",5,10) #index es para buscar desde la abajo hacia arriba
# print(resultado)

# mi_texto = "Esta es una prueba"
# resultado = mi_texto.rindex("a")#rindex es para buscar la palabra desde arriba hacia abajo
# print(resultado)

#FRAGMENTO
# texto = "ABCDEFGHIJKML"
# fragmento = texto[2:5]
# print(fragmento)

# texto = "ABCDEFGHIJKML"
# fragmento = texto[2:4:6]
# print(fragmento)

# #METODOS
# texto = "Este es un texto de texto"
# metodo = texto.upper()#upper es mayusculas combierte a las letras
# print(metodo)

# texto = "Este es un texto de texto"
# metodo = texto.lower()#lower combierte todo las letras en minusculas
# print(metodo)

# texto = "Este es un texto de texto"
# metodo = texto.split() #split hace listas a las palabras
# print(metodo)


# texto = "Este es un texto de texto"
# metodo = texto.find()# find te endica en que posision esta una palabra que busques
# print(metodo)

# texto = "Este es un texto de texto"
# metodo = texto.replace("e", "x") #replace remplasa con dos argunemnto es decir si pongo "e" y "x" todas la palabras que tenga una e seran cambiadas por una x
# print(metodo)

# a = "Apremder"
# b = "pyhton"
# c = "es"
# d = "genial"
# e = " ".join([a, b, c, d])
# print(e)


#PROPIEDADES
# nombre = "Carina"
# nombre = "karina"

# n1 = "kari"
# n2 = "na"
# print(n1 * 10)

# poema = """mil pequenos peces blancos
# como si hirviera 
# el color del agua"""
# # print(poema)
# print("agua"in poema)#bulianos
# print("agua" not in poema)
# print(len(poema))#es para ver cuantos caracteres tiene

# #LISTAS

# mi_lista = ['a', 'b', 'c']
# mi_lista2 = ['d', 'e', 'f']
# mi_lista3  mi_lista + mi_lista2
# resultado = len(mi_lista)
# resultado = mi_lista[0]
# print()


# mi_lista = ['a', 'b', 'c']
# mi_lista2 = ['d', 'e', 'f']
# mi_lista3  mi_lista + mi_lista2

#mi_lista3[0] = 'alfa'#aqui si hay como sobre escribir a las litas
#mi_lista3.append('g')#tambien agregar elementos
#eliminado = mi_lista3.pop(2)
#mi_lista3.pop()
# mi_lista.sort()#para ordenar caracteres 
# mi_lista.reverse()#reverse es para que haga las lista arrevez


#DICCIONARIOS

# diccionario = {'c1':'valor1', 'c2':'valor2'}
# resultado = diccionario['c1']
# print(resultado)

# cliente = {'nombre':'juan','apellido':'Fuentes', 'peso':88,
#            'talla':99}
# consulta = (cliente['apellido'])

# dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100,'s2':200}}
# print(dic['c3']['s2'])

# dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
# print(dic['c2'][1].upper())#para hacer  un dicionario para hace runa mayuscula

# dic = {1:'a', 2:'b'}
# dic[3] = 'c'               #para agregar otro diccionario
# # dic[2] = 'B'

# print(dic.keys())#para saber las llaves
# print(dic.values)# para verlos valores
# print(dic.items())#para ver todos los elementos
# print(dic)

# #TUPLES
# mi_tuple = (1,2,(10,20),3,4)
# mi_tuple = list(mi_tuple)

# print(type(mi_tuple))

# t = (1,2,3)
# x,y,z = t              #tambien se puede ocupar para ver los valores pero deben ser los mismo valores y variables
# print(x.y.z)

# t = (1,2,3,1)
# print(t.count(1))#sirve para contar cunstos valores hay repetidos
# print(t.index(2))#para ver en que valor de indice esta

#SETS
#los sets no se puden repetir por que si repiten no los ocupa, no pudes incluir lista ni dicionarios

# otro_set = {1,2,3}
# print(otro_set)

# mi_set = set((1,2,3,4,5))
# print(type(mi_set))                 #no hay como agregar iten, tampco hay como agregar listas ni dicionarios.
# print(mi_set)             #pero si hay como agregar Tuples
# print(len(mi_set))#para calcular cuantos hay en la lista
# print(2 in mi_set)# para ver si es verdad o falso

# s1 = {1,2,3}
# s2 = {3,4,5}               #para hacer uniones
# s3 = s1.union(s2)
# print(s3)

# s1 = {1,2,3}
# s1.add(4)               #para agregar 
# print(s1)


# s1 = {1,2,3}
# s1.remove(3)               #para elimar
# print(s1)


# s1 = {1,2,3}
# s1.discard(4)               #para descartar un elemento 
# print(s1)


# s1 = {1,2,3}
# s1.pop()               #va eliminnar un elemento alazar 
# print(s1)


# s1 = {1,2,3}
# s1.clear()               #para limpiar un set, se borra todo 
# print(s1)

#BOOLEANOS(VERDADERO O FALSO)
# var1 = True
# var2 = False
# print(type(var1))
# print(var1)

# numero = 5 > 2+3
# print(type(numero))
# print(numero)
# numero = bool(5>6)

# lista = [1,2,3,4]
# control = 5 in lista
# print(control)


