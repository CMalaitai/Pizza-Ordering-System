import tkinter as tk
from details import window_one, window_two

def create_order():
    root.destroy()
    if(var.get()==1):
        window_one()
    else:
        window_two()

root = tk.Tk()

root.title("Pizza Ordering System")

var = tk.IntVar()
var.set(0)

title_label = tk.Label(root, text="Pizza Ordering\nSystem", font=("Times New Roman",20))
title_label.grid(row = 0, column = 0, columnspan = 2)

pickup_radiobutton = tk.Radiobutton(root, text="Pick Up", variable = var, value=1)
pickup_radiobutton.grid(row = 1, column = 0)

delivery_radiobutton = tk.Radiobutton(root, text="Delivery", variable = var, value=2)
delivery_radiobutton.grid(row = 1, column = 1)

button = tk.Button(root, text = "GO", command = create_order)
button.grid(row = 2, column = 0, columnspan = 2)

root.mainloop()