"""
Escribe
un programa en
Python que solicite 5 números enteros al usuario. El mismo debe indicar si
entre dichos valores hay números duplicados o no, imprimiendo por pantalla “HAY DUPLICADOS” o “SON TODOS
DISTINTOS”
"""
lista=[]
for i in range(5):
    lista.append(int(input("Ingrese un numero: ")))

comparador=set(lista)

if len(lista) == len(comparador):
    print("SON TODOS DISTINTOS")
else:
    print("HAY DUPLICADOS")