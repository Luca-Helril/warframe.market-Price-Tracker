import tkinter as tk
from tkinter import messagebox
from Scraping import Scraping
from WarframeWiki import WarframeWiki

class MyGUI:
    

    def __init__(self, buttons):
        
        
        root = tk.Tk()

        root.geometry("1050x700") # Demensionen

        root.title("Warframe Tracker")
        
        self.label = tk.Label(root, text="", font=('Arial', 15))
        self.label.grid(row= 1, column= 2)



        textbox = tk.Text(root, height=1, font=('Arial', 18)) # height = wie fiele zeilen angezeigt werden
        textbox.grid(row= 2, column= 2) # Fügt das dextfelt hinzu
        # myentry = tk.Entry(root) # hat nur eine zeile


        buttonframe = tk.Frame(root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        buttonframe.columnconfigure(3, weight=1)
        buttonframe.columnconfigure(4, weight=1)
        #buttonframe.pack(padx=10, pady=10, fill='both', expand=True)


        #buttonframe.pack(fill='x') # streckt in die x demension
        buttonframe.grid(row=3, column=0, columnspan=5, sticky='ew', padx=5, pady=5)




        
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
        print("_________________________________________________________")
        scrab = Scraping(name)
        #String1 = scrab.get_all_durchschitsspreis()
        #print("_____________________________________________________________")
        #print(name)
        #print(String1)
        #self.label.config(text=name + "\n" + String1)
        info = scrab.get_all_info()
        info_String =""
        for item in info:
            info_String += f'{item + ": ":-<13}' + str(round(info.get(item)[0], 0)) + "\n"

        self.label.config(text=name + "\n" + info_String)
        



MyGUI(50)