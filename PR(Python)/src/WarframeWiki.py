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
                    primes_List["Warframes"].append(Prime_Name.text.lower() + " prime")
            
            with open('Warframe_Wiki_info.pkl', 'wb') as f:
                pickle.dump(primes_List, f)
            
        with open('Warframe_Wiki_info.pkl', 'rb') as f:
            primes_List = pickle.load(f)
        
        return primes_List

    
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
            if x > 10: # es werden x durchläufe gemacht
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
            
            print(filepath)

            image_data = requests.get(image_url).content
            with open(filepath, 'wb') as f:
                f.write(image_data)
            print(f"Gespeichert: {filename}")



    
            



        
    





