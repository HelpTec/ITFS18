from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    def __init__(self, colorFondo: str, colorBorde: str):
        self.colorFondo = colorFondo
        self.colorBorde = colorBorde

    @property
    def colorFondo(self):
        return self.__colorFondo
    @colorFondo.setter
    def colorFondo(self, value):
        self.__colorFondo = value

    @property
    def colorFondo(self):
        return self.__colorFondo
    @colorFondo.setter
    def colorFondo(self, value):
        self.__colorFondo = value

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimetro():
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, colorFondo: str, colorBorde: str, base: float, altura: float):
        super().__init__(colorFondo, colorBorde)
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self, value):
        self.__base = value

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, value):
        self.__altura = value

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def perimetro(self) -> float:
        return 0

class Circulo(FiguraGeometrica):
    def __init__(self, colorFondo: str, colorBorde: str, radio: float):
        super().__init__(colorFondo, colorBorde)
        self.radio = radio

    @property
    def radio(self):
        return self.__radio
    @radio.setter
    def radio(self, value):
        self.__radio = value

    def area(self) -> float:
        return math.pi * math.pow(self.radio, 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Rectangulo(FiguraGeometrica):
    def __init__(self, colorFondo: str, colorBorde: str, base: float, altura: float):
        super().__init__(colorFondo, colorBorde)
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self, value):
        self.__base = value

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, value):
        self.__altura = value

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return self.base * 2 + self.altura * 2

"""pruebas varias"""
def main():
    mi_rectangulo = Rectangulo("negro", "blanco", 3, 5)
    un_circulo = Circulo("azul", "amarillo", 20)
    ya_no_juego_mas = Triangulo("rojo", "verde", 5, 20)

    figurasGeometricas = [mi_rectangulo, un_circulo, ya_no_juego_mas,]

    for i in figurasGeometricas:
        print(f"El area de un {type(i)} es: {i.area()}")
        print(f"El perimetro  de un {type(i)} es: {i.perimetro()}")


if __name__ == "__main__":
    main()