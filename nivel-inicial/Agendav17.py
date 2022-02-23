# -*- coding: utf-8 -*-
"""

El presente archivo trabaja en conjunto con el archivo llamado "database".
Para ejecutar el Script completo, ambos archivos deben cuardarse en la misma carpeta
en Windows.

"""

# Importamos Librerias

from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
from basedatos1a import *
import sqlite3
import re


"""
FUNCIONES:

- Nuevo: Crea una nueva Ventana "root1" para que el usuario ingrese los datos, destruye
a "root0".

- Limpiar: Limpia todos los campos donde el Usuario ingresa datos.

- Guardar: Obtiene los datos ingresados por el usuario y los inserta en la Base de Datos.


- Listar: Se conecta por medio de instrucciones MySQL a la Base de datos y busca todos
los contactos Guardados. Los agrega a una Lista, los ordena y luego los imprime en pantalla
por TKinter.

- Modificar: Toma como parametros el ID, Nombre y Apellido ingresados por el Usuario, los cuales
deben ser obligatorios de ingresar. Modifica las variables: Nombre, Apellido, Telefono, Direccion,
Email del contacto que coincide con el ID ingresado.

- Borrar: Borra un contacto existente en la Agenda. Utiliza el ID del contacto como argumento.

- Buscar: Busca un contacto existente en la Agenda. Utiliza el ID del contacto como argumento. 

VARIABLES DE CAJAS:

Definimos de que tipo seran las variables que ingrese el usuario por
la interfaz gráfica: String, Entero, etc.

WIDGETS:

Definimos las etiquetas y las cajas para que el Usuario ingrese los datos.

"""

##########

#Color clásico ventana de inicio
def clasico():
    root0.config(bg="sky blue")
    titulo.config(bg="sky blue")
    titulo.config(fg="blue4")
    ok.config(bg="aquamarine")
    ok.config(fg="blue1")
    root0.mainloop()

#Color nocturno ventana de inicio
def oscuro():
    root0.config(bg="black")
    titulo.config(bg="black")
    titulo.config(fg="white")
    ok.config(bg="white")
    ok.config(fg="black")
    root0.mainloop()


