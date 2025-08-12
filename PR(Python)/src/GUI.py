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


        # anstat die informationen in ein label auszugeben, in einer liste ausgeben ______________________________________
        if 1== 2:
            for i in range(7):
                for j in range(3):
                    self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold'))

                    self.e.grid(row=i+4, column=j+2)
                    self.e.insert(END, "test")

        
        #Label wo wenn der knopf eines warframes gedrückt wird die warframe.market informationen über ihn angezeigt werden
        self.label = tk.Label(self.root, text="\n\n\n\n\n\n\n\n", font=('Arial', 15), anchor="w", justify=tk.LEFT)
        self.label.grid(sticky = N, row= 2, column= 2)

        textbox = tk.Text(self.root, height=1, font=('Arial', 18)) # height = wie fiele zeilen angezeigt werden
        textbox.grid(row= 3, column= 2) # Fügt das dextfelt hinzu
        # myentry = tk.Entry(root) # hat nur eine zeile

        # sorgt dafür, dass die Hauptspalten im gesamten Fenster flexibel sind.
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.rowconfigure(4, weight=1)

        # sorgt dafür, dass im Inneren des Buttonbereichs die Buttons auch gleichmäßig Platz kriegen
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
        # liest liste mit allem warframes aus z.b.["warframe": [name1, name2, name3]]
        for kategori in primes_List:
                for name in primes_List[kategori]:
                        if (thisCount <= buttons): # ist nicht wirklich benötogt nur zm einschränken damit tästen nicht so lange dauer ___________________________
                            picture_name = name.lower().replace(" prime", "") + ".png"
                            picture_path = r"D:\__ SAVES __\__PR__\Pictures" + "\\" + picture_name
                            if os.path.exists(picture_path): #wenn bild für den warframe exestirt
                                image = Image.open(picture_path)
                                image = image.resize((image.width // 1, image.height // 1))
                                photoimage = ImageTk.PhotoImage(image)
                                self.images.append(photoimage) #damit die bilder gespeichert werden und nicht automatisch gelöscht werden
                
                                btn = tk.Button(buttonframe, text=name, image = photoimage, compound = LEFT, font=('Arial', 14), anchor="w", padx=10, command=lambda n=name: self.show_info(n)) # Without this, name would refer to the same variable across all buttons — so they'd all print the last name. Using lambda n=name: captures the current value of name.
                                
                                zeile = thisCount // 5
                                spalte = thisCount % 5
                                
                                btn.grid(row=zeile, column=spalte, sticky="nsew", padx=2, pady=2)
                                buttonframe.rowconfigure(zeile, weight=1)
                                thisCount += 1
                            else:
                                print(picture_path)
        anotherbutton = tk.Button(self.root, text="HOME", command = self.open_new_window) #wenn der button gedrücht wird wechelt mann in das fenster von GUI2.py
        anotherbutton.place(x=1, y=1, height=50, width=100) # Plazirung von oben links

        self.root.mainloop()  # GUI-Schleife starten, damit wenn man button drückt auch etwas passirt


    #Gibt die informationen zu den warframe dessen Button man angeklickt hat in Lable aus
    def show_info(self, name):
        scrab = Scraping(name)
        info = scrab.get_all_info()
        info_String =""
        for item in info:
            info_String += f'{item + ": ":.<15}' + str(round(info.get(item)[0], 0)) + "\n"
        self.label.config(text=name + "\n" + info_String)

    #Öffnet ein neues fenster von der classe GUI2.py    
    def open_new_window(self):
        MyGUI2(self.root)



MyGUI(50) #führt die classe aus