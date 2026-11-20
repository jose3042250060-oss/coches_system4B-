from tkinter import Menu, Tk, Label, Entry, Button, messagebox, StringVar
from coches import coches

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0, 0)
        self.main()
    
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()


    def barraMenu(self):
        #Menu de Opciones
        menuBar = Menu(self.ventana)
        self.ventana.config(menu=menuBar)


        menuPrincipal = Menu(menuBar , tearoff=False)
        menuBar.add_cascade(label="Principal" , menu=menuPrincipal)
        menuPrincipal.add_command(label="Menu Principal",command=self.main)
        menuPrincipal.add_command(label="Menu Acciones",command=self.menu_acciones)
        menuPrincipal.add_separator()
        menuPrincipal.add_command(label="Salir",command=self.ventana.quit)
                
        accionesMenu = Menu(menuBar , tearoff=False)
        menuBar.add_cascade(label="Acciones" , menu=accionesMenu)
        accionesMenu.add_command(label="Agregar",command=self.insertar_coche_view )
        accionesMenu.add_command(label="Borrar",command=self.eliminar_coche_view)
        accionesMenu.add_command(label="Modificar",command=self.modificar_coche_view)
        accionesMenu.add_command(label="Mostrar",command=self.consultar_coche_view)
        accionesMenu.add_separator()
        accionesMenu.add_command(label="Regresar",command=self.main)



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
        self.barraMenu()
        self.borrarPantalla()
        Label(self.ventana, text="...Ingrese los datos del coche...").pack(pady=10)
        
        Label(self.ventana, text="Marca: ").pack(pady=2)
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=2)
        
        Label(self.ventana, text="Color: ").pack(pady=2)
        self.color = Entry(self.ventana)
        self.color.pack(pady=2)
        
        Label(self.ventana, text="Modelo: ").pack(pady=2)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=2)
        
        Label(self.ventana, text="Velocidad: ").pack(pady=2)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=2)
        
        Label(self.ventana, text="Potencia: ").pack(pady=2)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=2)
        
        Label(self.ventana, text="# de Asientos: ").pack(pady=2)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=2)

        Button(self.ventana, text="Agregar", command=lambda: 
               {self.insertar_coche_controller(),
                self.insertar_coche_view()
                }).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def eliminar_coche_view(self):
        self.barraMenu()
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar el ID del coche que deseas borrar:").pack(pady=10)
        self.id = Entry(self.ventana)          # antes: self.idBorrar
        self.id.focus()
        self.id.pack(pady=5)

        self.btn_buscar = Button(self.ventana, text="Buscar",
                             command=lambda: self.buscar_controller("eliminar"))
        self.btn_buscar.pack(pady=5)

        self.btn_eliminar = Button(self.ventana, text=":: Eliminar ::", state="disabled",
                               command=self.eliminar_y_refrescar)
        self.btn_eliminar.pack(pady=5)         # antes nunca se empacaba

        Button(self.ventana, text="::Regresar::", command=self.menu_acciones).pack(pady=5)

    def consultar_coche_view(self):
        self.barraMenu()
        self.borrarPantalla()
        Label(self.ventana, text="...::: Consultar Coches :::...").pack(pady=10)
        filas = self.consultar_coche_controller()
        Label(self.ventana, text=filas, justify="left").pack(pady=5)
        Button(self.ventana, text="::Regresar::", command=self.menu_acciones).pack(pady=10)

    def modificar_coche_view(self):
        self.barraMenu()
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del coche a modificar").pack(pady=10)
        
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)
        
        self.btn_buscar=Button(self.ventana,text="Buscar",command=lambda:self.buscar_controller("modificar"))
        self.btn_buscar.pack(pady=5)
        
        Label(self.ventana,text="...Datos del Coche").pack(pady=10)
        
        # Variables asociadas a los campos
        self.var_marca = StringVar()
        self.var_color = StringVar()
        self.var_modelo = StringVar()
        self.var_velocidad = StringVar()
        self.var_potencia = StringVar()
        self.var_asientos = StringVar()
        
        Label(self.ventana,text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana,textvariable=self.var_marca)
        self.marca.pack(pady=5)
        
        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana,textvariable=self.var_color)
        self.color.pack(pady=5)
        
        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana,textvariable=self.var_modelo)
        self.modelo.pack(pady=5)
        
        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana,textvariable=self.var_velocidad)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana,textvariable=self.var_potencia)
        self.potencia.pack(pady=5)
        
        Label(self.ventana,text="# de Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana,textvariable=self.var_asientos)
        self.asientos.pack(pady=5)
        
        self.btn_modificar=Button(self.ventana,text=":: Modificar ::",state="disabled",command=lambda: {self.modificar_coche_controller(),self.modificar_coche_view()})
        self.btn_modificar.pack(pady=5)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
    
    def cambiar_estado_btn(self, estado, tipo_accion):
        if estado:
            if tipo_accion=="eliminar":
                self.btn_eliminar.config(state="normal")
            elif tipo_accion=="modificar":
                self.btn_modificar.config(state="normal")
        else:
            if tipo_accion=="eliminar":
                self.btn_eliminar.config(state="disabled")
            elif tipo_accion=="modificar":
                self.btn_modificar.config(state="disabled")
                
    
    def confirmacion_eliminar(self, tipo_accion):
        resp=messagebox.askquestion(title="...¡Atencion!...",message=f"...¿Desea {tipo_accion} el registro?...")
        if resp=="yes":
            return True
        else:
            return False

    def eliminar_y_refrescar(self):
        self.eliminar_coche_controller()
        self.eliminar_coche_view()

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
        id=self.id.get()
        resp=self.confirmacion_eliminar("eliminar")
        if resp==True:
            respuesta=coches.Coches.eliminar(id)
        else:
            respuesta=False
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
        id = self.id.get()
        coche1 = coches.Coches.buscar(id)
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