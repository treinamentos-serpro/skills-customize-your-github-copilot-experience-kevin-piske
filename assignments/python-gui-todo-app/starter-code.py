import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.root.geometry("420x420")

        self.tasks = []

        self.task_label = tk.Label(root, text="Nova tarefa:")
        self.task_label.pack(pady=(10, 5))

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Adicionar", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remover Selecionada", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.task_list = tk.Listbox(root, width=50, height=15)
        self.task_list.pack(pady=10)

        self.status_var = tk.StringVar(value="Pronto para começar!")
        self.status_label = tk.Label(root, textvariable=self.status_var, fg="darkgreen")
        self.status_label.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            self.status_var.set("Digite uma tarefa antes de adicionar.")
            return

        self.tasks.append(task)
        self.task_list.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
        self.status_var.set(f"Tarefa adicionada: {task}")

    def remove_task(self):
        selected_index = self.task_list.curselection()
        if not selected_index:
            self.status_var.set("Selecione uma tarefa para remover.")
            return

        index = selected_index[0]
        task = self.task_list.get(index)
        self.task_list.delete(index)
        self.tasks.remove(task)
        self.status_var.set(f"Tarefa removida: {task}")


def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
