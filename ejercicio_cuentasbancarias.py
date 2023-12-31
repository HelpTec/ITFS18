from abc import ABC, abstractmethod
from datetime import datetime
from datetime import date
import random

def generador_de_numeros():
        nro_de_cuenta = random.randint(1000000000000, 9999999999999)
        entidad= random.randint(100, 999)
        sucursal= random.randint(1000, 9999)
        verificador= random.randint(0,1)
        cbu = f"{entidad}{sucursal} - {nro_de_cuenta} - {verificador}"
        saldo = random.randint(0,10000)
        resultado= [nro_de_cuenta, cbu, saldo]
        return resultado

def alias_generador():
    lista_de_palabras = ["nieta", "gorra", "maceta", "campera", "celular", "sombrero", "sol", "lava", "dulce", "volcan", "arroz", "cebolla", "mercado", "chipa"]
    alias= f"{random.choice(lista_de_palabras)}.{random.choice(lista_de_palabras)}.{random.choice(lista_de_palabras)}"
    return alias
class CuentasBancarias(ABC):
    def __init__(self, atributos, alias):
        self.__nro_cuenta, self.__cbu, self.__saldo = atributos
        self.__alias = alias 
        self.__movimientos=[]
    
    @property
    def nro_cuenta(self):
        return self.__nro_cuenta
    @nro_cuenta.setter
    def nro_cuenta(self, valor):
        self.__nro_cuenta = valor
    
    @property
    def cbu(self):
        return self.__cbu
    
    @cbu.setter
    def cbu(self, valor):
        self.__cbu = valor
    
    @property
    def alias(self):
        return self.__alias
    
    @alias.setter
    def alias(self, valor):
        self.__alias = valor
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
    
    @property
    def movimientos(self):
        return self.__movimientos
    
    @movimientos.setter
    def movimientos(self, valor):
        self.__movimientos = valor

    def consultar_saldo(self):
        return self.__saldo
    
    def depositar(self, monto_a_depositar):
        if monto_a_depositar > 0:
            self.saldo += monto_a_depositar
            tipo = "deposito"
            self.registrar(tipo, monto_a_depositar)
            return True
        else:
            return False
    
    def registrar(self, tipo, monto):
        movimiento = (datetime.now(), tipo, monto, self.saldo)
        self.__movimientos.append(movimiento)

    @abstractmethod
    def extraer(self, monto_a_extraer):
        pass

    @abstractmethod
    def transferir(self, monto_a_transferir, cuenta_destino):
        pass

class CajaDeAhorro(CuentasBancarias):
    def __init__(
        self, atributos, alias,
        monto_limite_extracciones, monto_limite_transferencias,
        cant_extracciones_disponibles, cant_transferencias_disponibles):
        super().__init__(atributos, alias)
        self.monto_limite_extracciones = monto_limite_extracciones
        self.monto_limite_transferencias = cant_transferencias_disponibles
        self.cant_extracciones_disponibles = cant_extracciones_disponibles
        self.cant_transferencias_disponibles = cant_transferencias_disponibles

    def extraer(self, monto_a_extraer):
        if (monto_a_extraer > 0
            and monto_a_extraer <= self.saldo
            and monto_a_extraer <= self.monto_limite_extracciones
            and self.cant_extracciones_disponibles > 0):
            self.saldo -= monto_a_extraer
            tipo = "extraer"
            self.registrar(tipo, monto_a_extraer)
            return True

    def transferir(self, monto_a_transferir, cuenta_destino):
        print(monto_a_transferir)
        input("monto a transferir")
        print(self.monto_limite_transferencias)
        input("Monto limite transferencias")
        if (monto_a_transferir > 0
            and monto_a_transferir <= self.saldo
            and monto_a_transferir <= self.monto_limite_transferencias):
            self.saldo -= monto_a_transferir
            cuenta_destino.depositar(monto_a_transferir)
            input("transferencia exitosa")
            print(cuenta_destino.consultar_saldo())
            input()
            fecha= datetime.now()
            tipo = "transferir"
            self.registrar(tipo, monto_a_transferir)
            return True
        else:
            input("algo salio mal")

class CuentaCorriente(CuentasBancarias):
    def __init__(
        self, atributos, alias,
        monto_maximo_descubierto):
        super().__init__(atributos, alias)
        self.monto_maximo_descubierto = monto_maximo_descubierto
    
    def extraer(self, monto_a_extraer):
        if (monto_a_extraer > 0
            and monto_a_extraer <= self.monto_maximo_descubierto + self.saldo):
            self.saldo -= monto_a_extraer
            tipo = "extracciòn"
            self.registrar(self, tipo, monto_a_extraer)
            return True
    
    def transferir(self, monto_a_transferir, cuenta_destino):
        if (monto_a_transferir > 0
            and monto_a_transferir <= self.monto_maximo_descubierto + self.saldo):
            self.saldo -= monto_a_transferir
            cuenta_destino.depositar(monto_a_transferir)
            input("transferencia exitosa")
            print(cuenta_destino.consultar_saldo())
            input()
            fecha= datetime.now()
            tipo = "transferir"
            self.registrar(self, tipo, monto_a_transferir)
            return True
        else:
            input("algo salio mal")

