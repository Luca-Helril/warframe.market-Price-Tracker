import pickle
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

import tkinter as tk
from tkinter import ttk



class MyGUI2:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Daten Sammlung")
        self.window.geometry("900x600")

        
        

        close_btn = ttk.Button(self.window, text="Close", command=self.window.destroy)
        close_btn.pack(pady=10)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        #self.window.columnconfigure(4, weight=1)
        #self.window.rowconfigure(4, weight=1)

        buttonframe = tk.Frame(self.window)
        for i in range(5):
            buttonframe.columnconfigure(i, weight=1)

        wf = WarframeWiki()
        primes_List = wf.get_primes_list()
        owed_list = wf.get_owned_list()

        self.images = []

        buttongröße = 1
        font_size = 10
        thisCount = 0


        for kategori in primes_List:
            for name in primes_List[kategori]:
                picture_name = name.lower().replace(" prime", "") + ".png"
                #print(picture_name)
                picture_path = r"D:\__ SAVES __\__PR__\Pictures" + "\\" + picture_name
                if os.path.exists(picture_path):
                    zeile = thisCount // 5

                    # Image
                    image = Image.open(picture_path)
                    image = image.resize((image.width // 1, image.height // 1))
                    photoimage = ImageTk.PhotoImage(image)
                    self.images.append(photoimage)
                    
                    # Warframe Buttons
                    self.btn1 = tk.Button(buttonframe, text=name, width=buttongröße, height=2,
                             image=photoimage, compound=LEFT, font=('Arial', font_size),
                             anchor="w", padx=5)
                            
                    self.btn1.grid(row=zeile, column=0, sticky="nsew", padx=2, pady=2)

                    # Bauteil Buttons
                    bauteil_list = ["blueprint", "chassis", "neuroptics", "system"]
                    thisCount2 = 1
                    for bauteil in bauteil_list:
                        besitz_zustand = owed_list[kategori][name][bauteil]
                        
                        btn2 = tk.Button(buttonframe,text=bauteil, width=buttongröße, height=2, font=('Arial', font_size), anchor="w", padx=5)
                        
                        btn2.grid(row=zeile, column=thisCount2, sticky="nsew", padx=2, pady=2)
                        btn2.config(command=lambda k=kategori, n=name, b=bauteil, wf=wf, btn=btn2: self.change_state(k, n, b, wf, btn))
                        if besitz_zustand:
                            btn2.config(bg='gray50')

                        thisCount2 += 1
                         
                    buttonframe.rowconfigure(zeile, weight=1)
                    thisCount += 1

        buttonframe.pack(expand=True, fill='both')

    def change_state(self, kategori, name, bauteil, warframeWki, btn):
        owned = warframeWki.get_owned_list()
        current = owned[kategori][name][bauteil]
        new_zustand = not current

        warframeWki.set_owed(kategori, name, bauteil, new_zustand)

        # link zu farben https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
        if new_zustand:
            btn.config(bg='gray50')
        else:
            btn.config(bg=ttk.Style().lookup('TButton', 'background'))
        

        print(warframeWki.get_owned_list()[kategori][name][bauteil])




