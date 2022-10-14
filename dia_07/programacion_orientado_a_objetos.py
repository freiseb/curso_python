#crear clases           
#definir atributos
#definir metodos
#crear objetos

#herencia
#polimorfismo
#cohesion
#abstraccion
#acoplamiento
#encapsulamiento

                            #CLASS
# class Pajaro:
#     pass

# mi_pajaro = Pajaro()
# otro_pajaro = Pajaro()

                            #Atributos 
# class Pajaro:
#     alas = True
    
#     def __init__(self, color, especie):
#         self.color = color
#         self.especie = especie

# mi_pajaro = Pajaro('negro', 'tucan')

# print(mi_pajaro.color) 
# print(Pajaro.alas)
# print(mi_pajaro.alas)

                            #Metodos 
                            
# class Pajaro:
#     alas = True
    
#     def __init__(self, color, especie):
#         self.color = color
#         self.especie = especie
        
#     def piar(self):
#         print('pio, mi color es {}'.format(self.color))
    
#     def volar(self, metros):
#         print(f"El pajaro ha volado {metros} metros")
        
# piolin = Pajaro('amarillo', 'canrio')

# piolin.piar()

                            #TIPOS DE METODOS


# class Pajaro:
#     alas = True
    
#     def __init__(self, color, especie):
#         self.color = color
#         self.especie = especie
        
#     def piar(self):
#         print('pio, mi color es {}'.format(self.color))
    
#     def volar(self, metros):
#         print(f"El pajaro ha volado {metros} metros")
#         self.piar()
    
#     def pintar_negro(self):
#         self.color = 'negro'
#         print(f"Ahora el pajaro es {self.clor}")
    
#     @classmethod
#     def poner_huevos(cls, cantidad ):
#         print(f"Puso {cantidad} huevos")
#         cls.alas = False
#         print(Pajaro.alas)
#     @staticmethod
#     def mirar():
#         print("El pajaro mira")
        
    
# piolin = Pajaro('amarillo', 'canrio')
# Pajaro.poner_huevos(3)
# piolin.piar()

                        #HERENCIA EXTENDIDA

# class Animal:
    
     
#      def __init__(self, edad, color):
#          self.edad = edad
#          self.color = color
    
#      def nacer(self):
#         print("Este animal ha nacido")
    
#      def hablar(self):
#         print("Este animal emite un sonido")
    
# class Pajaro(Animal):
    
#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad, color)
#         self.altura_vuelo = altura_vuelo

#     def hablar(self):
#         print('pio')
        
#     def volar(self,metros):
#         print(f"El pajaro vuela {metros} metros")
    

# piolin = Pajaro(3, 'amarillo', 60)
# mi_animal = Animal(5, 'negro')

# piolin.volar(100)

# ////////////////////////////////////////////////////////////////////////////

# class Padre:
#     def hablar(self):
#         print('hola')
    
# class Madre:
#     def reir(self):
#         print('ja ja ')
        
#     def hablar(self):
#         print('quetal')
        
# class Hijo(Padre, Madre):
#     pass

# class Nieto(Hijo):
#     pass                                
                        
                        
# mi_nieto = Nieto()

# print(Nieto.__mro__)                     
                        
                      
                            #POLIMORFISMO

# class Vaca:
#     def __init__(self, nombre):
#         self.nombre = nombre
    
#     def hablar(self):
#         print(self.nombre + "dice muu")
        
# class Oveja:
#     def __init__(self, nombre):
#         self.nombre = nombre
    
#     def hablar(self):
        
#         print(self.nombre + "dice bee")
              

# vaca1 = Vaca("Aurora")
# oveja1 = Oveja("nuve")

# def animal_habla(animal):
#     animal.hablar()
    
# animal_habla(oveja1)                        

                                    #METODOS ESPECIALES

# class CD:
    
#     def __init__(self, autor, titulo, canciones):
#         self.autor = autor
#         self.titulo = titulo
#         self.canciones = canciones    
    
#     def __str__(self):
#         return f"Album: {self.titulo} de {self.autor}"
    
#     def __len__(self):
#         return self.canciones
    
#     def __del__(self):
#         print("Se ha eliminado el cd")
        

# mi_cd = CD("PINK FLOYD"," The wall",24)

# del mi_cd  #sirve para borrar el 'del'
