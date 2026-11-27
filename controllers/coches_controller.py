from models import coches_model

class CochesController:
##Controlador 

    def insertar_coche_controller(self):
        coches1 = coches_model.CochesModel(
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
            respuesta = coches_model.CochesModel.eliminar(id_coche)
        else:
            respuesta = False
        self.respuesta_sql(respuesta)

    def consultar_coche_controller(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in coches_model.CochesModel.consultar():
            self.tree.insert("", "end", values=row)

    def modificar_coche_controller(self):
        id_coche = self.id.get()
        coches1 = coches_model.CochesModel(
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
        coche1 = coches_model.CochesModel.buscar(id_coche)
        self.encontro(coche1, tipo_accion)