import requests
import json
from bs4 import BeautifulSoup


class Scraping:

    def __init__(self, produkt):
        self.produkt = produkt.replace(' ', '_') # welcher warframe
 
    def getInfo(self, typ):
        url_x = 'https://api.warframe.market/v2/orders/item/'
        url = url_x + self.produkt + "_" + typ # typ = welches beuteil

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
            # set wird extra weggelassen
            )]
        
        warframe_map["gesammt minimum"] = int = [(
            warframe_map.get("blueprint")[1] + 
            warframe_map.get("chassis")[1] + 
            warframe_map.get("neuroptics")[1] + 
            warframe_map.get("systems")[1]
            # set wird extra weggelassen
            )]
        
        return warframe_map
    

# weapons scraping https://wiki.warframe.com/w/Prime
            
        
        
    

    



