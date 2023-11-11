import abc
from datetime import datetime
from datetime import date
import random

class CuentasBancarias(abc):
    def __init__(self, nro_cuenta, cbu, alias, saldo):
        self.nro_cuenta = nro_cuenta
        self.cbu = cbu
        self.alias = alias
        self.saldo = saldo
        self.movimientos=[]
    
    def registrar(self, tipo, monto):
        movimiento = (datetime.now(), tipo, monto, self.saldo)
        self.movimientos.append(movimiento)
    
    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, monto_a_depositar):
        if monto_a_depositar > 0:
            self.saldo += monto_a_depositar
            tipo = "deposito"
            self.registrar(self, tipo, monto_a_depositar)
            return True
        else:
            return False

    @abstractmethod
    def extraer(self, monto_a_extraer):
        pass

    @abstractmethod
    def transferir(self, monto_a_transferir, cuenta_destino):
        pass

class CajaDeAhorro(CuentasBancarias):
    def __init__(
        self, nro_cuenta, cbu, alias, saldo,
        monto_limite_extracciones, monto_limite_transferencias,
        cant_extracciones_disponibles, cant_transferencias_disponibles):
        super().__init__(nro_cuenta, cbu, alias, saldo)
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
            self.registrar(self, tipo, monto_a_extraer)
            return True

    def transferir(self, monto_a_transferir, cuenta_destino):
        if (monto_a_transferir > 0
            and monto_a_transferir <= self.saldo
            and monto_a_transferir <= self.monto_limite_extracciones):
            self.saldo -= monto_a_transferir
            fecha= datetime.now()
            tipo = "transferir"
            self.registrar(self, tipo, monto_a_transferir)
            return True

class CuentaCorriente(CuentasBancarias):
    def __init__(
        self, nro_cuenta, cbu, alias, saldo,
        monto_maximo_descubierto):
        super().__init__(self, nro_cuenta, cbu, alias, saldo)
        self.monto_maximo_descubierto = monto_maximo_descubierto
    
    def extraer(self, monto_a_extraer):
        if (monto_a_extraer > 0
            and monto_a_extraer <= self.monto_maximo_descubierto + self.saldo):
            self.saldo -= monto_a_extraer
            tipo = "extracciòn"
            self.registrar(self, tipo, monto_a_extraer)
            return True

class Cliente:
    lista= []
    def __init__(self, razon_social, cuit, tipo_de_persona, domicilio):
        self.__razon_social = razon_social
        self.__cuit = cuit
        self.__tipo_de_persona = tipo_de_persona
        self.__domicilio = domicilio
        self.__cuentas_bancarias = []
    
    def crear_nueva_cuenta_bancaria():
        while True:
            try:
                tipo_de_cuenta = int(input("Indique tipo de cuenta bancaria: Presione 1 para ºCaja de Ahorroº o 2 para ºCuenta Corrienteº"))
                if tipo_de_cuenta == 1:
                    nro_de_cuenta = random.randint(1000000000000, 9999999999999)
                    entidad= random.randint(100, 999)
                    sucursal= random.randint(1000, 9999)
                    verificador= random.randint(0,1)
                    cbu = f"{entidad}{sucursal} - {nro_de_cuenta} - {verificador}"
                    
                elif tipo_de_cuenta == 2:
                    
                else:
                    print("Por favor seleccione la opciòn deseada disponible")
                    input()
            except ValueError:
                print("Solo valores numericos porfavor")
class Banco:
    lista= []
