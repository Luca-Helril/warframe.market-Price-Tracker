import tkinter as tk
from tkinter import messagebox
from Scraping import Scraping
from WarframeWiki import WarframeWiki

class MyGUI:
    

    def __init__(self, buttons):
        
        
        root = tk.Tk()

        root.geometry("1000x650") # Demensionen

        root.title("Warframe Tracker")
        
        self.label = tk.Label(root, text="", font=('Arial', 18))
        self.label.pack(padx=20, pady=20) # setzt distanz zwischen rand und den label und fügt es zur root dazu



        textbox = tk.Text(root, height=3, font=('Arial', 18)) # height = wie fiele zeilen angezeigt werden
        textbox.pack() # Fügt das dextfelt hinzu
        # myentry = tk.Entry(root) # hat nur eine zeile

        button = tk.Button(root, text="klick", font=('Arial', 18) )
        button.pack(padx=20, pady=20)

        buttonframe = tk.Frame(root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        buttonframe.columnconfigure(3, weight=1)
        buttonframe.columnconfigure(4, weight=1)
        #buttonframe.pack(padx=10, pady=10, fill='both', expand=True)


        buttonframe.pack(fill='x') # streckt in die x demension



        
        thisCount = 0
        for kategori in WarframeWiki.primes_List:
                for name in WarframeWiki.primes_List[kategori]:
                        if (thisCount <= buttons):
            
                            btn = tk.Button(buttonframe, text=name, font=('Arial', 14), command=lambda n=name: self.show_info(n)) # Without this, name would refer to the same variable across all buttons — so they'd all print the last name. Using lambda n=name: captures the current value of name.
                            zeile = thisCount // 5
                            spalte = thisCount % 5
                            btn.grid(row=zeile, column=spalte, sticky="news", padx=2, pady=2)
                            thisCount += 1
        anotherbutton = tk.Button(root, text="HOME")
        anotherbutton.place(x=1, y=1, height=50, width=100) # Plazirung von oben links

        root.mainloop()  # GUI-Schleife starten


    def show_info(self, name):
        scrab = Scraping(name)
        String1 = scrab.get_all_durchschitsspreis()
        #print("_____________________________________________________________")
        #print(name)
        print(String1)
        self.label.config(text=name + "\n" + String1)



        
        
        

MyGUI(50)