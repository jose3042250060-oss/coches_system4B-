from tkinter import Tk, Label, Entry, Button, messagebox, StringVar, Menu, Frame
from coches import coches

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0, 0)
        self.barraMenu()
        self.main()
    
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            if not isinstance(widget, Menu):
                widget.destroy()

    def barraMenu(self):
        menuBar = Menu(self.ventana)
        self.ventana.config(menu=menuBar)

        menuPrincipal = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Principal", menu=menuPrincipal)
        menuPrincipal.add_command(label="Menu Principal", command=self.main)
        menuPrincipal.add_command(label="Menu Acciones", command=self.menu_acciones)
        menuPrincipal.add_separator()
        menuPrincipal.add_command(label="Salir", command=self.ventana.quit)
                
        accionesMenu = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Acciones", menu=accionesMenu)
        accionesMenu.add_command(label="Agregar", command=self.insertar_coche_view)
        accionesMenu.add_command(label="Borrar", command=self.eliminar_coche_view)
        accionesMenu.add_command(label="Modificar", command=self.modificar_coche_view)
        accionesMenu.add_command(label="Mostrar", command=self.consultar_coche_view)
        accionesMenu.add_separator()
        accionesMenu.add_command(label="Regresar", command=self.main)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text=":::MENU PRINCIPAL:::").pack(pady=20)
        Button(self.ventana, text="1- Coches", command=self.menu_acciones).pack(padx=10, pady=5)
        Button(self.ventana, text="2- Salir", command=self.ventana.quit).pack(padx=10, pady=5)

    def menu_acciones(self):
        self.borrarPantalla()
        tipo = "Coche"
        Label(self.ventana, text=f"...:::Menu de {tipo}:::...").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_coche_view).pack(pady=5)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_coche_view).pack(pady=5)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_coche_view).pack(pady=5)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_coche_view).pack(pady=5)
        Button(self.ventana, text="5.- Regresar", command=self.main).pack(pady=5)

    def insertar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingrese los datos del coche...").pack(pady=10)
        
        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)
        
        # CORRECCIÓN: Todos los Entry ahora pertenecen a self.frame1
        Label(self.frame1, text="Marca: ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.marca = Entry(self.frame1)
        self.marca.focus()
        self.marca.grid(row=0, column=1, pady=5, padx=5, sticky="w")
        
        Label(self.frame1, text="Color: ").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.color = Entry(self.frame1)
        self.color.grid(row=1, column=1, pady=5, padx=5, sticky="w")
        
        Label(self.frame1, text="Modelo: ").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.modelo = Entry(self.frame1)
        self.modelo.grid(row=2, column=1, pady=5, padx=5, sticky="w")
        
        Label(self.frame1, text="Velocidad: ").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.velocidad = Entry(self.frame1)
        self.velocidad.grid(row=3, column=1, pady=5, padx=5, sticky="w")
        
        Label(self.frame1, text="Potencia: ").grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.potencia = Entry(self.frame1)
        self.potencia.grid(row=4, column=1, pady=5, padx=5, sticky="w")
        
        Label(self.frame1, text="# de Asientos: ").grid(row=5, column=0, pady=5, padx=5, sticky="e")
        self.asientos = Entry(self.frame1)
        self.asientos.grid(row=5, column=1, pady=5, padx=5, sticky="w")

        Button(self.frame1, text="Agregar", command=self.insertar_y_refrescar).grid(row=6, column=0, pady=10, padx=5, sticky="e")
        Button(self.frame1, text="Regresar", command=self.menu_acciones).grid(row=6, column=1, pady=10, padx=5, sticky="w")

    def eliminar_coche_view(self):
        self.borrarPantalla()

        Label(self.ventana, text="Ingresar el ID del coche que deseas borrar:").pack(pady=10)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)

        # CORRECCIÓN: Ambos botones pertenecen a self.frame1 y usan columnas distintas
        self.btn_buscar = Button(self.frame1, text="Buscar",
                                 command=lambda: self.buscar_controller("eliminar"))
        self.btn_buscar.grid(row=0, column=0, pady=5, padx=5, sticky="e")

        self.btn_eliminar = Button(self.frame1, text=":: Eliminar ::", state="disabled",
                                   command=self.eliminar_y_refrescar)
        self.btn_eliminar.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        Button(self.ventana, text="::Regresar::", command=self.menu_acciones).pack(pady=5)

    def consultar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...::: Consultar Coches :::...").pack(pady=10)
        filas = self.consultar_coche_controller()
        Label(self.ventana, text=filas, justify="left").pack(pady=5)
        Button(self.ventana, text="::Regresar::", command=self.menu_acciones).pack(pady=10)

    def modificar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del coche a modificar").pack(pady=10)
        
        frame_busqueda = Frame(self.ventana)
        frame_busqueda.pack(pady=5)
        
        Label(frame_busqueda, text="ID: ").grid(row=0, column=0, padx=5)
        self.id = Entry(frame_busqueda)
        self.id.focus()
        self.id.grid(row=0, column=1, padx=5)
        
        self.btn_buscar = Button(frame_busqueda, text="Buscar", command=lambda: self.buscar_controller("modificar"))
        self.btn_buscar.grid(row=0, column=2, padx=5)
        
        Label(self.ventana, text="...Datos del Coche").pack(pady=10)
        
        self.var_marca = StringVar()
        self.var_color = StringVar()
        self.var_modelo = StringVar()
        self.var_velocidad = StringVar()
        self.var_potencia = StringVar()
        self.var_asientos = StringVar()
        
        # CORRECCIÓN: Formulario con grid para que quepa completo en 600x600
        frame_datos = Frame(self.ventana)
        frame_datos.pack(pady=5)
        
        Label(frame_datos, text="Marca: ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.marca = Entry(frame_datos, textvariable=self.var_marca)
        self.marca.grid(row=0, column=1, pady=5, padx=5, sticky="w")
        
        Label(frame_datos, text="Color: ").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.color = Entry(frame_datos, textvariable=self.var_color)
        self.color.grid(row=1, column=1, pady=5, padx=5, sticky="w")
        
        Label(frame_datos, text="Modelo: ").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.modelo = Entry(frame_datos, textvariable=self.var_modelo)
        self.modelo.grid(row=2, column=1, pady=5, padx=5, sticky="w")
        
        Label(frame_datos, text="Velocidad: ").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.velocidad = Entry(frame_datos, textvariable=self.var_velocidad)
        self.velocidad.grid(row=3, column=1, pady=5, padx=5, sticky="w")
        
        Label(frame_datos, text="Potencia: ").grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.potencia = Entry(frame_datos, textvariable=self.var_potencia)
        self.potencia.grid(row=4, column=1, pady=5, padx=5, sticky="w")
        
        Label(frame_datos, text="# de Asientos: ").grid(row=5, column=0, pady=5, padx=5, sticky="e")
        self.asientos = Entry(frame_datos, textvariable=self.var_asientos)
        self.asientos.grid(row=5, column=1, pady=5, padx=5, sticky="w")
        
        self.btn_modificar = Button(frame_datos, text=":: Modificar ::", state="disabled", command=self.modificar_y_refrescar)
        self.btn_modificar.grid(row=6, column=0, pady=15, padx=5, sticky="e")
        
        Button(frame_datos, text=":: Regresar ::", command=self.menu_acciones).grid(row=6, column=1, pady=15, padx=5, sticky="w")
    
    def cambiar_estado_btn(self, estado, tipo_accion):
        nuevo_estado = "normal" if estado else "disabled"
        if tipo_accion == "eliminar":
            self.btn_eliminar.config(state=nuevo_estado)
        elif tipo_accion == "modificar":
            self.btn_modificar.config(state=nuevo_estado)
                    
    def confirmacion_eliminar(self, tipo_accion):
        resp = messagebox.askquestion(title="...¡Atencion!...", message=f"...¿Desea {tipo_accion} el registro?...")
        return resp == "yes"

    def insertar_y_refrescar(self):
        self.insertar_coche_controller()
        self.insertar_coche_view()

    def eliminar_y_refrescar(self):
        self.eliminar_coche_controller()
        self.eliminar_coche_view()

    def modificar_y_refrescar(self):
        self.modificar_coche_controller()
        self.modificar_coche_view()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title=":: Exitoso ::", message="...¡Acción Realizada con Éxito!...")
        else:
            messagebox.showerror(title=":: Error ::", message="...¡Esta Acción no pudo realizarse!...")

    def insertar_coche_controller(self):
        coches1 = coches.Coches(
            self.marca.get(),
            self.color.get(),
            self.modelo.get(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )
        respuesta = coches1.insertar()
        self.respuesta_sql(respuesta)
        del coches1

    def eliminar_coche_controller(self):
        id_coche = self.id.get()
        if self.confirmacion_eliminar("eliminar"):
            respuesta = coches.Coches.eliminar(id_coche)
        else:
            respuesta = False
        self.respuesta_sql(respuesta)

    def consultar_coche_controller(self):
        registro = coches.Coches.consultar()
        filas = ""
        if len(registro) > 0:
            for num, fila in enumerate(registro, 1):
                filas += f"Coche #{num} | ID: {fila[0]} | Marca: {fila[1]} | Color: {fila[2]} | Modelo: {fila[3]} | Vel: {fila[4]} | Pot: {fila[5]} | Asientos: {fila[6]}\n"
        else:
            filas = "...¡No se encontró información en la BD!..."
        return filas

    def modificar_coche_controller(self):
        id_coche = self.id.get()
        coches1 = coches.Coches(
            self.marca.get(),
            self.color.get(),
            self.modelo.get(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )
        respuesta = coches1.actualizar(id_coche)
        self.respuesta_sql(respuesta)
        del coches1

    def buscar_controller(self, tipo_accion):
        id_coche = self.id.get()
        coche1 = coches.Coches.buscar(id_coche)
        if len(coche1) > 0:
            messagebox.showinfo(title="..¡Registro Encontrado!..",
                                message=f"...El registro fue encontrado con éxito, puedes {tipo_accion}...")
            self.cambiar_estado_btn(True, tipo_accion)
            if tipo_accion == "modificar":
                self.var_marca.set(coche1[0][1])
                self.var_color.set(coche1[0][2])
                self.var_modelo.set(coche1[0][3])
                self.var_velocidad.set(coche1[0][4])
                self.var_potencia.set(coche1[0][5])
                self.var_asientos.set(coche1[0][6])
        else:
            messagebox.showerror(title="...¡Verifica por favor!...",
                                 message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!...")
            self.cambiar_estado_btn(False, tipo_accion)
            
if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()