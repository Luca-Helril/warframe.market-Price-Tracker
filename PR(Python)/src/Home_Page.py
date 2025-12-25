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
from Price_Tracker import Price_Tracker


class HomeGUI:

    def __init__(self, root):
        self.root = root


        self.root.geometry("900x600") # Demensionen
        self.root.title("Warframe Tracker")

        # Configure grid weights
        Grid.rowconfigure(self.root, 0, weight=1)
        for col in range(3): # für alle spalten
            Grid.columnconfigure(self.root, col, weight=1)

        width = 40
        height = 15

        btn1 = tk.Button(self.root, text="Price Tracker", bg="teal", command= self.choose1, width = width, height=height).grid(row=0, column=0, sticky="new", padx=2,pady=2)
        btn2 = tk.Button(self.root, text="Collection", bg="teal", command= self.choose2, width = width, height=height).grid(row=0, column=1, sticky="new", padx=2,pady=2)
        btn3 = tk.Button(self.root, text="Screen scan", bg="teal", command= self.choose3, width = width, height=height).grid(row=0, column=2, sticky="new", padx=2,pady=2)
        
        lbl=Label(self.root,text="",font=  ("Times","40","bold italic"))
        lbl.grid(row=1,column=0)


    # later to call Price Tracker
    def choose1(self):
        print("button 1")
        self.root.withdraw()
        Price_Tracker(self.root, 70)


    # later to call warframe_collection
    def choose2(self):
        print("button 2")
        self.root.withdraw()    
        Warframe_Collection(self.root)
        

    # later to call Sreen_scant -> png_text_extractor
    def choose3(self):
        print("button 3")
        self.root.withdraw()  

if __name__ == "__main__":
    root = tk.Tk()#
    root.tk.call("source", "Azure/azure.tcl")
    root.tk.call("set_theme", "dark")
    HomeGUI(root)
    root.mainloop() # GUI-Schleife starten, damit wenn man button drückt auch etwas passirt

      