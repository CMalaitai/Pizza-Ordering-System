import tkinter as tk
import intro


def go_back():

    root.destroy()
    intro

def window_one():
    # Pick up details
    
    root = tk.Tk()

    root.title("Details for Pickup")
    
    name_label = tk.Label(root, text = "Name")
    name_label.grid(row = 0, column = 0)
    
    name_entry = tk.Entry(root)
    name_entry.grid(row = 0, column = 1)

    back_button = tk.Button(root, text = "Go Back", command = go_back)
    back_button.grid(row = 1, column = 0)

    submit_button = tk.Button(root, text = "Submit")
    submit_button.grid(row = 1, column = 1)

    file = open("customer.txt", "a+")
    file.write("p,{}".format(name_entry.get()))
    file.close()

    root.mainloop()

def window_two():
    # Delivery details
    
    root = tk.Tk()

    root.title("Details for Delivery")

    name_label = tk.Label(root, text = "Name")
    name_label.grid(row = 0, column = 0)
    
    name_entry = tk.Entry(root)
    name_entry.grid(row = 0, column = 1)

    address_label = tk.Label(root, text = "Address")
    address_label.grid(row = 1, column = 0)
    
    address_entry = tk.Entry(root)
    address_entry.grid(row = 1, column = 1)

    phone_label = tk.Label(root, text = "Phone Number")
    phone_label.grid(row = 2, column = 0)
    
    phone_entry = tk.Entry(root)
    phone_entry.grid(row = 2, column = 1)

    submit_button = tk.Button(root, text = "Submit")
    submit_button.grid(row = 3, column = 0, columnspan = 2)

    file = open("customer.txt", "a+")
    file.write("d,{},{},{}".format(name))
    file.close()

    root.mainloop()