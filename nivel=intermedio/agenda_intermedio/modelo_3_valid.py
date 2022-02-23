"""
----------- modelo_3_valid-------------------
En este modulo encontramos el regex, el mismo nos genera
una gran ayuda para que los datos ingresados cumplan ciertos caracteres
o cantidad de letras/numeros a usar.
---------------Validacion----------------------------
mensaje--> configuracion de los mensajes de tkinter
validar_email---> conf. para que los datos ingresados tengan similitud a un mail
validar telefono---> genera que solo sea valido ingresar numeros 
"""
from tkinter import messagebox
import re

"------ importaciones de modulos --------------"

"------------- clases -------------------------"


def mensaje(titulo, texto):
    messagebox.showinfo(titulo, texto)


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
    except Exception:
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
    except Exception:
        mensaje("Validacion de Telefono", "Error, ingrese Telefono nuevamente")
        tf = ""
        return tf