def nuevo():
    root0.destroy()
    OPTIONS = [
        "Familiar",
        "Pareja",
        "Amigo",
        "Trabajo",
    ]

    listado = []

    def mensaje(titulo, texto):
        messagebox.showinfo(titulo, texto)

    def listar():
        if len(listado) > 0:
            # Borrar lo que haya en la lista
            listado.clear()
        conexion = sqlite3.connect("agenda1.db")
        consulta = conexion.cursor()
        consulta.execute(
            "SELECT id, nombre, apellido, telefono, direccion, mail, relacion from agenda1"
        )
        for i in consulta:
            # Obtengo de la BDatos las diferentes caract para cada contacto (i)
            id = i[0]
            nombre = i[1]
            apellido = i[2]
            telefono = i[3]
            direccion = i[4]
            mail = i[5]
            relacion = i[6]
            listado.append(i)  # Agrego lo que obtuve a una lista vacia
            listado.sort()
        conexion.close()

        try:
            textscreen.delete(1.0, END)  # Limpio lo que haya en pantalla
        except:
            mensaje("Listado", "Error en listado")

        textscreen.insert(
            INSERT,
            "Id\tNombre\t\tApellido\t\tTelefono\t\tDirecc\t\t\tEmail\t\t\tRelacion\n",
        )

        for elemento in listado:
            # Inserto o imprimo en pantalla de Tkinter lo que guarde en la lista
            id = elemento[0]
            nombre = elemento[1]
            apellido = elemento[2]
            telefono = elemento[3]
            direccion = elemento[4]
            mail = elemento[5]
            relacion = elemento[6]
            textscreen.insert(INSERT, id)
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, nombre)
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, apellido)
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, telefono)
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, direccion)
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, mail)
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, relacion)
            textscreen.insert(INSERT, "\t")
            textscreen.insert(INSERT, "\n")

    def limpiar():
        ID.set("")
        nombre.set("")
        apellido.set("")
        telefono.set("")
        direccion.set("")
        mail.set("")
        relacion.set("")

    def validar_email(em):
        patron_em = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-z]{2,}"
        coincidencias = re.search(patron_em, em)
        try:
            if coincidencias:
                return em
            else:
                mensaje("Validar Email", "Email No Valido")
                em = ""
                return em
        except:
            mensaje("Validacion de Email", "Error, ingrese Email nuevamente")
            em = ""
            return em

    def validar_telefono(tf):
        patron_tf = r"[0-9]{7,11}"
        coincidencias = re.search(patron_tf, tf)
        try:
            if coincidencias:
                return tf
            else:
                mensaje("Validar Telefono", "Telefono No Valido")
                tf = ""
                return tf
        except:
            mensaje("Validacion de Telefono", "Error, ingrese Telefono nuevamente")
            tf = ""
            return tf

    def guardar():

        no = nombre.get()
        ap = apellido.get()
        tf = telefono.get()
        direc = direccion.get()
        em = mail.get()
        re = relacion.get()

        if (no == "") or (ap == ""):
            mensaje("Guardar", "Faltan Datos")
        else:
            limpiar()
            crear_tabla()

            try:
                insertar_datos(
                    no, ap, validar_telefono(tf), direc, validar_email(em), re
                )
                mensaje("Guardar", "Datos Guardados")
            except:

                mensaje("Guardar", "Verifique, el contacto ya existe en la agenda")

        listar()

    def modificar():
        id = ID.get()
        no = nombre.get()
        ap = apellido.get()
        tf = telefono.get()
        direc = direccion.get()
        em = mail.get()
        re = relacion.get()
        if (no == "") or (ap == "") or (id == ""):
            mensaje("Modificar", "Faltan Datos")

        else:
            try:
                limpiar()
                modifica(id, no, ap, validar_telefono(tf), direc, validar_email(em), re)
                mensaje("Modificar", "Contacto modificado")
                listar()

            except:
                mensaje("Modificar", "Error al modificar Contacto")

    def borrar():
        try:

            id = ID.get()
            if id == "":
                mensaje("Borrar", "Debes insertar el ID que deseas modificar")
            else:
                borra(id)
                limpiar()
                listar()
                mensaje("Borrar", "Contacto Borrado")
        except:
            mensaje("Error", "Error al borrar, inserta código")

    def buscar():
        try:

            id = ID.get()
            if id == "":
                mensaje("Buscar", "Inserta Identificador")
            else:
                tupla = busca(id)
                nombre.set(tupla[0])
                apellido.set(tupla[1])
                telefono.set(tupla[2])
                direccion.set(tupla[3])
                mail.set(tupla[4])
                relacion.set(tupla[5])
                mensaje("Buscar", "Contacto encontrado")
        except:
            mensaje("Error", "Error al buscar, inserta Identificador")

    def cerrar():
        root1.destroy()

    # Botón color clásico ventana principal
    def clasico1():
        root1.config(bg="sky blue")
        etiquetaID.config(bg="sky blue", fg="black")
        etiquetaNombre.config(bg="sky blue", fg="black")
        etiquetaApellido.config(bg="sky blue", fg="black")
        etiquetaTelefono.config(bg="sky blue", fg="black")
        etiquetaDireccion.config(bg="sky blue", fg="black")
        etiquetaEmail.config(bg="sky blue", fg="black")
        etiquetaRelacion.config(bg="sky blue", fg="black")
        botonAgregar.config(bg="steel blue", fg="black")
        botonModificar.config(bg="steel blue", fg="black")
        botonBorrar.config(bg="steel blue", fg="black")
        botonBuscar.config(bg="steel blue", fg="black")
        botonReset.config(bg="steel blue", fg="black")
        botonCerrar.config(bg="red3", fg="black")
        titulo.config(bg="sky blue", fg="black")
 
    #Botón color nocturno ventana principal
    def oscuro1():
        root1.config(bg="black")
        etiquetaID.config(bg="black", fg="white")
        etiquetaNombre.config(bg="black", fg="white")
        etiquetaApellido.config(bg="black", fg="white")
        etiquetaTelefono.config(bg="black", fg="white")
        etiquetaDireccion.config(bg="black", fg="white")
        etiquetaEmail.config(bg="black", fg="white")
        etiquetaRelacion.config(bg="black", fg="white")
        botonAgregar.config(bg="grey", fg="black")
        botonModificar.config(bg="grey", fg="black")
        botonBorrar.config(bg="grey", fg="black")
        botonBuscar.config(bg="grey", fg="black")
        botonReset.config(bg="grey", fg="black")
        botonCerrar.config(bg="red3", fg="white")
        titulo.config(bg="black", fg="white")

    root1 = Tk()
    root1.geometry("1050x600")
    root1.title("Agenda - MENU PRINCIPAL")
    root1.config(bg="sky blue")
    titulo = Label(
        root1,
        text="Ingrese a continuación los datos del contacto",
        bg="RoyalBlue1",
        font="bold",
    )
    titulo.grid(row=0, column=0, columnspan=2)

    # VARIABLES DE CAJAS

    ID = IntVar()
    nombre = StringVar()
    apellido = StringVar()
    telefono = StringVar()
    direccion = StringVar()
    mail = StringVar()
    relacion = StringVar()

    # WIDGETS

    etiquetaID = Label(
        root1,
        text="ID",
        bg="sky blue",
    )
    etiquetaID.grid(row=1, column=0)
    cajaID = Entry(root1, textvariable=ID)
    cajaID.grid(row=1, column=1)

    etiquetaNombre = Label(
        root1,
        text="Nombre",
        bg="sky blue",
    )
    etiquetaNombre.grid(row=2, column=0)
    cajaNombre = Entry(root1, textvariable=nombre)
    cajaNombre.grid(row=2, column=1)

    etiquetaApellido = Label(
        root1,
        text="Apellido",
        bg="sky blue",
    )
    etiquetaApellido.grid(row=3, column=0)
    cajaApellido = Entry(root1, textvariable=apellido)
    cajaApellido.grid(row=3, column=1)

    etiquetaTelefono = Label(
        root1,
        text="Telefono",
        bg="sky blue",
    )
    etiquetaTelefono.grid(row=4, column=0)
    cajaTelefono = Entry(root1, textvariable=telefono)
    cajaTelefono.grid(row=4, column=1)

    etiquetaDireccion = Label(
        root1,
        text="Direccion",
        bg="sky blue",
    )
    etiquetaDireccion.grid(row=5, column=0)
    cajaDireccion = Entry(root1, textvariable=direccion)
    cajaDireccion.grid(row=5, column=1)

    etiquetaEmail = Label(
        root1,
        text="e-mail",
        bg="sky blue",
    )
    etiquetaEmail.grid(row=6, column=0)
    cajaEmail = Entry(root1, textvariable=mail)
    cajaEmail.grid(row=6, column=1)

    etiquetaRelacion = Label(
        root1,
        text="Tipo de contacto",
        bg="sky blue",
    )
    etiquetaRelacion.grid(row=9, column=0)

    relacion = StringVar(root1)
    relacion.set(OPTIONS[0])
    dropDownMenu = OptionMenu(
        root1, relacion, OPTIONS[0], OPTIONS[1], OPTIONS[2], OPTIONS[3]
    )

    dropDownMenu.grid(row=9, column=1)

    textscreen = Text(root1)
    textscreen.place(x=50, y=240, width=950, height=300)

    # BOTONES

    botonAgregar = Button(
        root1, text="Agregar", command=lambda: guardar(), bg="steel blue"
    )
    botonAgregar.place(x=50, y=200)

    botonModificar = Button(
        root1, text="Modificar", command=lambda: modificar(), bg="steel blue"
    )
    botonModificar.place(x=140, y=550)

    botonBorrar = Button(
        root1, text="Borrar", command=lambda: borrar(), bg="steel blue"
    )
    botonBorrar.place(x=250, y=550)

    botonBuscar = Button(
        root1, text="Buscar", command=lambda: buscar(), bg="steel blue"
    )
    botonBuscar.place(x=350, y=550)

    botonReset = Button(root1, text="Reset", command=lambda: limpiar(), bg="steel blue")
    botonReset.place(x=450, y=550)

    botonCerrar = Button(root1, text="Cerrar Aplicación", command=lambda: cerrar(), bg="red3")
    botonCerrar.place(x=900, y=550)
    ########### botones oscuro ······
    ################################################
    botonclasico = Button(root1, text="Classic", command=clasico1, bg="steel blue")
    botonclasico.place(x=938, y=175)
    botonclasico.config(width=8, height=1)
    botonoscuro = Button(root1, text="Nocturno", command=oscuro1, bg ="black", fg="white")
    botonoscuro.place(x=938, y=200)
    botonoscuro.config(width=8, height=1)
    listar()
    root1.mainloop()