class Cliente:
    
    def __init__(self, razon_social, cuit, tipo_de_persona, domicilio):
        self.__razon_social = razon_social
        self.__cuit = cuit
        self.__tipo_de_persona = tipo_de_persona
        self.__domicilio = domicilio
        self.__cuentas_bancarias = []
    
    @property
    def razon_social(self):
        return self.__razon_social
    
    @razon_social.setter
    def razon_social(self, __razon_social):
        self.__razon_social = __razon_social
    
    @property
    def cuit(self):
        return self.__cuentas_bancarias
    @cuit.setter
    def cuit(self, valor):
        self.__cuit = valor
    
    @property
    def tipo_de_persona(self):
        return self.__tipo_de_persona
    @tipo_de_persona.setter
    def tipo_de_persona(self, valor):
        self.__tipo_de_persona = valor

    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self, valor):
        self.__domicilio = valor

    @property
    def cuentas_bancarias(self):
        return self.__cuentas_bancarias
    @cuentas_bancarias.setter
    def cuentas_bancarias(self, valor):
        self.__cuentas_bancarias= valor

    def crear_nueva_cuenta_bancaria(self, atributos, alias, tipo_de_cuenta):
        if tipo_de_cuenta == 1:
            if self.__tipo_de_persona == 1:
                monto_limite_extracciones = 100000000
                monto_limite_transferencias = 100000000
                cant_extracciones_disponibles = 10000000
                cant_transferencias_disponibles = 100000000
                nueva_cuenta = CajaDeAhorro(atributos, alias, monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles, cant_transferencias_disponibles)
                self.cuentas_bancarias.append(nueva_cuenta)
            elif self.__tipo_de_persona == 2:
                monto_limite_extracciones = 1000000
                monto_limite_transferencias = 1000000
                cant_extracciones_disponibles = 1000000
                cant_transferencias_disponibles = 10000000
                nueva_cuenta = CajaDeAhorro(atributos, alias, monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles, cant_transferencias_disponibles)
                self.cuentas_bancarias.append(nueva_cuenta)
            else:
                input("algo salio mal")
        elif tipo_de_cuenta == 2:
            if self.__tipo_de_persona == 1:
                monto_maximo_descubierto = 5000
                nueva_cuenta= CuentaCorriente(atributos, alias, monto_maximo_descubierto)
                self.cuentas_bancarias.append(nueva_cuenta)
            elif self.__tipo_de_persona == 2:
                monto_maximo_descubierto = 10000
                nueva_cuenta= CuentaCorriente(atributos, alias, monto_maximo_descubierto)
                self.cuentas_bancarias.append(nueva_cuenta)
        else:
            input("Algo salio mal")

class Banco:
    def __init__(self, nombre, domicilio):
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__clientes = []

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, valor):
        self.__clientes = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def domicilio(self):
        return self.__domicilio

    @domicilio.setter
    def domicilio(self, valor):
        self.__domicilio = valor

    def crear_nuevo_cliente(self, cliente_nuevo):
        self.clientes.append(cliente_nuevo)
        return True

def main():
    banco_nuevo = Banco("Santander Rio", "Buenos Aires")
    Leo = Cliente("Leo Messi", 20333333338, 2, "Rosario")
    McGuiver = Cliente("Mc Guiver", 20444444448, 1, "Estados Unidos")
    Limon = Cliente("Limon", 20555555558, 1, "San Martin")
    banco_nuevo.crear_nuevo_cliente(Leo)
    banco_nuevo.crear_nuevo_cliente(McGuiver)
    banco_nuevo.crear_nuevo_cliente(Limon)
    atributos = generador_de_numeros()
    alias = alias_generador()
    Leo.crear_nueva_cuenta_bancaria(atributos, alias, 1)
    Leo.crear_nueva_cuenta_bancaria(atributos, alias, 2)
    caja_ahorro_Leo = Leo.cuentas_bancarias[0]
    cuenta_Corriente_Leo = Leo.cuentas_bancarias[1]
    atributos = generador_de_numeros()
    alias = alias_generador()
    McGuiver.crear_nueva_cuenta_bancaria(atributos, alias, 1)
    McGuiver.crear_nueva_cuenta_bancaria(atributos, alias, 2)
    caja_ahorro_McGuiver = McGuiver.cuentas_bancarias[0]
    cuenta_Corriente_McGuiver = McGuiver.cuentas_bancarias[1]
    atributos = generador_de_numeros()
    alias = alias_generador()
    Limon.crear_nueva_cuenta_bancaria(atributos, alias, 1)
    Limon.crear_nueva_cuenta_bancaria(atributos, alias, 2)
    caja_ahorro_Limon = Limon.cuentas_bancarias[0]
    cuenta_Corriente_Limon = Limon.cuentas_bancarias[1]

#simulacion de transacciones  
    caja_ahorro_Leo.depositar(2000)
    cuenta_Corriente_Leo.depositar(5000)
    caja_ahorro_Leo.extraer(1000)
    caja_ahorro_Leo.transferir(2000, caja_ahorro_Limon)

if __name__ == "__main__":
    main()
