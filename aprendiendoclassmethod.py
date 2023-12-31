"""los class method son decoradores que permiten acceder a los metodos de la clase sin crear
instancias de la misma. De hecho estos metodos pueden acceder solo a la clase y no a la instancia
reciben como argumento un cls que es en si la clase."""

class Clase:
    
    saludo = "hola"
    
    @classmethod
    def metododeclase(cls):
        return "metodo de clase", cls
    
    @classmethod
    def cambiarvariable(cls):
        cls.saludo = "chau"
        
print(Clase.metododeclase())

"""esto implica que los metodos de clase no pueden acceder a los atributos de la instancia, pero si
a los de la clase y modificarlos
por lo que entiendo tambien pueden usarse desde el objeto en cuestiòn"""

mi_clase = Clase
print(mi_clase.metododeclase())
print(Clase.saludo)
mi_clase.cambiarvariable()
print(Clase.saludo)

"""aunque confirmo que puede ser accedido por una clase, puedo dar por hecho el que solo sirve
acceder a los metodos de la clase desde un objeto sin instanciar la misma y, creando el class method 
adecuado, pueden modificar atributos de la clase"""

"""un ejemplo de esto"""

class Circulo:
    
    pi= 3.14
    
    @classmethod
    def radio(cls, radio):
        return cls.pi * (radio**2)

resultado = Circulo.radio(2)
print(resultado)

"cabe destacar que un atributo de clase no pasa por un init, eso es algo bastante importante"