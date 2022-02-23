"""
---------------------- modelo_1_bbdd ---------------------
Este modulo contiene todos los datos de la base de datos,
nos encontramos con 3 clases
Se crean inicialmente dos clases:
    Connection --> la misma es la conexion a la base de datos
    Disconnection --> es la desconecion a la base de datos
Dichas clases serán las clases padres de la clase hija (Crud_Method), 
que contiene las  funciones de: 
Creación, Lectura, Actualización y Borrado de Contacto.
Por último se instancia la clase hija (Crud_Method) para utilizar sus funciones
en el archivo principal "Controlador".
------ importaciones de modulos --------------"""

import sqlite3
from tkinter import messagebox


"------------- clases -------------------------"
"---------------- padres ----------------------"


class Connection:
    def __init__(self):
        pass

    def create_connection(self):
        self.conexion = sqlite3.connect("agenda1.db")
        self.consulta = self.conexion.cursor()


class Disconnection:
    def __init__(self):
        pass

    def close_connection(self):
        self.consulta.close()
        self.conexion.commit()
        self.conexion.close()


"---------------- hija ----------------------"


class Crud_Method(Connection, Disconnection):
    def __init__(self):
        pass

    def create_table(self):
        self.create_connection()
        sql1 = """
        CREATE TABLE IF NOT EXISTS agenda1 ( 
            
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            apellido VARCHAR(255) NOT NULL,
            telefono VARCHAR(255) NOT NULL,
            direccion VARCHAR(255) NOT NULL,
            mail VARCHAR(255) NOT NULL,
            relacion VARCHAR(255) NOT NULL,
            UNIQUE(nombre,apellido)
        )
        """
        if self.consulta.execute(sql1):
            print("Tabla creada")
        else:
            print("Error al crear la tabla")
        self.close_connection()

    def insert_data(self, nombre, apellido, telefono, direccion, mail, relacion):
        self.create_connection()
        datos = (nombre, apellido, telefono, direccion, mail, relacion)
        sql1 = """   
        INSERT INTO agenda1(nombre, apellido, telefono, direccion, 
        mail, relacion) VALUES
        (?,?,?,?,?,?) """
        if self.consulta.execute(sql1, datos):
            print("Datos Guardados")
        else:
            print("Error al guardar los datos")
        self.close_connection()

    def modify_data(self, id, nombre, apellido, telefono, direccion, mail, relacion):
        self.create_connection()
        self.consulta.execute(
            """
        UPDATE agenda1 SET nombre = ?, apellido = ?, telefono = ?, direccion = 
        ?, mail = ? , relacion=?
        WHERE id = ?""",
            (nombre, apellido, telefono, direccion, mail, relacion, str(id)),
        )
        self.close_connection()

    def delete_data(self, id):
        self.create_connection()
        self.consulta.execute("""DELETE from agenda1 WHERE id = """ + str(id))
        self.close_connection()

    def search_data(self, id):
        self.create_connection()
        try:
            self.consulta.execute("SELECT * FROM agenda1 WHERE id= " + str(id))
            for i in self.consulta:
                nombre = i[1]
                apellido = i[2]
                telefono = i[3]
                direccion = i[4]
                mail = i[5]
                relacion = i[6]
                return (nombre, apellido, telefono, direccion, mail, relacion)
            self.close_connection()
        except Exception:
            messagebox.showinfo("Buscar", "Error al buscar")
