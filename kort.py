import random
#2 tuples der hver indeholder numre og farver på kortet
numre = ('to','tre','fire','fem','seks','syv','otte','ni','ti','bonde','dronning','konge','es')
farver =('hjerter','ruder','kløver','spade')
#Værdi til at styre hvor mange gange spillet har været i gang
number_of_hands = 0
#Klasse til at give alle kortene numre og farver
class Kort:

    def __init__(self,farve,nummer):
        self.farve = farve
        self.nummer = nummer



    def __str__(self):
        return self.farve + ": " + self.nummer


#funktion  der så så putter alle de 52 kort i et deck Array
def lavDeck(deck):
    for farve in farver:
        for nummer in numre:
            deck.append(Kort(farve, nummer))

#Blander alle kortene i deck arrayet
def blandKort(deck):
    random.shuffle(deck)

#når et kort bliver delt ud fra decket bliver det slettet i deck arrayet og giver videre til korthånd
def delkort(deck):
        enkelt_kort = deck.pop()
        return enkelt_kort

#Tjekker hvor mange gange spillet har kørt og putter alle kortene tilbage i listen og blannder efter 4 spil
def tjek_hånd(deck):
    global number_of_hands
    if number_of_hands==4:
        deck.clear() #Her ryder vi hele decket
        lavDeck(deck) #Her putter vi alle kortene tilbage i arrayet
        blandKort(deck) #Her blander vi kortene
        number_of_hands = 0
        print("Nu blander vi kort")
    number_of_hands += 1

#Metode til at tilføje kort fra deck til korthånd og tjekker om man har et es
def trækkort(hånd,deck):
    hånd.tilføj_kort(delkort(deck))
    hånd.tjekes()

#Her bliver de første 4 kort delt ud
def første_runde_del(spiller1,dealer,deck):
    trækkort(spiller1,deck)
    trækkort(dealer,deck)
    trækkort(spiller1,deck)
    trækkort(dealer,deck)

