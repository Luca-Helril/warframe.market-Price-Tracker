import easyocr

import sys
sys.stdout.reconfigure(encoding="utf-8")

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('ScreenShot.png')
primes = []

for (bbox, text, prob) in result:
    #print(f'Text: {text}, Probability: {prob}')
    if "Prime" in text:
        print(f'Text: {text}')
        primes.append(text)

print(primes)

# methode aufrufe die prüft ob die elemente in array bereits in besitz sind


    