import abc
from datetime import datetime
from datetime import date
"""
saldo = 10
monto = 10

def probador(saldo, monto):
    movimientos=[]
    saldo += monto
    fecha= datetime.now()
    movimiento = (fecha, monto, saldo)
    movimientos.append(movimiento)
    print (movimientos)
    enter=input()
    
for i in range(10):
    probador(saldo, monto)
"""
class CuentasBancarias:
    def __init__(self, nro_cuenta, cbu, alias, saldo) -> None:
        self.nro_cuenta = nro_cuenta
        self.cbu = cbu
        self.alias = alias
        self.saldo = saldo
        self.movimientos=[]
    
    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            fecha= datetime.now()
            movimiento = (fecha,"deposito", monto, self.saldo)
            self.movimientos.append(movimiento)
            return True
        else:
            return False
    
    def extraer(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            fecha= datetime.now()
            movimiento = (fecha, "extracciòn", monto, self.saldo)
            self.movimientos.append(movimiento)
            return True
    
    def transferir(self, monto, cuenta_destino):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            fecha= datetime.now()
            movimiento = (fecha, "transferencia", monto, self.saldo)
            self.movimientos.append(movimiento)
            return True
            
class CajaDeAhorro(CuentasBancarias):
    def __init__(self, monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles, cant_transferencias_disponibles):
         

class CuentaCorriente(CuentasBancarias):
    pass

class Cliente:
    lista= []

class Banco:
    lista= []
