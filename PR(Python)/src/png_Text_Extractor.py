import easyocr
from Scraping import Scraping
from WarframeWiki import WarframeWiki
import sys

# import pytesseract from PIL import Image     # alternative falls es zeitprobleme mit easyocr gibt

sys.stdout.reconfigure(encoding="utf-8")

reader = easyocr.Reader(['en'], gpu=True) # this needs to run only once to load the model into memory
result = reader.readtext('ScreenShot.png')
words = []

for (bbox, text, prob) in result:
    #print(f'Text: {text}, Probability: {prob}')
    if "Prime" in text: # nur die Texte wo Prime drinn ist
        print(f'Text: {text}')
        split_words = text.split()
        split_words.append(None)
        words.append(split_words) # Z.b. ['Acceltra', 'Prime', 'Blueprint', None]

print(words)

# methode aufrufe die prüft ob die elemente in array bereits in besitz sind
warframeWiki = WarframeWiki()
primes_List = warframeWiki.get_primes_list()
owed_list = warframeWiki.get_owned_list()

# optemirung weil n^3 
result = []
for kategori in primes_List: # katogorien (z.b. Warframes, waffen, ...)
            for name in primes_List[kategori]: # name der gegensdände (z.b. Garuda, Volt, ...)
                for item in words: # schauen ob der name des objects mit den namen der von screemshot kommt übereinstimmt
                    if(name.lower() == item[0].lower()):
                        item[3] = owed_list[kategori][item[1]][item[2]] # boolean in item[3] reinschreiben ob das item in besitz ist


print(words)
                         

            


    