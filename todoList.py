import tkinter as tk

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

# Function to mark a task as completed
def mark_completed():
    selected_task = task_list.get(tk.ACTIVE)
    if selected_task:
        task_list.delete(tk.ACTIVE)
        completed_list.insert(tk.END, selected_task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget to add tasks
entry = tk.Entry(root)
entry.pack(pady=10)

# Create buttons to add tasks and mark tasks as completed
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
complete_button = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_button.pack()

# Create a listbox to display tasks and completed tasks
task_list = tk.Listbox(root)
task_list.pack()
completed_list = tk.Listbox(root)
completed_list.pack()

root.mainloop()