# INICIO DEL PROGRAMA

# Creamos la ventana root0 y le asignamos una Geometría

root0 = Tk()
root0.title("Agenda")
root0.config(bg="sky blue")

# Le asignamos a la Ventana Inicial "root0" y diferentes Labels (Opciones) y Botones

# Título
titulo = Label(
    root0,
    bg="sky blue",
    fg="blue4",
    text="AGENDA DE CONTACTOS",
    padx=12,
    height=16,
    width=20,
    font=("courier", 10, "bold"),
)

titulo.grid(row=1, column=2)

# Botones Colores de Fondo
noche = Button(
    root0,
    command=lambda: oscuro(),
    text="Nocturno",
    bg="black",
    fg="white",
    padx=15,
    height=1,
    width=5,
)

noche.grid(row=2, column=1)

claro = Button(
    root0,
    command=lambda: clasico(),
    text="Classic",
    bg="steel blue",
    padx=15,
    height=1,
    width=5,
)

claro.grid(row=3, column=1)

# Boton de Ingreso
ok = Button(
    root0,
    command=lambda: nuevo(),
    text="Entrar",
    padx=20,
    height=1,
    width=5,
    bg="steel blue",
    fg="black",
    font=("courier", 10, "bold"),
)

ok.grid(row=2, column=2)

mainloop()
