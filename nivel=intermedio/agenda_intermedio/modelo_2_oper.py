"""
------------modelo_2_oper------------------
Este modulo es especificamente para definir la operacion que tendran los 
botones del modulo 'vista'
------------ funciones -----------------------
1.___init___() ---> en el mismo se define los variables
2.mensaje ---> configura la funcion mensaje de tkinter
3.limpiar elemento---> limpia en tkinter los Entry si tienen elementos dentro
4.listar---> lista los contactos que hay en la base de datos para visualizarlos
5.borrar---> nos permite eliminar un contacto existente en nuestra base de datos
6.buscar---> nos permite buscar contactos en la base de datos
7.modificar--> nos permite modificar contactos ya existentes
8.guardar---> nos permite guardar un nuevo contacto
"""

import modelo_3_valid as val
import re
from modelo_1_bbdd import Crud_Method
from tkinter import messagebox
import sqlite3

"------ importaciones de modulos --------------"

"------------- clases -------------------------"


class Modelo:
    "-------------------------1-------------------------------"

    def __init__(self, ID, nombre, apellido, telefono, direccion, mail, relacion):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mail = mail
        self.relacion = relacion

    "-------------------------2-------------------------------"

    def mensaje(self, titulo, texto):
        self.titulo = titulo
        self.texto = texto
        messagebox.showinfo(self.titulo, self.texto)

    "-------------------------3-------------------------------"

    def limpiar_element(self):
        self.ID.set("")
        self.nombre.set("")
        self.apellido.set("")
        self.telefono.set("")
        self.direccion.set("")
        self.mail.set("")
        self.relacion.set("")

    "-------------------------4-------------------------------"

    def listar(self):

        listado = []

        if len(listado) > 0:

            listado.clear()  # Borra lo que haya en la lista
        self.conexion = sqlite3.connect("agenda1.db")
        self.consulta = self.conexion.cursor()
        self.consulta.execute(
            "SELECT id, nombre, apellido, telefono, direccion, mail, relacion from agenda1"
        )
        for i in self.consulta:
            listado.append(i)  # Agrego lo que obtuve a una lista vacia
            listado.sort()  # Ordeno la lista
        self.conexion.close()
        return listado

    "-------------------------5-------------------------------"

    def borrar(
        self,
        ID,
        nombre=None,
        apellido=None,
        telefono=None,
        direccion=None,
        mail=None,
        relacion=None,
    ):
        try:
            self.id = ID.get()
            if self.id == "":
                self.mensaje("Borrar", "Debes insertar el ID que deseas modificar")
            else:

                crud = Crud_Method()
                crud.delete_data(self.id)
                self.limpiar_element()
                self.listar()
                self.mensaje("Borrar", "Contacto Borrado")
        except Exception:

            self.mensaje("Error", "Error al borrar, inserta código")

    "-------------------------6-------------------------------"

    def buscar(
        self,
        ID,
        nombre=None,
        apellido=None,
        telefono=None,
        direccion=None,
        mail=None,
        relacion=None,
    ):
        try:
            self.id = ID.get()
            if self.id == "":
                self.mensaje("Buscar", "Inserta Identificador")
            else:
                crud = Crud_Method()
                tupla = crud.search_data(self.id)
                self.nombre.set(tupla[0])
                self.apellido.set(tupla[1])
                self.telefono.set(tupla[2])
                self.direccion.set(tupla[3])
                self.mail.set(tupla[4])
                self.relacion.set(tupla[5])
                self.mensaje("Buscar", "Contacto encontrado")
        except Exception:
            self.mensaje("Error", "Error al buscar, inserta Identificador")

    "-------------------------7-------------------------------"

    def modificar(
        self,
        ID,
        nombre=None,
        apellido=None,
        telefono=None,
        direccion=None,
        mail=None,
        relacion=None,
    ):
        self.id = ID.get()
        self.no = nombre.get()
        self.ap = apellido.get()
        self.tf = telefono.get()
        self.direc = direccion.get()
        self.em = mail.get()
        self.re = relacion.get()
        if (self.no == "") or (self.ap == "") or (self.id == ""):
            self.mensaje("Modificar", "Faltan Datos")

        else:
            try:
                self.limpiar_element()
                crud = Crud_Method()
                crud.modify_data(
                    self.id, self.no, self.ap, self.tf, self.direc, self.em, self.re
                )
                self.mensaje("Modificar", "Contacto modificado")
                self.listar()
            except Exception:
                self.mensaje("Modificar", "Error al modificar Contacto")

    "-------------------------8-------------------------------"

    def guardar(self, ID, nombre, apellido, telefono, direccion, mail, relacion):

        self.no = nombre.get()
        self.ap = apellido.get()
        self.tf = telefono.get()
        self.direc = direccion.get()
        self.em = mail.get()
        self.re = relacion.get()

        if (self.no == "") or (self.ap == ""):
            self.mensaje("Guardar", "Faltan Datos")
        else:
            crud = Crud_Method()
            crud.create_table()
            try:
                crud.insert_data(
                    self.no,
                    self.ap,
                    val.validar_telefono(self.tf),
                    self.direc,
                    val.validar_email(self.em),
                    self.re,
                )
                self.mensaje("Guardar", "Datos Guardados")
            except Exception:
                self.mensaje("Guardar", "Verifique, el contacto ya existe en la agenda")

            self.listar()
            self.limpiar_element()
