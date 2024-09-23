import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesitas instalar tkcalendar (pip install tkcalendar)

# Clase para la aplicación de la agenda
class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame principal
        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(padx=10, pady=10)

        # Frame para la lista de eventos
        self.frame_lista = tk.Frame(self.frame_principal)
        self.frame_lista.grid(row=0, column=0, columnspan=3, pady=10)

        # Lista de eventos (TreeView)
        self.treeview = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings', height=8)
        self.treeview.column("Fecha", width=100)
        self.treeview.column("Hora", width=100)
        self.treeview.column("Descripción", width=300)

        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Hora", text="Hora")
        self.treeview.heading("Descripción", text="Descripción")

        self.treeview.pack(side="left")

        # Barra de desplazamiento
        self.scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.treeview.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.treeview.config(yscrollcommand=self.scrollbar.set)

        # Frame para la entrada de datos
        self.frame_entrada = tk.Frame(self.frame_principal)
        self.frame_entrada.grid(row=1, column=0, columnspan=3, pady=10)

        # Etiquetas y campos de entrada
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.entrada_fecha = DateEntry(self.frame_entrada, date_pattern='dd/mm/yyyy', width=15)
        self.entrada_fecha.grid(row=0, column=1, padx=10)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.entrada_hora = tk.Entry(self.frame_entrada)
        self.entrada_hora.grid(row=1, column=1, padx=10)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.entrada_descripcion = tk.Entry(self.frame_entrada, width=40)
        self.entrada_descripcion.grid(row=2, column=1, padx=10)

        # Frame para los botones
        self.frame_botones = tk.Frame(self.frame_principal)
        self.frame_botones.grid(row=2, column=0, columnspan=3, pady=10)

        # Botones
        self.boton_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.grid(row=0, column=0, padx=10)

        self.boton_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.grid(row=0, column=1, padx=10)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=root.quit)
        self.boton_salir.grid(row=0, column=2, padx=10)

    # Función para agregar un nuevo evento
    def agregar_evento(self):
        fecha = self.entrada_fecha.get()
        hora = self.entrada_hora.get()
        descripcion = self.entrada_descripcion.get()

        if fecha and hora and descripcion:
            self.treeview.insert('', 'end', values=(fecha, hora, descripcion))
            self.entrada_fecha.set_date(self.entrada_fecha.today())  # Reiniciar a la fecha actual
            self.entrada_hora.delete(0, tk.END)
            self.entrada_descripcion.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    # Función para eliminar un evento seleccionado
    def eliminar_evento(self):
        seleccion = self.treeview.selection()
        if seleccion:
            confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?")
            if confirmacion:
                self.treeview.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona un evento para eliminar.")

# Crear la ventana principal
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AgendaPersonal(ventana)
    ventana.mainloop()