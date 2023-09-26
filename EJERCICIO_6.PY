"""Usando la función del ejercicio anterior, escribir un programa que pida al usuario 
dos intervalos expresados en horas, minutos y segundos, 
sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos"""

from EJERCICIO_5 import *

print("mensaje de prueba")
intervalo_1 = calcular_segundos()
intervalo_2 = calcular_segundos()

print(intervalo_1+intervalo_2)
segundos = (intervalo_1+intervalo_2)%60
minutos = (intervalo_1+intervalo_2)//60
horas = (intervalo_1+intervalo_2)//3600



print(f"la duraciòn total en horas, minutos y segundos es: {horas}:{minutos%60}:{segundos}")