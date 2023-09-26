"""Escribe un programa en Python que solicite al usuario que ingrese 5 números enteros. Luego imprimir el máximo
y el mínimo de los valores ingresados. El programa deberá
permitir el ingreso de valores iguales."""

lista = []
for I in range(5):
    lista.append(float(input("Ingrese un numero: ")))
print(f"{max(lista)}")
print(f"{min(lista)}")