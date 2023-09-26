"""Crear una clase llamada Persona.
Con los siguientes atributos privados:
•nombre
•edad
•dni
Y los siguientes métodos:
•mostrar_edad(): retorna la edad de la persona
•es_mayor_edad(): retorna True si edad es mayor o igual a 18, o False si es menor a 18.

El método constructor __init__ de la clase debe recibir y asignar los valores a cada uno de
los atributos privados de la clase."""

class persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    def mostrar_edad(self):
        return self.__edad
    def es_mayor_edad(self):
        return self.__edad >= 18
    
diego = persona("diego", 17, 22334455)

print(diego.mostrar_edad())
print(diego.es_mayor_edad())