import requests
import json
from bs4 import BeautifulSoup


class Scraping:

    def __init__(self, produkt):
        self.produkt = produkt.replace(' ', '_')


    def getDurchschnittsPreisItem(self, typ):
        url_x = 'https://api.warframe.market/v2/orders/item/'
        url = url_x + self.produkt + "_" + typ

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
        else:
            print(self.produkt)
            print("Fehler beim Abrufen:" , response.status_code)


        kumulierter_Preis = 0
        Anzahl_Verkäufer = 0

        for person in data['data']:
            if person['type'] == 'sell' and person['user']['status'] == 'ingame':
                kumulierter_Preis += person['platinum']
                Anzahl_Verkäufer += 1
                
        durchschnitts_Preis = round(kumulierter_Preis / Anzahl_Verkäufer,2)
        return durchschnitts_Preis
    
            
    def get_all_durchschitsspreis(self):
        komolirter_String = (
            "set: " + str(self.getDurchschnittsPreisItem("set")) + "\n" +
            "blueprint: " + str(self.getDurchschnittsPreisItem("blueprint")) + "\n" +
            "chassis: " + str(self.getDurchschnittsPreisItem("chassis_blueprint")) + "\n" +
            "neuroptics: " + str(self.getDurchschnittsPreisItem("neuroptics_blueprint")) + "\n" +
            "systems: " + str(self.getDurchschnittsPreisItem("systems_blueprint"))
        )
        
        return komolirter_String
    

    



