"""
-------------- vista --------------------
Este modulo es referido a tkinter, en el mismo se encuentra la configuracion
de toda la interfaz grafica
--------------- inicion --------------------------
1.___init___ ---> conf. de la primera ventana que
    saldra al arrancar la app
2.clasico---> genera que la interfaz grafica
    cambie la tematica de las letras y fondo
3.noche---> genera que la interfaz grafica 
    cambie la tematica de las letras y fondo
4.ingreso_datos--->lanza la 2 ventana para
    poder llevar a cabo las siguientes funiones:
5.cerrar---> boton para cerrar la app
6.clasico1---> genera que la interfaz grafica
    cambie la tematica de las letras y fondo
7.oscuro1--->genera que la interfaz grafica cambie
    la tematica de las letras y fondo
8.limpiar---> limpia los datos dentro de los Entry de la interfaz grafica
9.lista---> lista los contactos
---las sig. def. captan los datos de tkinter para ser
    usados en el modulo_2_oper en la definicion dentro de
    ese modulo que haga referencia cada uno
    (se especifica acontinuacion a que def. haran referencia)
10.borra---> nos lleva a la funcion borrar
11.busca---> nos lleva a la funcion buscar
12.modifica---> nos lleva a la funcion modificar
13.guarda---> nos lleva a la funcion guardar
"""


from modelo_2_oper import Modelo
from tkinter import END
from tkinter import INSERT
from tkinter import Text
from tkinter import IntVar
import webbrowser
from tkinter import OptionMenu
from tkinter import messagebox
from tkinter import StringVar
from tkinter import Button
from tkinter import Menu
from tkinter import Tk
from tkinter import Entry
from tkinter import Label

"------ importaciones de modulos --------------"

"------------- clases -------------------------"


