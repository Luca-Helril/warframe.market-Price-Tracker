import requests
from bs4 import BeautifulSoup
import pickle
import os

class WarframeWiki:
    # Saves all primes
    primes_List = {
        "Warframes": [],
        "Weapons": [],
        #"Primary Weapons": [],
        #"Secondary Weapons": [],
        #"Melee Weapons": [],
        #"Companions": [],
        #"": [],
        #"": [],
    }


    # _______________________________ WARFRAMES _________________________________________

    if not os.path.exists('Warframe_Wiki_info.pkl') or False: # Wenn die Warframe liste nochmal erneuert werden soll False -> True
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

    #print(loaded_dict)

    # _______________________________ Weapons _________________________________________
    """
    url_Weapons = 'https://wiki.warframe.com/w/Weapons#Primary'
    response_Weapons = requests.get(url_Weapons)
    html_Weapons = response_Weapons.text 
    soup_Weapons = BeautifulSoup(html_Weapons, 'lxml')

    # Gibt eine liste aller Waffen zurück
    Weapons = soup_Weapons.find_all('span', {'data-param2': 'Weapons'})

    for weapons in Weapons:
        weapons_name = weapons.get('data-param')
        if weapons_name:
            if weapons_name.find("Prime")>0:
                primes_List["Weapons"].append(weapons_name.lower())
    """
    #print(primes_List)
            



        
    





