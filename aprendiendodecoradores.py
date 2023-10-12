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
    
objeto = Celsius(-10)
print(objeto.afarenheit())

"""tuvimos varios errores basicos de identaciòn, hay que tenerlo en cuenta esto
sin mencionar la falta de atenciòn a la hora de crear objetos de la clase Celsius llamandolos por
nombres que no existian. A tener en cuenta en siguientes estudios"""