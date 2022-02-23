""" 
----------- INFORMACION --------------------------
    Grupo 1, integrantes: 
    Baracetti, Giuliana
    Corbatto, Mauricio
    Mervich, German
    Mielniczuk Lapp, Julio
    Nanini, Marcos
-------------- MODULOS ------------------------
controlador --> es en donde nos encontramos y es desde donde se lanza la app
modelo_1_bbdd --> base de datos
modelo_2_oper --> operaciones, se conecta 
    con la base de datos y presenta la informacion en tkinter
modelo_3_valid --> funciones regex 
vista --> se encuentra en el todo lo referido a la interfaz grafica
---------------------------------------------------"""


from vista import Inicio
from tkinter import Tk

"------ importaciones de modulos --------------"
"------------- clases -------------------------"


class Controller:
    def __init__(self, root):
        self.root_controller = root
        self.inicio_agenda()

    def inicio_agenda(self):
        Inicio(self.root_controller)


"------------- root -------------------------"
if __name__ == "__main__":
    root_tk = Tk()
    app = Controller(root_tk)
    root_tk.mainloop()
