def funcion(saludo):
    print(saludo)
    
def contenido():
    return "hola gandini"

funcion(contenido())

variable = contenido

print(variable())

def operacion(funcionnueva, saludo):
    print("prueba")
    funcion(saludo)

operacion(funcion, contenido())

"""funcion a recibe funcion b y retorna funcion c"""

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print("antes de ejecutar")
        resultado = funcion_b(*args, **kwargs)
        print("despues de la funcion")
        return resultado
    return funcion_c

@funcion_a
def hola():
    print("hola desde funciòn saludar")

@funcion_a
def suma(a, b):
    return a + b

print(suma(20, 10))

"""al meter decoradores las funciones hola y suma se ven añadidas a una nueva funcion, la c,
con las propiedades y nuevas funciones que yo necesite añadir"""
