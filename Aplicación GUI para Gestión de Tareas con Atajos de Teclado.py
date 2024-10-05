import tkinter as tk
from tkinter import messagebox, simpledialog


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Lista para almacenar las tareas
        self.tasks = []

        # Frame principal
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(padx=10)

        # Botón para añadir tareas
        self.add_task_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(padx=10, pady=10)

        # Botones de gestión de tareas
        self.complete_task_button = tk.Button(self.frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Asignación de atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_index]
            self.tasks[selected_index] = f"{completed_task} (Completada)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()
