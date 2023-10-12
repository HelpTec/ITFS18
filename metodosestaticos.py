"""basicamente funcionan como los de clase pero tienen algunos impedimentos
- no pueden modificar atributos de clase ni de instancia
- no pueden modificar tampoco los estados de la clase ni los de la instancia"""

class Circulo:
    
    pi= 3.14
    
    @staticmethod
    def radio(radio):
        return Circulo.pi * (radio**2)

resultado = Circulo.radio(2)
print(resultado)

"""a tener en cuenta que:
-no accede ni a los self ni a los cls, por ende no se ponen
-basicamente funcionan como metodos y comparten el namespace de la clase, por ende SE LO LLAMA con el
nombre de la clase directamente.
- cuando se arma el metodo se pone solo el argumento que va a recibir, nada mas, no recibe argumento
de clase, a su ves, repito, no usa ni cls ni self, esto probablemnte sea una trampa del examen"""