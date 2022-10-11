#ejem
# dic = {'clave1':100, 'clave2':500}
# a  = dic.popitem()
# print(a)
# print(dic)
# str = ",:_#,,,,,,:::____##Pyton_ _Total,,,,,,::#"
# print(str.lstrip((', : % _ #,[(, # :)]')))
    #CREAR FUNCIONES 
#ejem
# def saludar_persona(nombre):
#     print('hola'nombre)

# saludar_persona('ferando')     

    #RETURN
#eje
# def multiplicar(numero1, numero2):

#     return numero1 * numero2
# resultado = multiplicar(5, 10)
# print(resultado)
    
# def invertir_palabra(mayuscula):
#     return mayuscula.upper()
# palabra = invertir_palabra("python"[ : : -1])
# print(palabra)

    #FUNCIONES DINAMICAS
#EJEM
# def chequear_3_cifras(numero):

#     return numero in range(100,1000)

# suma = 567 + 402 
# resultado = chequear_3_cifras(suma)
# print(resultado)

# def chequear_3_cifras(lista):
#     for n in lista:
#         if n in range(100, 1000):
#             return True
#         else:
#             pass
#     return False
# resultado = chequear_3_cifras([443, 5,222])
# print(resultado)


# def chequear_3_cifras(lista):
#     lista_3_cifras = []
#     for n in lista:
#         if n in range(100, 1000):
#             lista_3_cifras.append(n)
#         else:
#             pass
#     return lista_3_cifras
# resultado = chequear_3_cifras([443, 5,222])
# print(resultado)


        #EJEMPLOS DE FUNCION
# precios_cafe = [('capuchino',1.5),('Expreso',1.2),('Moka',1.9)]

# def cafe_mas_caro(lista_precios):
#     precio_mayor = 0
#     cafe_mas_caro = ''
    
#     for cafe, precio in lista_precios:
#         if precio > precio_mayor:
#             precio_mayor = precio
#             cafe_mas_caro = cafe
#         else:
#             pass
#     return(cafe_mas_caro, precio_mayor)
# cafe, precio = cafe_mas_caro(precios_cafe)
# print(f'El cafe mas caro es {cafe} cuyo precio es {precio}')

        #INTERACCION ENTRE FUNCIONES
from random import shuffle

#lista inicial
palitos = ['-', '--','---','----']
#mezclar palos
def mezlcar(lista):
    shuffle(lista)
    return lista
#pedirle intento
def probar_suerte():
    inteto = ''
    while inteto not in ['1','2', '3', '4']:
        inteto = input("Elige un numero del 1 al 4: ")
    return int(inteto)
#Comprobar intento
def chequear_intento(lista, inteto):
    if lista[inteto -1] == '-':
        print("A lavar los platos")
    else:
        print("Esta ves te has salvado")
    print(f'Te ha tocado {lista[inteto-1]}')


palitos_mezclados = mezlcar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)
    #ARGUMENTOS INDENTIFICADOS(*args)
def suma(**args):
    total = 0
    for arg in args:  #return sum(args) asi tambien hya como hacer para no hacer muy largo la linea
        total += arg
    return total 
print(suma(6,5,5,4,8))
    #ARGUMENTOS INDEFINIDOS(**kwargs)
def suma(**kwargs):
    total = 0 
    for clave, valor in kwargs.items():
        print(f"{Clave} = {valor}")
        total += valor
         
suma(x=3, y=5, z=2)


def suma(num1, num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")
    
    for arg in args:
        print(f"arg = {arg}") 
    for clave, valor in kwargs.items():
        print(f"{Clave} = {valor}")

args = [100, 200, 300, 400]
kwargs = {x="uno", y="dos", z="tres"}        
        
        
prueba(15,50, *args, **kwargs )

    