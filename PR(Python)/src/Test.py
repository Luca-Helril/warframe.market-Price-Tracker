import requests
from bs4 import BeautifulSoup
from WarframeWiki import WarframeWiki
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Scraping import Scraping

import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Scraping import Scraping
from WarframeWiki import WarframeWiki

from tkinter.ttk import *
import os

class MyGUI:
    def __init__(self, buttons):
        self.root = tk.Tk()

        self.root.tk.call("source", "Azure/azure.tcl")
        self.root.tk.call("set_theme", "dark")

        self.root.geometry("900x600")
        self.root.title("Warframe Tracker")

        # genauer nachschauen wie es funktionirt
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.rowconfigure(4, weight=1)

        buttonframe = tk.Frame(self.root) # erstellt einen Frame für Buttons
        buttonframe.columnconfigure(0, weight=1) # Spalte 0 sich beim Vergrößern mit anpasst
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        buttonframe.columnconfigure(3, weight=1)
        buttonframe.columnconfigure(4, weight=1)

        buttonframe.grid(row=4, column=0, columnspan=5, sticky='nsew', padx=5, pady=5)

        #photo = PhotoImage(file=r"D:\__ SAVES __\__PR__\64px-NidusPrimeIcon272.png")
        photo = PhotoImage(file="bild2.png")



        photoimage = photo.subsample(3, 3)

        thisCount = 0
        for kategori in WarframeWiki.primes_List:
                for name in WarframeWiki.primes_List[kategori]:
                        if (thisCount <= buttons):
            
                            btn = tk.Button(buttonframe, text=name, image = photoimage, compound = LEFT, font=('Arial', 14), command=lambda n=name: self.show_info(n)) # Without this, name would refer to the same variable across all buttons — so they'd all print the last name. Using lambda n=name: captures the current value of name.
                            zeile = thisCount // 5
                            spalte = thisCount % 5
                            btn.grid(row=zeile, column=spalte, sticky="nsew", padx=2, pady=2)
                            buttonframe.rowconfigure(zeile, weight=1)
                            thisCount += 1
        anotherbutton = tk.Button(self.root, text="HOME") # Hat momentan keine funktion _________________________
        anotherbutton.place(x=1, y=1, height=50, width=100)

        self.root.mainloop()


MyGUI(50)



