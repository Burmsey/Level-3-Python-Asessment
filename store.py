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

        self.home_screen.grid(row=0, column=0, padx=100, pady=100, sticky="ew")

        
        self.title_label = Label(self.home_screen, text="Welcome to the Store!")
        self.menu = Button(self.home_screen, text="Menu", command=self.open_menu).pack(pady=20)


        # self.title_label.grid(row=1, column=0, padx=100, pady=20)
        # self.menu.grid(row=2, column=0, padx=100, pady=20)
        
        

    def open_menu(self):
        pass  # Placeholder for menu functionality

if __name__ == "__main__":
    root = Tk()
    store = Store(root)
    root.mainloop()
# This code creates a simple Tkinter GUI application with a welcome message and a button to open a menu.