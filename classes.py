import tkinter as tk
from tkinter import ttk

class My_Checkbutton():
    """Creates a checkbutton. Variable is .var, button itself is .the_button."""
    def __init__(self, location, my_text):
        self.var = tk.IntVar()
        self.the_button = tk.Checkbutton(location, text=my_text, variable=self.var)
