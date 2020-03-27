import tkinter as tk

def order_method():
    # 1 = Pick Up (No extra cost)
    # 2 = Delivery ($3)
    
    if(var.get() == 1):
        return(0)
    else:
        return(3)

def calculate_cost():
    cost = 0
    cost = cost + order_method()
    cost_label.configure(text="${}".format(cost))


root = tk.Tk()

title_label = tk.Label(root, text="Pizza Ordering\nSystem")
title_label.grid(row = 0, column = 0, columnspan = 2)

var = tk.IntVar()
var.set(0)

pizza_options = []
f = open("pizzas.txt","r")
for i in f:
    pizza = i.split(",")
    pizza_options.append(pizza[0])
f.close()

pizza = tk.StringVar(root)
pizza.set(pizza_options[0])

pickup_radiobutton = tk.Radiobutton(root, text="Pick Up", variable =var, value=1)
pickup_radiobutton.grid(row = 1, column = 0)
delivery_radiobutton = tk.Radiobutton(root, text="Delivery", variable = var, value=2)
delivery_radiobutton.grid(row = 1, column = 1)

pizza_one = tk.OptionMenu(root, pizza, *pizza_options)
pizza_one.grid(row = 2, column = 0)

pizza_two = tk.OptionMenu(root, pizza, *pizza_options)
pizza_two.grid(row = 3, column = 0)

pizza_three = tk.OptionMenu(root, pizza, *pizza_options)
pizza_three.grid(row = 4, column = 0)

pizza_four = tk.OptionMenu(root, pizza, *pizza_options)
pizza_four.grid(row = 5, column = 0)

pizza_five = tk.OptionMenu(root, pizza, *pizza_options)
pizza_five.grid(row = 6, column = 0)

cost_title = tk.Label(root, text="Price:")
cost_title.grid(row = 7, column = 0)

cost_label = tk.Label(root, text="")
cost_label.grid(row = 7, column = 1)

order_button = tk.Button(root, text="Calculate", command = calculate_cost)
order_button.grid(row = 8, column = 0, columnspan = 2)

root.mainloop()