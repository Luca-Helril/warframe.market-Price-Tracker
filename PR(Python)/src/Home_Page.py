import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Scraping import Scraping
from WarframeWiki import WarframeWiki
from tkinter import Tk, Label
from PIL import Image, ImageTk
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import Image
from PIL import Image, ImageTk
from Warframe_Collection import Warframe_Collection


class HomeGUI:

    def __init__(self):
        self.root = tk.Tk()

        #Theme
        self.root.tk.call("source", "Azure/azure.tcl")
        self.root.tk.call("set_theme", "dark")

        self.root.geometry("900x600") # Demensionen
        self.root.title("Warframe Tracker")

        # Configure grid weights
        Grid.rowconfigure(self.root, 0, weight=1)
        for col in range(3): # für alle spalten
            Grid.columnconfigure(self.root, col, weight=1)

        width = 40
        height = 15

        btn1 = tk.Button(self.root, text="[|]", bg="teal", command= self.choose1, width = width, height=height).grid(row=0, column=0, sticky="new", padx=2,pady=2)
        btn2 = tk.Button(self.root, text="[|]", bg="teal", command= self.choose2, width = width, height=height).grid(row=0, column=1, sticky="new", padx=2,pady=2)
        btn3 = tk.Button(self.root, text="[|]", bg="teal", command= self.choose3, width = width, height=height).grid(row=0, column=2, sticky="new", padx=2,pady=2)
        
        lbl=Label(self.root,text="Pick a Decade",font=  ("Times","40","bold italic"))
        lbl.grid(row=1,column=0)


        self.root.mainloop()  # GUI-Schleife starten, damit wenn man button drückt auch etwas passirt

    # later to call warframe_collection
    def choose1(self):
        print("button 1")

    # later to call Gui
    def choose2(self):
        print("button 2")

    # later to call Sreen_scant -> png_text_extractor
    def choose3(self):
        print("button 3")

HomeGUI()