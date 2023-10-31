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

class Control_LG(Control_Remoto):

    def subir_Volumen(self):
        self.volumen += 1
        print(self.volumen,"volumen arriba")
    def bajar_Volumen(self):
        self.volumen -= 1
        print(self.volumen,"volumen abajo")
    def cambiar_Canal(self):
        self.canal += 1
        print(self.canal,"canal siguiente")
    def canal_Anterior(self):
        if self.canal <= 1:
            print(self.canal, "no se puede bajar mas")
        else:
            self.canal -= 1
            print(self.canal,"canal anterior")

micontrolLG = Control_LG()

micontrolLG.subir_Volumen()
micontrolLG.bajar_Volumen()
micontrolLG.canal_Anterior()
micontrolLG.cambiar_Canal()
micontrolLG.canal_Anterior()

"""en sì, las interfaces no cambian de como lo vimos en el sistema de control de capas, son definidas
e implementadas por otra clase, en el sistema de capas las usamos para la capa controladora, aca
por lo visto se usa para otra cosa
en todo caso a esto se le conoce como INTERFACES INFORMALES"""

"""implementar una interfaz como tal puede tener el problema de que no todas las clases implementen
todos los metodos de la misma, ahì es donde entran las INTERFACES FORMALES. Las mismas obligan
a todas las clases que implementan la interfaz a tambien implementar todos sus metodos
esto se logra atraves de importar el modulo ABC"""