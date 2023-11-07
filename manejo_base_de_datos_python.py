import sqlite3

try:
    #Creamos la conexión a la Base de Datos
    bd = sqlite3.connect("./base_de_datos.db")
    print("Base de datos abierta")
    #Con el cursor ya podemos interactuar completamente
    cursor = bd.cursor()

    # Una vez se tenga una Connection, se puede crear un objeto Cursor y llamar su método execute() para ejecutar comandos SQL:
    # Crear una tabla
    cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
        "id"	INTEGER NOT NULL,
        "titulo"	TEXT NOT NULL,
        "autor"	TEXT NOT NULL,
        "genero"	TEXT NOT NULL,
        "precio"	REAL NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );''')
    print("La tabla se ha creado correctamente")

    # Insertar un registro a la tabla
    cursor.execute('''INSERT INTO libros (titulo,autor,genero,precio)
        VALUES
        ('Cementerio de animales','Stephen King', 'Terror', 1550),
        ('Las estrellas, mi destino','Alfred Bester', 'Ciencia ficción', 2000),
        ('El cuento de la criada','Margaret Atwood', 'Ciencia ficción', 1850);'''
    )
    print("Los nuevos registros se han insertado correctamente")

    # Guardar (commit) los cambios
    bd.commit()
    print("Se han guardado los cambios correctamente")

    #Mostrar todos los registros por consola
    cursor.execute('SELECT * FROM libros ORDER BY id')
    print(cursor.fetchall())

    # Se recomienda cerrar la conexión a la BD si hemos terminado.
    # Solo debemos asegurarnos de que se hayan aplicado los cambios o se perderán.
    bd.close()
    print("Se ha cerrado la conexión a la BD")
except sqlite3.OperationalError as error:
	print("Error al abrir la BD.", error)