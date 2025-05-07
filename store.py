from tkinter import *
from tkinter import messagebox

class Cart:
    def __init__(self, drinks, mains, sides):
        self.drinks = drinks
        self.mains = mains
        self.sides = sides
        pass
        #store name, address, phone number in here?

class Store:
    def __init__(self, root):
        self.root = root
        self.root.title("Burger Joint")
        self.home_screen = Frame(root)
        self.delivery_frame = Frame(root)

        self.items_in_cart = []

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

        self.drink_choice = StringVar() 
        self.main_choice = StringVar()
        self.sides_choice = StringVar()
        self.drinks_label = Label(self.delivery_frame, text="Drinks")
        self.drinks_dropdown = OptionMenu(self.delivery_frame, self.drink_choice, "Coke", "Sprite")
        self.main_label = Label(self.delivery_frame, text="Main")
        self.main_dropdown = OptionMenu(self.delivery_frame, self.main_choice, "Pizza", "Burger", "Salad")
        self.sides_label = Label(self.delivery_frame, text="Sides")
        self.sides_dropdown = OptionMenu(self.delivery_frame, self.sides_choice, "Fries")

        self.show_btn = Button(self.delivery_frame, text="Add To Cart", command=self.added_to_cart)
        self.cart = Button(self.delivery_frame, text="Show Cart", command=self.show_cart)
        self.show_btn.grid(row=4, columnspan=6, padx=5, pady=5)
        self.cart.grid(row=5, columnspan=6, padx=5, pady=5)

        self.drink_choice_clear = Button(self.delivery_frame, text="Clear", command=self.drinks_clear)
        self.main_choice_clear = Button(self.delivery_frame, text="Clear", command=self.main_clear)
        self.sides_choice_clear = Button(self.delivery_frame, text="Clear", command=self.sides_clear)

        self.drinks_label.grid(row=1, column=0, padx=5, pady=5)
        self.drinks_dropdown.grid(row=2, column=0, padx=5, pady=5)
        self.drink_choice_clear.grid(row=3, column=0, padx=5, pady=5)

        self.main_label.grid(row=1, column=1, padx=5, pady=5)
        self.main_dropdown.grid(row=2, column=1, padx=5, pady=5)
        self.main_choice_clear.grid(row=3, column=1, padx=5, pady=5)

        self.sides_label.grid(row=1, column=2, padx=5, pady=5)
        self.sides_dropdown.grid(row=2, column=2, padx=5, pady=5)   
        self.sides_choice_clear.grid(row=3, column=2, padx=5, pady=5)

    def added_to_cart(self):
        self.cart = []
        drink = self.drink_choice.get()
        main = self.main_choice.get()
        sides = self.sides_choice.get()

        self.items_in_cart.append(Cart(drink, main, sides))

        self.drink_choice.set("")
        self.main_choice.set("")
        self.sides_choice.set("")
    
    def show_cart(self):
        coke = 0
        sprite = 0
        pizza = 0
        burger = 0
        salad = 0
        fries = 0

        for cart_item in self.items_in_cart:
            if cart_item.drinks == "Coke":
                coke += 1
            elif cart_item.drinks == "Sprite":
                sprite += 1

            if cart_item.mains == "Pizza":
                pizza += 1
            elif cart_item.mains == "Burger":
                burger += 1
            elif cart_item.mains == "Salad":
                salad += 1

            if cart_item.sides == "Fries":
                fries += 1

        print(f"Coke: {coke}x, Sprite: {sprite}x, Pizza: {pizza}x, Burger: {burger}x, Salad: {salad}x, Fries: {fries}x")

    
    def drinks_clear(self):
        self.drink_choice.set("")
    
    def main_clear(self):
        self.main_choice.set("")
    
    def sides_clear(self):
        self.sides_choice.set("")

            
            
        
        

    def open_menu(self):
        pass  # Placeholder for menu functionality

if __name__ == "__main__":
    root = Tk()
    store = Store(root)
    root.mainloop()
# This code creates a simple Tkinter GUI application with a welcome message and a button to open a menu.
