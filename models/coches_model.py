import os
os.system("cls" if os.name == "nt" else "clear")
from conexionBD import conexion, cursor 

class CochesModel():
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potencia=potencia
        self._asientos=asientos

    def Acelerar(self):
        self._velocidad+=1

    def insertar(self):
        try:
            sql = "INSERT INTO coches VALUES (null, %s, %s, %s, %s, %s, %s)"
            valores = (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from coches where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def buscar(id):
        try:
            cursor.execute("select * from coches where id=%s",(id,))
            return cursor.fetchall()
        except:
            return []

    def actualizar(self, id):
        try:
            sql = "UPDATE coches SET marca = %s, color = %s, modelo = %s, velocidad = %s, potencia = %s, asientos = %s WHERE id = %s"
            valores = (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def Frenar(self):
        self._velocidad-=1

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca=marca

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color=color

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self,modelo):
        self._modelo=modelo

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self,potencia):
        self._potencia=potencia

    @property
    def asientos(self):
        return self._asientos

    @asientos.setter
    def asientos(self,asientos):
        self._asientos=asientos

class Camiones(CochesModel):
    def __init__(self, color, marca, velocidad, modelo, potencia, plazas,eje,capacidadCarga):
        super().__init__(marca=marca, color=color, modelo=modelo, velocidad=velocidad, potencia=potencia, asientos=plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    def cargar(self,tipo_cargar):
        print(f"El tipo de carga del camion es: {tipo_cargar}")

    def Acelerar(self):
        self._velocidad+=1
        print(f"Estoy acelerando como un camion")

    def Frenar(self):
        self._velocidad-=1
        print(f"Estoy frenando como un camion")

    @property
    def eje(self):
        return self.__eje

    @eje.setter
    def eje(self, eje):
        self.__eje = eje

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga

    @capacidadCarga.setter
    def capacidadCarga(self, capacidadCarga):
        self.__capacidadCarga = capacidadCarga
