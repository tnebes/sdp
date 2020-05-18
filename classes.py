import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass

class My_Checkbutton():
    """Creates a checkbutton. Variable is .var, button itself is .the_button."""
    def __init__(self, location, my_text, column, row, sticky="NSEW"):
        self.var = tk.IntVar()
        self.the_button = tk.Checkbutton(location, text=my_text, variable=self.var)
        self.the_button.grid(column=column, row=row, sticky=sticky)

class My_Entry():
    """Creates an entry box. Variable is .var, entry is .the_entry."""
    def __init__(self, location, width, column, row, padx=0, pady=0):
        self.var = tk.StringVar()
        # janky
        self.the_entry = ttk.Entry(location, width=width, textvariable=self.var)
        self.the_entry.grid(column=column, row=row, padx=padx, pady=pady)

class My_Label():
    """Creates a label. .the_label"""
    def __init__(self, location, text, column, row, pady=0, sticky="NSEW"):
        self.the_label = ttk.Label(location, text=text)
        self.the_label.grid(column=column, row=row, pady=pady, sticky=sticky)

class My_Button():
    """Creates a button. .the_button"""
    def __init__(self, location, text, column, row, sticky="NSEW"):
        self.the_button = tk.Button(location, text=text)
        self.the_button.grid(column=column, row=row, sticky=sticky)

class My_Listbox():
    """Creates a listbox. .the_listbox"""
    def __init__(self, location, height, width, column, row):
        self.the_listbox = tk.Listbox(location, height=height, width=width)
        self.the_listbox.grid(column=column, row=row)

class My_Text():
    """Creates a textbox. .the_text"""
    def __init__(self, location, width, height, column, row, sticky="NSEW"):
        self.the_text = tk.Text(location, width=width, height=height)
        self.the_text.grid(column=column, row=row, sticky=sticky)

@dataclass
class My_Tab():
    """A class used for storing references to GUI objects in a tab"""
    name: str

        
        

