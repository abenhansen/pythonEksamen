import random
numre = ('to','tre','fire','fem','seks','syv','otte','ni','ti','bonde','dronning','konge','es')
farver =('hjerter','ruder','kløver','spade')
number_of_hands = 0
class Kort:

    def __init__(self,farve,nummer):
        self.farve = farve
        self.nummer = nummer



    def __str__(self):
        return self.farve + ": " + self.nummer



def lavDeck(deck):
    for farve in farver:
        for nummer in numre:
            deck.append(Kort(farve, nummer))


def blandKort(deck):
    random.shuffle(deck)
def delkort(deck):
        enkelt_kort = deck.pop()
        return enkelt_kort

def tjek_hånd(deck):
    global number_of_hands
    if number_of_hands==4:
        deck.clear()
        lavDeck(deck)
        blandKort(deck) #Her blander vi kortene
        number_of_hands = 0
        print("Nu blander vi kort")
    # print(number_of_hands)
    # print(len(deck))
    number_of_hands += 1

def trækkort(hånd,deck):
    hånd.tilføj_kort(delkort(deck))
    hånd.tjekes()

def første_runde_del(spiller1,dealer,deck):
    trækkort(spiller1,deck)
    trækkort(dealer,deck)
    trækkort(spiller1,deck)
    trækkort(dealer,deck)

