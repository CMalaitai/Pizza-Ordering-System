import tkinter as tk
import pizzas

def order_method():
    # 1 = Pick Up (No extra cost)
    # 2 = Delivery ($3)
    
    if(var.get() == 1):
        return(0)
    else:
        return(3)

def calculate_cost():
    print()

def pizza_list():
    file = open("pizzas.txt", "r")
    pizza_menu = []

    for pizza in file:
        p = pizza.split(",")
        pizza_menu.append(p[0])
    
    return pizza_menu

def window(var):
    root = tk.Tk()

    cost = 0

    if(var == 2):
        cost = cost + 3

    pizza_one = tk.StringVar()
    pizza_two = tk.StringVar()
    pizza_three = tk.StringVar()
    pizza_four = tk.StringVar()
    pizza_five = tk.StringVar()

    pizza_one.set("Please select a pizza")
    pizza_two.set("Please select a pizza")
    pizza_three.set("Please select a pizza")
    pizza_four.set("Please select a pizza")
    pizza_five.set("Please select a pizza")

    pizza_menu = pizza_list()

    pizza_one = tk.OptionMenu(root, pizza_one, *pizza_menu)
    pizza_one.grid(row = 2, column = 0)

    pizza_two = tk.OptionMenu(root, pizza_two, *pizza_menu)
    pizza_two.grid(row = 3, column = 0)

    pizza_three = tk.OptionMenu(root, pizza_three, *pizza_menu)
    pizza_three.grid(row = 4, column = 0)

    pizza_four = tk.OptionMenu(root, pizza_four, *pizza_menu)
    pizza_four.grid(row = 5, column = 0)

    pizza_five = tk.OptionMenu(root, pizza_five, *pizza_menu)
    pizza_five.grid(row = 6, column = 0)

    cost_title = tk.Label(root, text="")
    cost_title.grid(row = 7, column = 0)

    cost_title.configure(text = "Price: ${}".format(str(cost)))

    order_button = tk.Button(root, text="Calculate", command = calculate_cost)
    order_button.grid(row = 8, column = 0, columnspan = 2)

    root.mainloop()