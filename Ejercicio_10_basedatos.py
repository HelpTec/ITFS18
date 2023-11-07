import sqlite3
from os import system

try:
    bd = sqlite3.connect("./empleados.db")
    print("Base de datos creada")
    cursor = bd.cursor()
except sqlite3.OperationalError as error:
	print("Error al abrir la BD.", error)

def crearTabla():
    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "nro_legajo" INT NOT NULL UNIQUE,
        "dni" int NOT NULL UNIQUE,
        "nombre" text NOT NULL,
        "apellido" text NOT NULL,
        "area" text NOT NULL
    );''')
    bd.commit()
    print("Tabla creada")

def agregar_empleado(id, nro_legajo, dni, nombre, apellido, area):
    comando = "INSERT INTO empleados (id, nro_legajo, dni, nombre, apellido, area) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(comando,[id, nro_legajo, dni, nombre, apellido, area])
    bd.commit()

def buscar_por_dni(dni):
    comando = '''SELECT * FROM empleados WHERE dni=?;'''
    cursor.execute(comando,(dni))
    print(cursor.fetchall())
    input("precione enter para continuar")

def mostrar_Registros():
    sentencia = '''SELECT * FROM empleados ORDER BY id;'''
    for i in cursor.execute(sentencia):
        print(i)
    input("presione enter para seguir")

def modificar_area(nro_legajo, area):
    comando= '''UPDATE empleados SET area=? WHERE nro_legajo=?'''
    cursor.execute(comando,(area, nro_legajo))

def eliminar_Por_Legajo(nro_legajo):
    comando= '''DELETE * FROM empleados WHERE nro_legajo=?'''
    cursor.execute(comando,(nro_legajo))
    bd.commit()

def cerrar_programa():
    bd.close()
    return True

def main():
    salir = False
    while salir == False:
        system("cls")
        print("Ejercicio 10")
        opcion = int(input("Ingrese una opciòn: "))
        try:
            if opcion == 1:
                crearTabla()
            elif opcion == 2:
                nro_legajo= int(input("Inserte legajo: "))
                dni= int(input("Inserte Dni: "))
                nombre= input("Nombre: ")
                apellido= input("Apellido: ")
                area= input("Area: ")
                agregar_empleado(nro_legajo, dni, nombre, apellido, area)
            elif opcion == 3:
                dni= int(input("Inserte DNI: "))
                buscar_por_dni(dni)
            elif opcion == 4:
                mostrar_Registros()
            elif opcion == 5:
                nro_legajo= int(input("Inserte legajo: "))
                area= input("Ingrese area nueva: ")
                modificar_area(nro_legajo, area)
            elif opcion == 6:
                nro_legajo= int(input("Inserte legajo a eliminar: "))
                eliminar_Por_Legajo(nro_legajo)
            elif opcion == 7:
                salir = cerrar_programa()
            else:
                print("opciòn invalida")
                input("")
        except TypeError:
            print("Elija una opciòn numerica")

main()
