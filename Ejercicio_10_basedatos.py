import sqlite3
from os import system

try:
    bd = sqlite3.connect("./empleados.db")
    cursor = bd.cursor()
except sqlite3.OperationalError as error:
	print("Error al abrir la BD.", error)

def crearTabla():
    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
        "id" INTEGER NOT NULL,
        "nro_legajo" INTEGER NOT NULL UNIQUE,
        "dni" INTEGER NOT NULL UNIQUE,
        "nombre" TEXT NOT NULL,
        "apellido" TEXT NOT NULL,
        "area" TEXT NOT NULL,
        PRIMARY KEY ("id" AUTOINCREMENT)
    );''')
    bd.commit()
    print("Tabla creada")

def agregar_empleado(nro_legajo, dni, nombre, apellido, area):
    comando = "INSERT INTO empleados (nro_legajo, dni, nombre, apellido, area) VALUES (?, ?, ?, ?, ?);"
    cursor.execute(comando,(nro_legajo, dni, nombre, apellido, area,))
    bd.commit()

def buscar_por_dni(dni):
    cursor.execute('SELECT * FROM empleados WHERE dni=?', (dni,))
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
    comando= '''DELETE FROM empleados WHERE nro_legajo=?'''
    cursor.execute(comando,(nro_legajo,))
    bd.commit()

def cerrar_programa():
    bd.close()
    return True

def pantalla_Principal():
    print("Ejercicio 10 POO")
    print(10*"=")
    lista_de_opciones=["Crear Tabla", "Ingresar Empleado", "Buscar Empleado Por DNI", "Mostrar Registros", "Modificar Area", "Eliminar Registro", "Salir"]
    nro=1
    for i in (lista_de_opciones):
        print(nro, i)
        nro+=1
        
def main():
    salir = False
    while salir == False:
        system("cls")
        pantalla_Principal()
        opcion = int(input("Ingrese una opciòn: "))
        try:
            match opcion:
                case 1:
                    crearTabla()
                case 2:
                    nro_legajo= int(input("Inserte legajo: "))
                    dni= int(input("Inserte Dni: "))
                    nombre= input("Nombre: ")
                    apellido= input("Apellido: ")
                    area= input("Area: ")
                    agregar_empleado(nro_legajo, dni, nombre, apellido, area)
                case 3:
                    dni= int(input("Inserte DNI: "))
                    buscar_por_dni(dni)
                case 4:
                    mostrar_Registros()
                case 5:
                    nro_legajo= int(input("Inserte legajo: "))
                    area= input("Ingrese area nueva: ")
                    modificar_area(nro_legajo, area)
                case 6:
                    nro_legajo= int(input("Inserte legajo a eliminar: "))
                    eliminar_Por_Legajo(nro_legajo)
                case 7:
                    salir = cerrar_programa()
                case _:
                    print("opciòn invalida")
                    input("")
        except TypeError:
            print("Elija una opciòn numerica")

main()
