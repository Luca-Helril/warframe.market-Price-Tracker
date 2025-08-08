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
        self.window.columnconfigure(4, weight=1)
        self.window.rowconfigure(4, weight=1)

        buttonframe = tk.Frame(self.window)
        for i in range(6):
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
                    image = Image.open(picture_path)
                    image = image.resize((image.width // 1, image.height // 1))
                    photoimage = ImageTk.PhotoImage(image)
                    self.images.append(photoimage)
                    
                    zeile = thisCount // 5

                    self.btn1 = tk.Button(buttonframe, text=name, width=buttongröße, height=2,
                             image=photoimage, compound=LEFT, font=('Arial', font_size),
                             anchor="w", padx=5, command=lambda n=name, k="bauteil": self.change_state(n, k)) 
                    
                    self.btn1.grid(row=zeile, column=0, sticky="nsew", padx=2, pady=2)
                    
                    
                    bauteil_list = ["set", "blueprint", "chassis", "neuroptics", "system"]
                    thisCount2 = 1
                    for bauteil in bauteil_list:
                        self.btn2 = tk.Button(buttonframe, text=bauteil, width=buttongröße, height=2,
                            font=('Arial', font_size),
                            anchor="w", padx=5, command=lambda n=name, k=bauteil: self.change_state(n, k))
                        
                        self.btn2.grid(row=zeile, column=thisCount2, sticky="nsew", padx=2, pady=2)
                        thisCount2 += 1
                    
                    buttonframe.rowconfigure(zeile, weight=1)
                    thisCount += 1

        buttonframe.pack(expand=True, fill='both')

    def change_state(self, name, bauteil):
        print("funktionirt " + name + ": " + bauteil)    
