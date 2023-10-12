"""uso de decorador @property para objetos en python
hace que el uso getters y setters sea mas facil
ejemplos
"""
class Celsius:
    #inicializamos la clase
    def __init__(self, temperatura=0):
        self.temperatura = temperatura
        
    #agregamos un metodo
    def afarenheit(self):
        return (self.temperatura * 1.8) + 32
    
    #usamos el decorador property
    @property
    def temperatura(self):
        print("obteniendo temperatura...")
        return self.__temperatura
    
    #ahora que decoramos al metodo temperatura con el property
    #declaramos un setter con un decorador para agregar el metodo
    @temperatura.setter
    def temperatura(self, value):
        print("asignando valor... ")
        if value < -237.35:
            raise ValueError("la temperatura por debajo de -237 no es posible")
        self.__temperatura = value
    
objeto = Celsius()
print(objeto.temperatura)
objeto.temperatura = 10
print(objeto.temperatura)
print(objeto.afarenheit())

"""tuvimos varios errores basicos de identaciòn, hay que tenerlo en cuenta esto
sin mencionar la falta de atenciòn a la hora de crear objetos de la clase Celsius llamandolos por
nombres que no existian. A tener en cuenta en siguientes estudios"""

"""en resumen, el decorador property se encarga de manejar los atributos de clases de una manera
mas prolija y eficiente implementando la protecciòn de atributos de clases que python no tiene
por su cuenta y otros lenguajes si.
Sumado a que el decorador property ya tiene per se en sus argumentos las funciones get, set y del
que terminan por ser llamadas y asignadas automaticamente por el programa al simplemente usar
las funciones de objeto.atributo para el getter, objeto.atributo = valor para el setter y del,
correspondientemente, sin necesidad de usar los parentesis ni crear metodos de codigo largo
para manejar getters y setters que sin el propertys no funcionarian como se supone que lo harìan"""