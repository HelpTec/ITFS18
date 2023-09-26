"""Escribir una función que permita calcular 
la duración en segundos de un intervalo dado en horas, minutos y segundos."""



def calcular_segundos():
    horas = int(input("ingrese horas: "))
    minutos = int(input("ingrese minutos: "))
    segundos = int(input("ingrese segundos: "))
    return horas*3600+minutos*60+segundos