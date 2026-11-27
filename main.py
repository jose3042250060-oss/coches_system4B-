from tkinter import Tk
from views.coches_view import CochesView

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.coches_view = CochesView(self.ventana)


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()