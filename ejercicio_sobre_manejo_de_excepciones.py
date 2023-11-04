"""Realiza una función llamada agregar_una_vez(lista, elem) que reciba una lista y
un elemento. La función debe añadir el elemento al final de la lista con la condición
de no repetir ningún elemento. Si este elemento ya se encuentra en la lista se debe
invocar un error de tipo ValueError que debes capturar y mostrar el siguiente
mensaje en su lugar:
“Error: Imposible añadir elementos duplicados => [elemento]”
En una función main() inicializa la lista con: elementos = [1, 5, -2], luego intenta
añadir los siguientes valores a la lista: 10, -2, "Hola". Para finalizar, muestra el
contenido de la lista."""

class ValueError(Exception):
    def __init__(self, elemento, message= "Error: Imposible añadir elementos duplicados"):
        self.elemento = elemento
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f' {self.message} => {self.elemento}'
    
class listaDeElementos:
    def __init__(self):
        self.lista = []
    
    def agregar_una_vez(self, elem):
        if elem not in self.lista:
            self.lista.append(elem)
        else:
            raise ValueError(elem)

def main():
    lista1 = listaDeElementos()
    lista1.lista = [1, 5, -2]
    try:
        lista1.agregar_una_vez(10)
        lista1.agregar_una_vez(-2)
        lista1.agregar_una_vez("Hola")
    finally:
        print(lista1.lista)
main()