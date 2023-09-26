"""Escribir un programa en Python que pida al usuario que ingrese las 
medidas de la base y la altura de un rectángulo y muestre:

1.El perímetro del rectángulo
2.El área del rectángulo"""

print(f"programa en python que pide la base y altura de un rectangulo y muestra perimetro y el area")

base= int(input("Ingrese Base: "))
altura= int(input("Ingrese Altura: "))
print(f"El perímetro del rectángulo es {base*2+altura*2}")
print(f"El area del rectangulo es {base*altura}")