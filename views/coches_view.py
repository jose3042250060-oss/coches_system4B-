from controllers.coches_controller import CochesController
from tkinter import Label, Entry, Button, messagebox, StringVar, Menu, Frame, ttk

class CochesView:
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
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)
        Button(self.frame1, text="Coches",width=10,height=3, command=self.menu_acciones).pack(padx=10, pady=5)
        Button(self.frame1, text="Salir",width=10,height=3, command=self.ventana.quit).pack(padx=10, pady=5)

    def menu_acciones(self):
        self.borrarPantalla()
        tipo = "Coche"
        Label(self.ventana, text=f"...:::Menu de {tipo}:::...").pack(pady=10)
        
        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)
        
        Button(self.frame1, text="Agregar",width=10,height=3, command=self.insertar_coche_view).grid(row=0, column=0, pady=10, padx=10, sticky="ew")
        Button(self.frame1, text="Borrar",width=10,height=3, command=self.eliminar_coche_view).grid(row=1, column=0, pady=10, padx=10, sticky="ew")
        Button(self.frame1, text="Modificar",width=10,height=3, command=self.modificar_coche_view).grid(row=2, column=0, pady=10, padx=10, sticky="ew")
        Button(self.frame1, text="Mostrar",width=10,height=3, command=self.consultar_coche_view).grid(row=3, column=0, pady=10, padx=10, sticky="ew")
        Button(self.frame1, text="Regresar",width=10,height=3, command=self.main).grid(row=4, column=0, pady=10, padx=10, sticky="ew")

    def insertar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingrese los datos del coche...").pack(pady=10)
        
        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)
        
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

        Button(self.frame1, text="Agregar", command=lambda: {CochesController.insertar_coche_controller(self),self.insertar_coche_view()}).grid(row=6, column=0, pady=10, padx=5, sticky="e")

        Button(self.frame1, text="Regresar", command=self.menu_acciones).grid(row=6, column=1, pady=10, padx=5, sticky="w")

    def eliminar_coche_view(self):
        self.borrarPantalla()

        Label(self.ventana, text="Ingresar el ID del coche que deseas borrar:").pack(pady=10)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)

        self.btn_buscar = Button(self.frame1, text="Buscar", command=lambda: CochesController.buscar_controller(self, "eliminar"))
        self.btn_buscar.grid(row=0, column=0, pady=5, padx=5, sticky="e")

        self.btn_eliminar = Button(self.frame1, text=":: Eliminar ::", state="disabled", command=lambda: CochesController.eliminar_coche_controller(self))
        self.btn_eliminar.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        Button(self.ventana, text="::Regresar::", command=self.menu_acciones).pack(pady=5)

    def consultar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...::: Consultar Coches :::...").pack(pady=10)
        
        # Tabla
        self.tree =ttk.Treeview(self.ventana, columns=("ID", "Marca", "Color", "Modelo","Velocidad","Potencia","Asientos"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.heading("Velocidad", text="Velocidad")
        self.tree.heading("Potencia", text="Potencia")
        self.tree.heading("Asientos", text="Asientos")
        self.tree.pack(fill="both", expand=False)

        CochesController.consultar_coche_controller(self)

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
        
        self.btn_buscar = Button(frame_busqueda, text="Buscar", command=lambda: CochesController.buscar_controller(self, "modificar"))
        self.btn_buscar.grid(row=0, column=2, padx=5)
        
        Label(self.ventana, text="...Datos del Coche").pack(pady=10)
        
        self.var_marca = StringVar()
        self.var_color = StringVar()
        self.var_modelo = StringVar()
        self.var_velocidad = StringVar()
        self.var_potencia = StringVar()
        self.var_asientos = StringVar()
        
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
        
        self.btn_modificar = Button(self.ventana,frame_datos, text=":: Modificar ::", state="disabled", command=lambda: CochesController.modificar_coche_controller(self))
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

    def encontro(self, coche1, tipo_accion):
        if len(coche1) > 0:
            messagebox.showinfo(title="..¡Registro Encontrado!..",message=f"...El registro fue encontrado con éxito, puedes {tipo_accion}...")
            self.cambiar_estado_btn(True, tipo_accion)
            if tipo_accion == "modificar":
                self.var_marca.set(coche1[0][1])
                self.var_color.set(coche1[0][2])
                self.var_modelo.set(coche1[0][3])
                self.var_velocidad.set(coche1[0][4])
                self.var_potencia.set(coche1[0][5])
                self.var_asientos.set(coche1[0][6])
        else:
            messagebox.showerror(title="...¡Verifica por favor!...", message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!...")
            self.cambiar_estado_btn(False, tipo_accion)