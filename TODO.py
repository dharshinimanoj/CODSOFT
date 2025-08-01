import tkinter as tk
from tkinter import messagebox
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List App")
        self.root.geometry("400x450")
        self.tasks = []

        # Title
        tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold")).pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        # Add Button
        tk.Button(root, text="Add Task", width=20, command=self.add_task).pack()

        # Task Listbox
        self.task_listbox = tk.Listbox(root, height=15, width=40, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)

        # Buttons for delete and mark done
        tk.Button(root, text="Mark as Done", width=20, command=self.mark_done).pack(pady=2)
        tk.Button(root, text="Delete Task", width=20, command=self.delete_task).pack(pady=2)

        # Load previous tasks if any
        self.load_tasks()

        # Save tasks on exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            if not task.endswith(" ✅"):
                self.tasks[selected_index] = task + " ✅"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file]
                self.update_task_list()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
