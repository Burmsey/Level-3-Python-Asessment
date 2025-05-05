from tkinter import *
from tkinter import messagebox

class Menu:
    def __init__(self):
        pass

class Store:
    def __init__(self, root):
        self.root = root
        self.root.title("Burger Joint")
        self.home_screen = Frame(root)
        self.delivery_frame = Frame(root)

        self.home_screen.grid(row=0, column=0, padx=100, pady=100, sticky="ew")

        
        self.title_label = Label(self.home_screen, text="Welcome to the Store!")
        self.delivery = Button(self.home_screen, text="Delivery", command=self.delivery_order)
        self.pickup = Button(self.home_screen, text="Pickup", command=self.pickup_order)

        self.title_label.grid(row=0, column=1, padx=10, pady=10)
        self.pickup.grid(row=2, column=0, padx=5, pady=5)
        self.delivery.grid(row=2, column=2, padx=5, pady=5)

    def delivery_order(self):
        self.order_type = "delivery"
        self.menu()
    def pickup_order(self):
        self.order_type = "pickup"
        self.menu()


    def menu(self):
        self.home_screen.grid_forget()
        self.delivery_frame.grid(row=0, column=0, padx=100, pady=100, sticky="ew")

        self.text = Label(self.delivery_frame, text="Menu Options")

        self.drink_var = StringVar() 
        self.drinks_label = Label(self.delivery_frame, text="Drinks")
        self.drinks_dropdown = OptionMenu(self.delivery_frame, self.drink_var, "Coke", "Sprite")
        self.main_label = Label(self.delivery_frame, text="Main")
        self.main_dropdown = OptionMenu(self.delivery_frame, StringVar(), "Pizza", "Burger", "Salad")
        self.sides_label = Label(self.delivery_frame, text="Sides")
        self.sides_dropdown = OptionMenu(self.delivery_frame, StringVar(), "Fries")

        self.show_btn = Button(self.delivery_frame, text="Show Drink", command=self.show)
        self.show_btn.grid(row=3, column=0, padx=5, pady=5)

        self.lbl = Label(self.delivery_frame, text="")

        self.text.grid(row=0, column=1, padx=10, pady=10)

        self.drinks_label.grid(row=1, column=0, padx=5, pady=5)
        self.drinks_dropdown.grid(row=2, column=0, padx=5, pady=5)

        self.main_label.grid(row=1, column=1, padx=5, pady=5)
        self.main_dropdown.grid(row=2, column=1, padx=5, pady=5)

        self.sides_label.grid(row=1, column=2, padx=5, pady=5)
        self.sides_dropdown.grid(row=2, column=2, padx=5, pady=5)   

    def show(self):
        selected_drink = self.drink_var.get()
        self.lbl.config(text=f"Selected Drink: {selected_drink}")
        print(selected_drink)
            
            
        
        

    def open_menu(self):
        pass  # Placeholder for menu functionality

if __name__ == "__main__":
    root = Tk()
    store = Store(root)
    root.mainloop()
# This code creates a simple Tkinter GUI application with a welcome message and a button to open a menu.