class ListaDeTareas:
    def __init__(self):
        self.__lista_tareas = []
    def agregarTarea(self, tarea):
        self.__lista_tareas.append(tarea)
        if tarea == self.__lista_tareas[-1]:
            print("Tarea agregada correctamente a la lista")
        else:
            print("La tarea no fue agregada a la lista")
    def quitarTarea(self, tarea):
        encontrados = self.__lista_tareas.count(tarea)
        if encontrados <= 0:
            print("No existe la tarea en la lista")
        else:
            for i in range(encontrados):
                self.__lista_tareas.remove(tarea)
            if tarea in self.__lista_tareas:
                print("La tarea no fue eliminada a la lista")
            else:
                print("La tarea fue eliminada de la lista")
    def mostrarTarea(self):
        return self.__lista_tareas
    
lista1 = ListaDeTareas()

for i in range(2): 
    lista1.agregarTarea("prueba")

lista1.quitarTarea("prueba")
lista1.quitarTarea("casa")
lista1.agregarTarea("ropa")
print(lista1.mostrarTarea())