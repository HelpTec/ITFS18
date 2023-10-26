"""para entender los metodos abrstractos tenemos que empezar definiendo que son las interfases.
las mismas son clases con metodos afines a todas las subclases pero que no poseen implementaciòn alguna
es decir, son superclases, con todo lo que las define, pero centradas en el que y no en el como
un ejemplo serìa un control de televisiòn para dos marcas distintas"""

class Control_Remoto():
    volumen = 50
    canal = 10
    def subir_Volumen():
        pass
    def bajar_Volumen():
        pass
    def cambiar_canal():
        pass
    def canal_Anterior():
        pass

class Control_Samsung(Control_Remoto):

    def subir_Volumen(self):
        self.volumen += 1
        print(self.volumen,"+")
    def bajar_Volumen(self):
        self.volumen -= 1
        print(self.volumen,"-")
    def cambiar_Canal(self):
        self.canal += 1
        print(self.canal,"+")
    def canal_Anterior(self):
        if self.canal <= 1:
            print(self.canal)
        else:
            self.canal -= 1
            print(self.canal,"-")

micontrol = Control_Samsung()

micontrol.subir_Volumen()
micontrol.bajar_Volumen()
micontrol.canal_Anterior()
micontrol.cambiar_Canal()
micontrol.canal_Anterior()