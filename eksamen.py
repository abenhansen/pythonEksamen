from kort import Kort
from spiller import Hånd
import kort as k

deck = [] # Laver et array der skal indhole hele kort spillet
k.lavDeck(deck)  #Her laver vi kortene, giver dem farver og numre
k.blandKort(deck)
penge=100
pc_penge = 100
number_of_hands=0
helespillet = True

def betting():
    while True:
        try:
            svar = int(input("Hvor meget vil du bette? Tast 0 hvis du bare vil spille for sjov"))
            if svar > penge:
                print("Du har ikke nok penge! Du kar kun {0}".format(penge))
                continue
        except ValueError:
            print("Ikke et tal! Prøv igen!.")
            continue
        else:
            return svar
            # break

def playAgain():
    global helespillet
    if pc_penge == 0:
        print("Computer har ikke flere penge og har tabt spillet!")
        helespillet = False
    else:
        while True:
            svar = input("Vil du spille igen? Tryk j eller n")
            if svar == "j":
                break
            elif svar == "n":
                helespillet = False
                break
            else:
                print("Du skal indtaste 'j' eller 'n'!")
                continue

def trækkort(hånd):
    hånd.tilføj_kort(k.delkort(deck))
    hånd.tjekes()

while True:
    spiller_svar = input("Vil du være gambler eller dealer? Tryk g eller d" )
    if spiller_svar=="g":
        spiller_dealer = False
        print("Du har valgt at være spiller!")
        break
    elif spiller_svar=="d":
        spiller_dealer = True
        print("Du har valgt at være dealer!")
        break
    else:
        print ("Prøv Igen")
        continue

while helespillet:

    # print(len(deck))
    if(spiller_dealer==False):
        print("Du har så mange penge: {0}".format(penge))
    else:
        print("Computer har så mange penge: {0}".format(pc_penge))
    bet = 0
    pc_bet = 0
    spiller1 = Hånd()
    dealer = Hånd()
    def vis_hånd_spiller():
        print("Spillers hånd")
        # print("Korthånds værdi: {0}".format(spiller1.værdi))
        for kort in spiller1.korthånd:
            print(kort)

    def vis_hånd_computer():
        print("Computer hånd")
        # print("Korthånds værdi: {0}".format(dealer.værdi))
        for kort in dealer.korthånd:
            print(kort)


    if number_of_hands==4:
        deck.clear()
        k.lavDeck(deck)
        k.blandKort(deck) #Her blander vi kortene
        number_of_hands = 0
        print("Nu blander vi kort")
    # print(number_of_hands)
    # print(len(deck))
    number_of_hands += 1
    if (spiller_dealer == False):
        bet = betting()
        penge = penge - bet
        print(bet)
    else:
        # if (pc_penge > 0):
        #     pc_bet = int(pc_penge / 2)
        #     pc_penge = pc_penge-pc_bet
        #     print("Computer har bettet: {0} og har {1} tilbage".format(pc_bet, pc_penge))
        pc_bet = int(pc_penge / 2)
        pc_penge = pc_penge - pc_bet
        print("Computer har bettet: {0} og har {1} tilbage".format(pc_bet, pc_penge))

    trækkort(spiller1)
    trækkort(dealer)
    trækkort(spiller1)
    trækkort(dealer)

    # spiller1.tilføj_kort(k.delkort(deck))
    # dealer.tilføj_kort(k.delkort(deck))
    # spiller1.tilføj_kort(k.delkort(deck))
    # dealer.tilføj_kort(k.delkort(deck))
    if (spiller_dealer == False):
        vis_hånd_spiller()
        vis_hånd_computer()
    else:
        vis_hånd_computer()
        vis_hånd_spiller()
    spiligang = True


    def træk_eller_stå():
        while True:
            global spiligang
            global penge
            # if (spiller_dealer == False):
            print("Spiller har: {0} point og Computer har: {1} point".format(spiller1.værdi,dealer.værdi))

            svar =input("Vil du trække et kort eller stå? Tryk 't' eller 's")
            if svar=="t":
                    # spiller1.tilføj_kort(k.delkort(deck))
                trækkort(spiller1)
                vis_hånd_spiller()
            elif svar=="s":
                print("Du har valgt at stå")
                if spiller_dealer == False:
                    while dealer.værdi<16:
                        # dealer.tilføj_kort(k.delkort(deck))
                        trækkort(dealer)
                        vis_hånd_computer()
                spiligang = False
                tjekvinder()

            else:
                print("Du skal indtaste 't' eller 's'!")
                continue
            break

    def spiller_er_dealer():
        global spiligang
        while dealer.værdi < 16:
            trækkort(dealer)
            vis_hånd_computer()
        if dealer.værdi > 21:
            print("Computer har trukket over 21!")
            print("Spiller har vundet!")
            playAgain()
            spiligang = False
        else:
            træk_eller_stå()
        # spiligang = False


    def tjekvinder():
        global penge
        global pc_penge
        global pc_bet
        global bet
        print("Spiller har så mange point : {0}".format(spiller1.værdi))
        print("Computer har så mange point : {0}".format(dealer.værdi))
        if dealer.værdi > 21:
            print("Computer har trukket over 21!")
            print("Spiller har vundet!")
            penge = penge + (bet * 2)
            playAgain()
        elif spiller1.værdi > dealer.værdi:
            print("Spiller har vundet!")
            penge = penge + (bet * 2)
            playAgain()
        elif dealer.værdi > spiller1.værdi:
            print("Computer har vundet!")
            pc_penge = pc_penge+(pc_bet*2)
            playAgain()
        elif dealer.værdi == spiller1.værdi:
            print("Push! Det blev uafgjort!")
            penge = penge + bet
            pc_penge = pc_penge+pc_bet
            playAgain()


    while spiligang:
        # vis_hånd_spiller()
        if spiller_dealer == False:
            træk_eller_stå()
        if spiller_dealer:
            spiller_er_dealer()
        if spiller1.værdi>21:
            print("Spiller har trukket over 21!")
            print("Computer har vundet!")
            pc_penge = pc_penge+(pc_bet*2)
            playAgain()
            break









