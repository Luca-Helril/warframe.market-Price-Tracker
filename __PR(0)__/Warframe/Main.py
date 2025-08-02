from Scraping import Scraping
from WarframeWiki import WarframeWiki

 # durchschnitt preis für (alle) produkte
 # grafen für die preise
 # benutzer oberfläche wo man nach produkt sucht und grafen mit durchschnitt preis bekommt
 # man kann eingeben welche bauteile man bereits besitzt


 # waffen namen nehmen in Sraper packen und wenn keine error masage kommt fortfahren
 # am besten schon dirket bei der erstellung der liste durchfüren

def print_Warframes1(count = -1):
    thisCount = 0
    for kategori in WarframeWiki.primes_List:
            print("_____________________________________________")
            print(kategori)
            
            for name in WarframeWiki.primes_List[kategori]:
                    if (thisCount <= count):
                        print(name)
                        scrab = Scraping(name + ' set')
                        print("set: " + str(scrab.getDurchschnittsPreis()))

                        scrab = Scraping(name + ' blueprint')
                        print("blueprint: " + str(scrab.getDurchschnittsPreis()))

                        scrab = Scraping(name + ' chassis blueprint')
                        print("chassis: " + str(scrab.getDurchschnittsPreis()))

                        scrab = Scraping(name + ' neuroptics blueprint')
                        print("neuroptics: " + str(scrab.getDurchschnittsPreis()))

                        scrab = Scraping(name + ' systems blueprint')
                        print("systems: " + str(scrab.getDurchschnittsPreis()))
                        
                        print("_________________________________________________________________")
                        if count != -1:
                            thisCount += 1   

#print_Warframes1()  

def print_Warframes2():
    scrab = Scraping("grendel prime")
    test = scrab.get_all_info()
    #print(test)
    info_String =""
    for item in test:
        info_String += f'{item + ": ":-<22}' + str(round(test.get(item)[0], 0)) + "\n"

    print(info_String)

print_Warframes2()
