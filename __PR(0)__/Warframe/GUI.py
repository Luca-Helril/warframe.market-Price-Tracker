import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Scraping import Scraping
from WarframeWiki import WarframeWiki




class MyGUI:
    

    def __init__(self, buttons):
        
        root = tk.Tk()
        root.geometry("900x600") # Demensionen
        root.title("Warframe Tracker")

        if 1== 2:
            for i in range(7):
                for j in range(3):
                    self.e = Entry(root, width=20, fg='blue', font=('Arial',16,'bold'))

                    self.e.grid(row=i+4, column=j+2)
                    self.e.insert(END, "test")

        
        self.label = tk.Label(root, text="\n\n\n\n\n\n\n\n", font=('Arial', 15), anchor="w", justify=tk.LEFT)
        self.label.grid(sticky = N, row= 2, column= 2)

        textbox = tk.Text(root, height=1, font=('Arial', 18)) # height = wie fiele zeilen angezeigt werden
        textbox.grid(row= 3, column= 2) # Fügt das dextfelt hinzu
        # myentry = tk.Entry(root) # hat nur eine zeile

        # genauer nachschauen wie es funktionirt
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=1)
        root.columnconfigure(4, weight=1)
        root.rowconfigure(4, weight=1)

        buttonframe = tk.Frame(root) # erstellt einen Frame für Buttons
        buttonframe.columnconfigure(0, weight=1) # Spalte 0 sich beim Vergrößern mit anpasst
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        buttonframe.columnconfigure(3, weight=1)
        buttonframe.columnconfigure(4, weight=1)
        #buttonframe.pack(padx=10, pady=10, fill='both', expand=True)

        #buttonframe.pack(fill='x') # streckt in die x demension
        buttonframe.grid(row=4, column=0, columnspan=5, sticky='nsew', padx=5, pady=5)

        
        thisCount = 0
        for kategori in WarframeWiki.primes_List:
                for name in WarframeWiki.primes_List[kategori]:
                        if (thisCount <= buttons):
            
                            btn = tk.Button(buttonframe, text=name, font=('Arial', 14), command=lambda n=name: self.show_info(n)) # Without this, name would refer to the same variable across all buttons — so they'd all print the last name. Using lambda n=name: captures the current value of name.
                            zeile = thisCount // 5
                            spalte = thisCount % 5
                            btn.grid(row=zeile, column=spalte, sticky="nsew", padx=2, pady=2)
                            buttonframe.rowconfigure(zeile, weight=1)
                            thisCount += 1
        anotherbutton = tk.Button(root, text="HOME") # Hat momentan keine funktion _________________________
        anotherbutton.place(x=1, y=1, height=50, width=100) # Plazirung von oben links

        root.mainloop()  # GUI-Schleife starten, damit wenn man button drückt auch etwas passirt


    def show_info(self, name):
        print(">")
        scrab = Scraping(name)
        info = scrab.get_all_info()
        info_String =""
        for item in info:
            info_String += f'{item + ": ":.<15}' + str(round(info.get(item)[0], 0)) + "\n"

        self.label.config(text=name + "\n" + info_String)
        



MyGUI(50)