class Inicio:
    "-------------- primera ventana -----------------------"
    "------------------- 1 -----------------------"

    def __init__(self, parent=None, **config):

        self.window_inicio = parent
        self.window_inicio.title("Agenda")
        self.window_inicio.config(bg="sky blue")

        self.label_titulo = Label(self.window_inicio, **config)
        self.label_titulo.config(
            bg="sky blue",
            fg="blue4",
            text="AGENDA DE CONTACTOS",
            padx=12,
            height=16,
            width=20,
            font=("courier", 10, "bold"),
        )
        self.label_titulo.grid(row=1, column=2)

        self.boton_nocturno = Button(self.window_inicio, **config)
        self.boton_nocturno.config(
            command=lambda: self.noche(),
            text="Night",
            bg="black",
            fg="white",
            padx=15,
            height=1,
            width=5,
        )
        self.boton_nocturno.grid(row=2, column=1)

        self.boton_clasico = Button(self.window_inicio, **config)
        self.boton_clasico.config(
            command=lambda: self.clasico(),
            text="Classic",
            bg="steel blue",
            fg="black",
            padx=15,
            height=1,
            width=5,
        )
        self.boton_clasico.grid(row=3, column=1)

        "--------------- Menu despegable ---------------"
        self.menubarra = Menu(self.window_inicio)
        self.menuarchivo = Menu(self.menubarra, tearoff=0)
        self.menuarchivo.add_command(
            label="Entrar", command=lambda: self.ingreso_datos()
        )
        self.menuarchivo.add_separator()
        self.menuarchivo.add_command(
            label="Salir", command=lambda: self.window_inicio.destroy()
        )
        self.window_inicio.config(menu=self.menubarra)
        self.menubarra.add_cascade(label="Archivo", menu=self.menuarchivo)

        "--------------- Menu despegable ---------------"
        "-------------- ayuda --------------"
        self.menuayuda = Menu(self.menubarra, tearoff=0)
        self.menuayuda.add_command(
            label="Acerca de...",
            command=lambda: webbrowser.open(
                "https://docs.google.com/document/d/1whPh5qDT3d2XDRh7x_s9qz1lCzp9pK9UQYkXIV7l7pY/edit?usp=sharing"
            ),
        )
        self.menuayuda.add_command(
            label="Licencia",
            command=lambda: messagebox.showinfo(
                "Licencia",
                " Integrantes: Baracetti, Giuliana; "
                "Corbatto, Mauricio; Mervich, German;"
                " Mielniczuk Lapp, Julio; Nanini, Marcos. "
                " Copyright © Todos los Derechos Reservados.",
            ),
        )
        self.menubarra.add_cascade(label="Ayuda", menu=self.menuayuda)

        self.boton_entrar = Button(self.window_inicio, **config)
        self.boton_entrar.config(
            command=lambda: self.ingreso_datos(),
            text="Entrar",
            bg="steel blue",
            fg="black",
            padx=20,
            height=1,
            width=5,
            font=("courier", 10, "bold"),
        )
        self.boton_entrar.grid(row=2, column=2)

    "------------------- 2 -----------------------"

    def clasico(self):

        self.window_inicio.config(bg="sky blue")
        self.label_titulo.config(bg="sky blue")
        self.label_titulo.config(fg="blue4")
        self.boton_entrar.config(bg="steel blue")
        self.boton_entrar.config(fg="black")
        self.window_inicio.mainloop()

    "------------------- 3 -----------------------"

    def noche(self):

        self.window_inicio.config(bg="black")
        self.label_titulo.config(bg="black")
        self.label_titulo.config(fg="white")
        self.boton_entrar.config(bg="white")
        self.boton_entrar.config(fg="black")
        self.window_inicio.mainloop()

    "----------------------- segunda ventana ------------------------"
    "------------------- 4 -----------------------"

    def ingreso_datos(self):
        self.window_inicio.destroy()
        self.window_ppal = Tk()

        self.window_ppal.geometry("1050x600")
        self.window_ppal.title("Agenda - MENU PRINCIPAL")
        self.window_ppal.config(bg="sky blue")

        self.label_titulo1 = Label(
            self.window_ppal,
            text="Ingrese a continuación los datos del contacto",
            bg="RoyalBlue1",
            font="bold",
        )

        self.label_titulo1.grid(row=0, column=0, columnspan=2)

        # Menu desplegable "Archivo"
        self.menuppal = Menu(self.window_ppal)
        self.menuarch = Menu(self.menuppal, tearoff=0)
        self.menuarch.add_separator()
        self.menuarch.add_command(
            label="Salir", command=lambda: self.window_ppal.destroy()
        )
        self.window_ppal.config(menu=self.menuppal)
        self.menuppal.add_cascade(label="Archivo", menu=self.menuarch)

        # Menu desplegable "Ayuda"
        self.menuayu = Menu(self.menuppal, tearoff=0)
        self.menuayu.add_command(
            label="Acerca de...",
            command=lambda: webbrowser.open(
                "https://docs.google.com/document/d/1whPh5qDT3d2XDRh7x_s9qz1lCzp9pK9UQYkXIV7l7pY/edit?usp=sharing"
            ),
        )
        self.menuayu.add_command(
            label="Licencia",
            command=lambda: messagebox.showinfo(
                "Licencia",
                " Integrantes: Baracetti, Giuliana; "
                "Corbatto, Mauricio; Mervich, German; "
                "Mielniczuk Lapp, Julio; Nanini, Marcos. "
                " Copyright © Todos los Derechos Reservados.",
            ),
        )
        self.menuppal.add_cascade(label="Ayuda", menu=self.menuayu)

        # VARIABLES DE CAJAS
        ID = IntVar()
        nombre = StringVar()
        apellido = StringVar()
        telefono = StringVar()
        direccion = StringVar()
        mail = StringVar()
        relacion = StringVar()

        # WIDGETS
        self.label_ID = Label(self.window_ppal, text="ID", bg="sky blue")
        self.label_ID.grid(row=1, column=0)
        self.cajaID = Entry(self.window_ppal, textvariable=ID)
        self.cajaID.grid(row=1, column=1)

        self.label_Nombre = Label(self.window_ppal, text="Nombre", bg="sky blue")
        self.label_Nombre.grid(row=2, column=0)
        self.cajaNombre = Entry(self.window_ppal, textvariable=nombre)
        self.cajaNombre.grid(row=2, column=1)

        self.label_Apellido = Label(self.window_ppal, text="Apellido", bg="sky blue")
        self.label_Apellido.grid(row=3, column=0)
        self.cajaApellido = Entry(self.window_ppal, textvariable=apellido)
        self.cajaApellido.grid(row=3, column=1)

        self.label_Telefono = Label(self.window_ppal, text="Telefono", bg="sky blue")
        self.label_Telefono.grid(row=4, column=0)
        self.cajaTelefono = Entry(self.window_ppal, textvariable=telefono)
        self.cajaTelefono.grid(row=4, column=1)

        self.label_Direccion = Label(self.window_ppal, text="Direccion", bg="sky blue")
        self.label_Direccion.grid(row=5, column=0)
        self.cajaDireccion = Entry(self.window_ppal, textvariable=direccion)
        self.cajaDireccion.grid(row=5, column=1)

        self.label_Email = Label(self.window_ppal, text="Email", bg="sky blue")
        self.label_Email.grid(row=6, column=0)
        self.cajaEmail = Entry(self.window_ppal, textvariable=mail)
        self.cajaEmail.grid(row=6, column=1)

        OPTIONS = ["Familiar", "Pareja", "Amigo", "Trabajo"]

        self.label_Relacion = Label(
            self.window_ppal, text="Tipo de Contacto", bg="sky blue"
        )
        self.label_Relacion.grid(row=7, column=0)

        relacion = StringVar(self.window_ppal)
        relacion.set(OPTIONS[0])
        dropDownMenu = OptionMenu(
            self.window_ppal, relacion, OPTIONS[0], OPTIONS[1], OPTIONS[2], OPTIONS[3]
        )
        dropDownMenu.grid(row=7, column=1)

        self.textscreen = Text(self.window_ppal)
        self.textscreen.place(x=50, y=240, width=950, height=300)

        # BOTONES
        self.botonAgregar = Button(
            self.window_ppal,
            text="Agregar",
            command=lambda: (
                self.guarda(ID, nombre, apellido, telefono, direccion, mail, relacion),
                self.lista(ID, nombre, apellido, telefono, direccion, mail, relacion),
            ),
            bg="steel blue",
        )
        self.botonAgregar.place(x=50, y=200)

        self.botonModificar = Button(
            self.window_ppal,
            text="Modificar",
            command=lambda: (
                self.modifica(
                    ID, nombre, apellido, telefono, direccion, mail, relacion
                ),
                self.lista(ID, nombre, apellido, telefono, direccion, mail, relacion),
            ),
            bg="steel blue",
        )
        self.botonModificar.place(x=140, y=550)

        self.botonBorrar = Button(
            self.window_ppal,
            text="Borrar",
            command=lambda: (
                self.borra(ID, nombre, apellido, telefono, direccion, mail, relacion),
                self.lista(ID, nombre, apellido, telefono, direccion, mail, relacion),
            ),
            bg="steel blue",
        )
        self.botonBorrar.place(x=250, y=550)

        self.botonBuscar = Button(
            self.window_ppal,
            text="Buscar",
            command=lambda: self.busca(
                ID, nombre, apellido, telefono, direccion, mail, relacion
            ),
            bg="steel blue",
        )
        self.botonBuscar.place(x=350, y=550)

        self.botonReset = Button(
            self.window_ppal,
            text="Reset",
            command=lambda: self.limpiar(
                ID, nombre, apellido, telefono, direccion, mail, relacion
            ),
            bg="steel blue",
        )
        self.botonReset.place(x=450, y=550)

        self.botonCerrar = Button(
            self.window_ppal,
            text="Cerrar Aplicación",
            command=lambda: self.cerrar(),
            bg="red3",
        )
        self.botonCerrar.place(x=900, y=550)
        """---------------Botones clasico y oscuro ------------
            ----------------------------------------------------"""
        self.botonclasico = Button(
            self.window_ppal,
            text="Classic",
            command=lambda: self.clasico1(),
            bg="steel blue",
        )
        self.botonclasico.place(x=938, y=175)
        self.botonclasico.config(width=8, height=1)

        self.botonoscuro = Button(
            self.window_ppal,
            text="Nocturno",
            command=lambda: self.oscuro1(),
            bg="black",
            fg="white",
        )
        self.botonoscuro.place(x=938, y=200)
        self.botonoscuro.config(width=8, height=1)

        try:
            self.lista(ID, nombre, apellido, telefono, direccion, mail, relacion)
        except Exception:
            pass

    "------------------- 5 -----------------------"

    def cerrar(self):
        self.window_ppal.destroy()

    "------------------- 6 -----------------------"

    def clasico1(self):
        self.window_ppal.config(bg="sky blue")
        self.label_ID.config(bg="sky blue", fg="black")
        self.label_Nombre.config(bg="sky blue", fg="black")
        self.label_Apellido.config(bg="sky blue", fg="black")
        self.label_Telefono.config(bg="sky blue", fg="black")
        self.label_Direccion.config(bg="sky blue", fg="black")
        self.label_Email.config(bg="sky blue", fg="black")
        self.label_Relacion.config(bg="sky blue", fg="black")
        self.botonAgregar.config(bg="steel blue", fg="black")
        self.botonModificar.config(bg="steel blue", fg="black")
        self.botonBorrar.config(bg="steel blue", fg="black")
        self.botonBuscar.config(bg="steel blue", fg="black")
        self.botonReset.config(bg="steel blue", fg="black")
        self.botonCerrar.config(bg="red3", fg="black")
        self.label_titulo1.config(bg="sky blue", fg="black")

    "------------------- 7 -----------------------"

    def oscuro1(self):
        self.window_ppal.config(bg="black")
        self.label_ID.config(bg="black", fg="white")
        self.label_Nombre.config(bg="black", fg="white")
        self.label_Apellido.config(bg="black", fg="white")
        self.label_Telefono.config(bg="black", fg="white")
        self.label_Direccion.config(bg="black", fg="white")
        self.label_Email.config(bg="black", fg="white")
        self.label_Relacion.config(bg="black", fg="white")
        self.botonAgregar.config(bg="grey", fg="black")
        self.botonModificar.config(bg="grey", fg="black")
        self.botonBorrar.config(bg="grey", fg="black")
        self.botonBuscar.config(bg="grey", fg="black")
        self.botonReset.config(bg="grey", fg="black")
        self.botonCerrar.config(bg="red3", fg="white")
        self.label_titulo1.config(bg="black", fg="white")

    "------------------- 8 -----------------------"

    def limpiar(self, ID, nombre, apellido, telefono, direccion, mail, relacion):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mail = mail
        self.relacion = relacion
        self.modelo = Modelo(ID, nombre, apellido, telefono, direccion, mail, relacion)
        self.modelo.limpiar_element()

    "------------------- 9 -----------------------"

    def lista(self, ID, nombre, apellido, telefono, direccion, mail, relacion):

        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mail = mail
        self.relacion = relacion

        self.listado = Modelo(ID, nombre, apellido, telefono, direccion, mail, relacion)
        self.listado = self.listado.listar()

        try:
            # Limpio lo que haya en pantalla
            self.textscreen.delete(1.0, END)
        except Exception:
            op.mensaje("Listado", "Error en listado")

        self.textscreen.insert(
            INSERT,
            "Id\tNombre\t\tApellido\t\tTelefono\t\tDirecc\t\t\tEmail\t\t\tRelacion\n",
        )

        for elemento in self.listado:
            # Inserto o imprimo en pantalla de Tkinter
            # lo que guarde en la lista
            id = elemento[0]
            nombre = elemento[1]
            apellido = elemento[2]
            telefono = elemento[3]
            direccion = elemento[4]
            mail = elemento[5]
            relacion = elemento[6]
            self.textscreen.insert(INSERT, id)
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, nombre)
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, apellido)
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, telefono)
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, direccion)
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, mail)
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, relacion)
            self.textscreen.insert(INSERT, "\t")
            self.textscreen.insert(INSERT, "\n")

    "------------ definicion de los botones -----------------------"
    "------------------- 10 -----------------------"

    def borra(self, ID, nombre, apellido, telefono, direccion, mail, relacion):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mail = mail
        self.relacion = relacion
        self.borrado = Modelo(ID, nombre, apellido, telefono, direccion, mail, relacion)
        self.borrado.borrar(ID, nombre, apellido, telefono, direccion, mail, relacion)

    "------------------- 11 -----------------------"

    def busca(self, ID, nombre, apellido, telefono, direccion, mail, relacion):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mail = mail
        self.relacion = relacion
        self.busqueda = Modelo(
            ID, nombre, apellido, telefono, direccion, mail, relacion
        )
        self.busqueda.buscar(ID, nombre, apellido, telefono, direccion, mail, relacion)

    "------------------- 12 -----------------------"

    def modifica(self, ID, nombre, apellido, telefono, direccion, mail, relacion):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mail = mail
        self.relacion = relacion
        self.modificacion = Modelo(
            ID, nombre, apellido, telefono, direccion, mail, relacion
        )
        self.modificacion.modificar(
            ID, nombre, apellido, telefono, direccion, mail, relacion
        )

    "------------------- 13 -----------------------"

    def guarda(self, ID, nombre, apellido, telefono, direccion, mail, relacion):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mail = mail
        self.relacion = relacion
        self.archivo = Modelo(ID, nombre, apellido, telefono, direccion, mail, relacion)
        self.archivo.guardar(ID, nombre, apellido, telefono, direccion, mail, relacion)
