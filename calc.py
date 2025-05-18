import tkinter as tk

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result = "Error! Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for entering numbers
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

entry_num1.pack()
entry_num2.pack()

# Radio buttons for selecting the operation
operation_var = tk.StringVar()
operation_var.set("Add")

add_radio = tk.Radiobutton(root, text="Add", variable=operation_var, value="Add")
subtract_radio = tk.Radiobutton(root, text="Subtract", variable=operation_var, value="Subtract")
multiply_radio = tk.Radiobutton(root, text="Multiply", variable=operation_var, value="Multiply")
divide_radio = tk.Radiobutton(root, text="Divide", variable=operation_var, value="Divide")

add_radio.pack()
subtract_radio.pack()
multiply_radio.pack()
divide_radio.pack()

# Button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Label to display the result
result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
