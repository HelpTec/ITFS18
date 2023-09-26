import random

class Password:
    __LONGITUD = 8
    __CARACTERES_VALIDOS= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    def __init__(self, longitud= __LONGITUD):
        if longitud >= 6 & longitud <= 15:
            self.__longitud = longitud
        else:
            print("invalido")
        self.__contrasena = self.generarPassword()

    def getcontrasena(self):
        return self.__contrasena
    def getlongitud(self):
        return self.__longitud

    def esFuerte(self):
        minus = 0
        num = 0
        charEsp = 0
        mayus = 0
        for char in self.__contrasena:
            if char.isupper():
                mayus += 1
            if char.islower():
                minus += 1
            if char in "<=>@#%&+":
                charEsp += 1
            if char.isdigit():
                num += 1
        if num > 1 and mayus >= 1 and minus > 1 and charEsp >= 1:
            return True
        else:
            return False 
    def generarPassword(self):
        return ''.join(random.choice(Password.__CARACTERES_VALIDOS) for i in range(self.__longitud))

mi_lista = []
for i in range(3):
    longitud = int(input("Ingrese longitud: "))
    if longitud  <= 0 or None:
        mi_lista.append(Password())
    else:
        mi_lista.append(Password(longitud))
print (mi_lista)

for i in range(3):
    print(mi_lista[i].esFuerte())
for i in range(3):
    print(mi_lista[i].getcontrasena())