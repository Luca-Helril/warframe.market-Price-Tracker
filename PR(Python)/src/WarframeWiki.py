import requests
from bs4 import BeautifulSoup
import pickle
import os
from tkinter.ttk import *
import glob
import tkinter as tk
from tkinter import messagebox
from Scraping import Scraping

class WarframeWiki:
    def __init__(self):
        self.primes_List = {
            "Warframes": [],
        }

        # wenn liste nicht exestirt wird sie erstllt
        if not os.path.exists('Warframe_ownd_info.pkl'):
            owned_data = self.get_owned_list()
            with open('Warframe_ownd_info.pkl', 'wb') as f:
                pickle.dump(owned_data, f)
        
        # wenn die liste exestirt wird sie geladen und in variable gespeichert
        with open('Warframe_ownd_info.pkl', 'rb') as f:
            self.Warframe_ownd_info_list = pickle.load(f)




    def get_primes_list(self):
        if not os.path.exists('Warframe_Wiki_info.pkl') or False: # Wenn die Warframe liste nochmal erneuert werden soll False -> True
            self.get_images()
            url_Warframes = 'https://wiki.warframe.com/w/Warframes'
            response = requests.get(url_Warframes)
            html = response.text 
            soup = BeautifulSoup(html, 'lxml')

            # Gibt eine liste aller Warframes zurück
            warframes = soup.find_all('div', class_='WarframeNavBox')

            for frames in warframes:
                Prime_Name = frames.find('span', style="color:gold;")
                #print(Prime_Name.text + " Prime") 
                if Prime_Name and not Prime_Name.text.lower() == 'excalibur':
                    self.primes_List["Warframes"].append(Prime_Name.text.lower() + " prime")
            
            with open('Warframe_Wiki_info.pkl', 'wb') as f:
                pickle.dump(self.primes_List, f)
            
        with open('Warframe_Wiki_info.pkl', 'rb') as f:
            self.primes_List = pickle.load(f)
        
        return self.primes_List

    
    def get_images(self):
        output_dir = r"D:\__ SAVES __\__PR__\Pictures"
        os.makedirs(output_dir, exist_ok=True)

        base_url = "https://wiki.warframe.com"
        url = "https://wiki.warframe.com/w/Warframes"

        htmldata = requests.get(url)
        soup = BeautifulSoup(htmldata.text, 'html.parser')

        # Daten in orner löschen
        files = glob.glob(os.path.join(output_dir, "*"))
        for f in files:
            os.remove(f)

        x = 0
        for item in soup.find_all('img'):
            if x > 700: # es werden x durchläufe gemacht
                break
            x += 1
            
            src = item.get("src")
            if not src or "Prime" in src:
                continue

            image_url = base_url + src


            # Dateinamen extrahieren
            filename = src.split("/")[-1].split("?")[0]
            filename = filename[5:-11].lower() + ".png"

            # Vollständiger Pfad zum Speichern
            filepath = os.path.join(output_dir, filename)
            
            #print(filepath)

            image_data = requests.get(image_url).content
            with open(filepath, 'wb') as f:
                f.write(image_data)
            #print(f"Gespeichert: {filename}")
    
    # gibt eine liste zurück die ändweder schon exestirt oder die neu gemacht wird
    # ["kategori"]: ["name1", "name2" ...]: ["set", "blueprint", "chassis"...]: [boolean]
    def get_owned_list(self):
        # wenn die datei bereit exestirt wird zie zurück gegeben
        if os.path.exists('Warframe_ownd_info.pkl'):
            with open('Warframe_ownd_info.pkl', 'rb') as f:
                return pickle.load(f)
        else:
            prime_list_temp = self.get_primes_list()
            bauteile = {
                "set" : False,
                "blueprint" : False,
                "chassis" : False,
                "neuroptics" : False,
                "system" : False
            }

            owned_list = {"Warframes": {}}

            for kategori in prime_list_temp:
                for name in prime_list_temp[kategori]:
                    owned_list[kategori][name] = bauteile.copy()
            #print(owned_list)
            return owned_list

    # aktualisirt die boolean werte der bauteile für die warframes, also ob sie in besitz sind oder nicht
    def set_owed(self, kategori, warframe_name, bauteil, zustand): # alles sind strings, zustand= boolean
        self.Warframe_ownd_info_list[kategori][warframe_name][bauteil] = zustand
        with open('Warframe_ownd_info.pkl', 'wb') as f:
            pickle.dump(self.Warframe_ownd_info_list, f)
        



#wf = WarframeWiki()
#wf.set_owed("Warframes", "ash prime", "set", True)
#print(wf.Warframe_ownd_info_list["Warframes"]["ash prime"])
#besitzt_set = wf.Warframe_ownd_info_list["Warframes"]["ash prime"]["set"]
#print(besitzt_set)  # True oder False
    
            



        
    





