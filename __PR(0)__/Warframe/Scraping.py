import requests
import json
from bs4 import BeautifulSoup


class Scraping:

    def __init__(self, produkt):
        self.produkt = produkt.replace(' ', '_')


    def getDurchschnittsPreisItem(self, typ):
        url_x = 'https://api.warframe.market/v2/orders/item/'
        url = url_x + self.produkt + "_" + typ

        print(url)

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
    
    def getInfo(self, typ):
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
        anzahl_Verkäufer = 0
        minimal_Preis = 0

        for person in data['data']:
            if person['type'] == 'sell' and person['user']['status'] == 'ingame':
                kumulierter_Preis += person['platinum']
                anzahl_Verkäufer += 1
                if (minimal_Preis == 0 or minimal_Preis > person['platinum']):
                    minimal_Preis = person['platinum']
       
        durchschnitts_Preis = round(kumulierter_Preis / anzahl_Verkäufer,2)

        info = [durchschnitts_Preis, minimal_Preis, anzahl_Verkäufer] # virleicht zu dictonary machen mit was es ist : wert
        return info


    def get_all_info(self):
        warframe_map = {}
        warframe_map["set"] = self.getInfo("set")
        warframe_map["blueprint"] = self.getInfo("blueprint")
        warframe_map["chassis"] = self.getInfo("chassis_blueprint")
        warframe_map["neuroptics"] = self.getInfo("neuroptics_blueprint")
        warframe_map["systems"] = self.getInfo("systems_blueprint")
        
        warframe_map["gesammt Durchschnitt"] = int = [(
            warframe_map.get("blueprint")[0] + 
            warframe_map.get("chassis")[0] + 
            warframe_map.get("neuroptics")[0] + 
            warframe_map.get("systems")[0]
            )]
        
        warframe_map["gesammt minimum"] = int = [(
            warframe_map.get("blueprint")[1] + 
            warframe_map.get("chassis")[1] + 
            warframe_map.get("neuroptics")[1] + 
            warframe_map.get("systems")[1]
            )]
        
        return warframe_map

    # später überprüfen ob benötigt wird
    def get_all_info_toString(self):
        info_Streing = ""
        for item in self.get_all_info():
            print(item + ": ")
            info_Streing = (item + ": " )
        return info_Streing




            
    def get_all_durchschitsspreis(self):
        komolirter_String = (
            "set: " + str(self.getDurchschnittsPreisItem("set")) + "\n" +
            "blueprint: " + str(self.getDurchschnittsPreisItem("blueprint")) + "\n" +
            "chassis: " + str(self.getDurchschnittsPreisItem("chassis_blueprint")) + "\n" +
            "neuroptics: " + str(self.getDurchschnittsPreisItem("neuroptics_blueprint")) + "\n" +
            "systems: " + str(self.getDurchschnittsPreisItem("systems_blueprint"))
        )
        
        return komolirter_String
    

    



