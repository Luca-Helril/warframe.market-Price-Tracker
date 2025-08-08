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
from GUI2 import MyGUI2



class MyGUI:
    

    def __init__(self, buttons):
        self.root = tk.Tk()

        #Theme
        self.root.tk.call("source", "Azure/azure.tcl")
        self.root.tk.call("set_theme", "dark")

        self.root.geometry("900x600") # Demensionen
        self.root.title("Warframe Tracker")

        if 1== 2:
            for i in range(7):
                for j in range(3):
                    self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold'))

                    self.e.grid(row=i+4, column=j+2)
                    self.e.insert(END, "test")

        
        self.label = tk.Label(self.root, text="\n\n\n\n\n\n\n\n", font=('Arial', 15), anchor="w", justify=tk.LEFT)
        self.label.grid(sticky = N, row= 2, column= 2)

        textbox = tk.Text(self.root, height=1, font=('Arial', 18)) # height = wie fiele zeilen angezeigt werden
        textbox.grid(row= 3, column= 2) # Fügt das dextfelt hinzu
        # myentry = tk.Entry(root) # hat nur eine zeile

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
        #buttonframe.pack(padx=10, pady=10, fill='both', expand=True)

        #buttonframe.pack(fill='x') # streckt in die x demension
        buttonframe.grid(row=4, column=0, columnspan=5, sticky='nsew', padx=5, pady=5)
#

        #photo = PhotoImage(file= picture_path)
        #photoimage = photo.subsample(4, 4)
        
        self.images = [] # zum speichern der bilder damit sie nicht gelöscht werden wenn das programm den sie werden nichtmher gebaucht
        wiki = WarframeWiki()
        primes_List = wiki.get_primes_list()
        thisCount = 0
        for kategori in primes_List:
                for name in primes_List[kategori]:
                        if (thisCount <= buttons):
                            #print(name)
                            picture_name = name.lower().replace(" prime", "") + ".png"
                            #print(picture_name)
                            picture_path = r"D:\__ SAVES __\__PR__\Pictures" + "\\" + picture_name
                            #print(picture_path)
                            if os.path.exists(picture_path):
                                image = Image.open(picture_path)
                                image = image.resize((image.width // 1, image.height // 1))
                                photoimage = ImageTk.PhotoImage(image)
                                self.images.append(photoimage)
                
                                btn = tk.Button(buttonframe, text=name, image = photoimage, compound = LEFT, font=('Arial', 14), anchor="w", padx=10, command=lambda n=name: self.show_info(n)) # Without this, name would refer to the same variable across all buttons — so they'd all print the last name. Using lambda n=name: captures the current value of name.
                                zeile = thisCount // 5
                                spalte = thisCount % 5
                                btn.grid(row=zeile, column=spalte, sticky="nsew", padx=2, pady=2)
                                buttonframe.rowconfigure(zeile, weight=1)
                                thisCount += 1
                            else:
                                print(picture_path)
        anotherbutton = tk.Button(self.root, text="HOME", command = self.open_new_window) # Hat momentan keine funktion _________________________
        anotherbutton.place(x=1, y=1, height=50, width=100) # Plazirung von oben links

        self.root.mainloop()  # GUI-Schleife starten, damit wenn man button drückt auch etwas passirt


    def show_info(self, name):
        print(">")
        scrab = Scraping(name)
        info = scrab.get_all_info()
        info_String =""
        for item in info:
            info_String += f'{item + ": ":.<15}' + str(round(info.get(item)[0], 0)) + "\n"
        self.label.config(text=name + "\n" + info_String)
        
    def open_new_window(self):
        MyGUI2(self.root)



MyGUI(50)