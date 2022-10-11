from os import setsid


#str es un string(texto)
#int es un integer(numeros)
#float es un floating(decimales)
# list es listas
#dic es diccionarios 
#tuple es tuples
# set es sets
#bool booleanos(es verdadero o falso)

# integers(enteros
#ejem
mi_entero = 1
print(mi_entero) 

print(type(mi_entero))

#floats(decimales)
mi_decimal = 2.5
print(mi_decimal)
print(type(mi_decimal))


#ejemplos de varianbles

nombre = "juan"
print(nombre)
edad = 30
print(edad) 




#COMVERSIONES ejem
num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))


#ejem2
edad = input("dime tu edad: ")
edad = int(edad)
nueva_edad = 1 + edad
print(nueva_edad)


#FORMATIAR CADENAS
#EJEM
x = 10
y = 5

print ("mis numeros son {} y {}".format(x,y))


color = "rojo"
matricula = 421451

print(f"EL auto es {color} y su matricula {matricula}")

#OPERACIONES
#EJEM
x = 6
y = 2

print(f"{x} mas {y} es igual a {x+y}")



#round(REDONDEO)
#EJEM round(22.231313, 2) = 22.23
valor = round(95.666666666666,2)

print(valor)
valor1 = 95.666666666666
print(round(valor))



