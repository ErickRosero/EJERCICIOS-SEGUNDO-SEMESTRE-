import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campo de entrada para nuevas tareas
        self.task_input = tk.Entry(root, width=50)
        self.task_input.pack(pady=10)
        self.task_input.bind('<Return>', self.add_task)  # Añadir tarea al presionar Enter

        # Frame para los botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Botón para marcar como completada
        self.complete_button = tk.Button(button_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Listbox para mostrar las tareas
        self.task_listbox = Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Scrollbar para la lista de tareas
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Doble clic para marcar como completada
        self.task_listbox.bind('<Double-1>', self.complete_task)

    def add_task(self, event=None):
        """Añadir una nueva tarea a la lista."""
        task = self.task_input.get()
        if task:
            self.task_listbox.insert(END, task)  # Inserta la tarea en la lista
            self.task_input.delete(0, END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")  # Mensaje si está vacío

    def complete_task(self, event=None):
        """Marcar la tarea seleccionada como completada."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)  # Elimina la tarea de la lista
            self.task_listbox.insert(selected_task_index, f"{task} - Completada")  # Inserta la tarea completada
            self.task_listbox.itemconfig(selected_task_index, {'fg': 'green'})  # Cambia el color de la tarea completada
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")  # Mensaje si no hay selección

    def delete_task(self):
        """Eliminar la tarea seleccionada de la lista."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)  # Elimina la tarea
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")  # Mensaje si no hay selección


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

