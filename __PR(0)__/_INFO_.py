from bs4 import BeautifulSoup

# if html file is used
with open('filename.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify()) # html code bu in pretty

    tag = soup.find('h5') # finds the first one with this tag
    html_tags = soup.find_all('h5') # finds all with this tag, is saved as list
    for name_x in html_tags:
        print(name_x.text) # aoutputs the text betwean <h5> text <h5>

    course_card = soup.find_all('div', class_='card')
    for name_y in course_card:
        course_name = name_y.h5.text
        course_price = name_y.a.text.split()[-1] # Spaltet den string in eine liste und nimmt sich das letzte element

        print(f'{course_name} kostet {course_price}')
#________________________________________________________________________________________________________

from bs4 import BeautifulSoup
import requests

hatm_text = requests.get('URL_x').text
soup = BeautifulSoup(hatm_text, 'lxml')

#__________________________________________________________________________________________________________

import time

if __name__ == '__name__':
    while True:
        #programm_x() # das programm "programm_x" wird jede 10 minuten ausgeführt
        time.sleep(600) # alle 10 minuten

#__________________________________________________________________________________________________________

import requests
import json
from bs4 import BeautifulSoup

url = ''


#__________________________________________________________________________________________________________
import requests
import json

# API-URL für das Item
url = "https://api.warframe.market/v1/items/mirage_prime_blueprint/orders"

# Header mit User-Agent (manchmal nötig, um nicht geblockt zu werden)
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

# API-Anfrage senden
response = requests.get(url, headers=headers)

# JSON-Daten aus der Antwort extrahieren
data = response.json()

print(data)
# Alle Bestellungen aus den Daten holen
orders = data["payload"]["orders"]

# Relevante Daten extrahieren (Preis, Spielername, Plattform, Status)
for order in orders:
    if order["order_type"] == "sell" and order["user"]["status"] == "ingame":
        print(f"Spieler: {order['user']['ingame_name']} | Preis: {order['platinum']}")


import csv

# CSV-Datei erstellen
with open("warframe_prices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Spieler", "Preis"])

    for order in orders:
        if order["order_type"] == "sell" and order["user"]["status"] == "ingame":
            writer.writerow([order["user"]["ingame_name"], order["platinum"]])

print("Daten erfolgreich gespeichert!")

#________________________________________________________________________
"""
for frames in warframes:
        #print('__________________________________________________________________')
        #print(frames.find('div', class_='WarframeNavBoxIcon'))
        Prime_Icon = frames.find('div', class_='WarframeNavBoxIcon')
        # Prüft ob es keinen text endhält
        if not Prime_Icon.get_text(strip=True):
            Prime_Name = frames.find('span', style="color:white;")
            #print(Prime_Name.text) 
        else: 
            Prime_Name = frames.find('span', style="color:gold;")
            #print(Prime_Name.text + " Prime") 
            if Prime_Name and not Prime_Name.text == "excalibur" and not Prime_Name == "excalibur":
                primes_List["Warframes"].append(Prime_Name.text.lower() + " prime")


"""
#________________________________________________________________________
 # durchschnitt preis für (alle) produkte
 # grafen für die preise
 # benutzer oberfläche wo man nach produkt sucht und grafen mit durchschnitt preis bekommt


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry("800x500") # Demensionen

root.title("Warframe Tracker")
label = tk.Label(root, text="Gebe etwas ein", font=('Arial', 18)) 

label.pack(padx=20, pady=20) # setzt distanz zwischen rand und den label und fügt es zur root dazu

textbox = tk.Text(root, height=3, font=('Arial', 18)) # height = wie fiele zeilen angezeigt werden
textbox.pack() # Fügt das dextfelt hinzu
# myentry = tk.Entry(root) # hat nur eine zeile

button = tk.Button(root, text="klick", font=('Arial', 18) )
button.pack(padx=20, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky="news") # 0 zeile, 0 spalte, news= himmelrichtungen
btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky="news") # 0 zeile, 0 spalte, news= himmelrichtungen
btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky="news") # 0 zeile, 0 spalte, news= himmelrichtungen

buttonframe.pack(fill='x') # streckt in die x demension

anotherbutton = tk.Button(root, text="HOME")
anotherbutton.place(x=1, y=1, height=50, width=100) # Plazirung von oben links



root.mainloop()

##________________________________________________________________________
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.textbox = tk.Text(self.root, height=3, font=('Arial', 18))
        self.textbox.pack(padx=20, pady=20)
        
        # eine check box defoult=0, aktiv=1
        self.cheack_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="show massage", font=('Arial', 18), variable=self.cheack_state)
        self.check.pack(padx=20, pady=20)

        self.button2 = tk.Button(self.root, text="Show massage", font=('Arial', 18), command=self.show_message)
        self.button2.pack(padx=20, pady=20)

        self.root.mainloop()
    
    def show_message(self):
        text = self.textbox.get('1.0', tk.END) # Liest den Text von Zeile 1, Zeichen 0 bis zum Ende des Textfelds
        if(self.cheack_state.get()==0):
            print(text)
        else:
           messagebox.showinfo(title="Massage", message=text)
        

MyGUI()