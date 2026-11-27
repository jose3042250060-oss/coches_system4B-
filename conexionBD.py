import mysql.connector
from tkinter import messagebox
try:
    conexion = mysql.connector.connect(

        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'bd_coches'
    )
    cursor = conexion.cursor(buffered=True)
except Exception:

    messagebox.showerror(title = "Sistema de gestión de coches", message = "por el momento no es posible conectar a la base de datos, por favor intente más tarde")
