import tkinter as tk
from GUI import BankGUI

# create root window
root = tk.Tk()
root.title("TM Banking App")

# create BankGUI object
bank_gui = BankGUI(root)

# run the main event loop
root.mainloop()