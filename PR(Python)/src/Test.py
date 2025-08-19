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
import glob


import tkinter as tk
from tkinter import ttk, LEFT
from PIL import Image, ImageTk
import os

class MyGUI2:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Daten Sammlung")
        self.window.geometry("900x600")

        # wenn gerückt wird wird das window geschlossen
        close_btn = ttk.Button(self.window, text="Close", command=self.window.destroy)
        close_btn.pack(pady=10)


        wf = WarframeWiki()
        primes_List = wf.get_primes_list()
        owed_list = wf.get_owned_list()

        # https://www.youtube.com/watch?v=0WafQCaok6g

        # Main frame
        main_frame = Frame(self.window)
        main_frame.pack(fill = BOTH, expand=1)

        # canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill = BOTH, expand=1)


        # scrollbar for canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # configure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))


        # another frame inside canvas
        second_frame = Frame(my_canvas)

        # add taht new frame to a wondow in the canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        for i in range(5):  # Spalte 0 = Name, Spalte 1-4 = Teile
            second_frame.grid_columnconfigure(i, weight=1)

        counter = 1
        for kategori in primes_List:
            for name in primes_List[kategori]:
                Button(second_frame, text=name).grid(row=counter, column=0, sticky="ew", padx=2, pady=2)
                
                bauteil_list = ["blueprint", "chassis", "neuroptics", "system"]
                counter2 = 1
                for item in bauteil_list:
                    Button(second_frame, text=item).grid(row=counter, column=counter2, sticky="ew", padx=2, pady=2)
                    counter2 += 1


                counter += 1





        

    # Der boolean value für die bauteile wird geändert und in bezihung dazu auch die farbe der buttons
    def change_state(self, kategori, name, bauteil, warframeWki, btn):
        
        owned = warframeWki.get_owned_list()
        current = owned[kategori][name][bauteil] # Ture oder False wert
        new_zustand = not current

        warframeWki.set_owed(kategori, name, bauteil, new_zustand) # setzt den boolean auf das gegenteil als was er forher wahr

        # link zu farben https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
        if new_zustand:
            btn.config(bg='gray50') # Tue
        else:
            btn.config(bg=ttk.Style().lookup('TButton', 'background')) # False (Defaoult color)
        
        #print(warframeWki.get_owned_list()[kategori][name][bauteil])



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hauptfenster verstecken
    root.tk.call("source", "Azure/azure.tcl")
    root.tk.call("set_theme", "dark")
    MyGUI2(root)     # GUI2 öffnen
    root.mainloop()