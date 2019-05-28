import spiller as sp
import kort as k
global spiller_dealer
penge=100
pc_penge = 100
# global spiller1
# global dealer
global spillethel
global spiligang
spillethel = True


def vis_penge():
    global pc
    global bet
    global pc_bet
    # print(len(deck))
    if spiller_dealer==False:
        print("Du har så mange penge: {0}".format(penge))
    else:
        print("Computer har så mange penge: {0}".format(pc_penge))
    bet = 0
    pc_bet = 0
    return bet,pc_bet
    # spiller1 = sp.Hånd()
    # dealer = sp.Hånd()

def vis_hånd_spiller(spiller1):
    print("Spillers hånd")
    for kort in spiller1.korthånd:
        print(kort)

def vis_hånd_dealer(dealer):
    print("Computer hånd")
    if spiller_dealer==False:
        for kort in dealer.korthånd[1:]:
            print("Første kort skjult")
            print(kort)
    else:
        for kort in dealer.korthånd:
            print(kort)

def vis_alle_hænder(spiller1,dealer):
    global spiligang
    if (spiller_dealer == False):
        vis_hånd_spiller(spiller1)
        vis_hånd_dealer(dealer)
    else:
        vis_hånd_dealer(dealer)
        vis_hånd_spiller(spiller1)
    spiligang=True



def spiller_type():
    global spiller_dealer
    while True:
        spiller_svar = input("Vil du være gambler eller dealer? Tryk g eller d" )
        if spiller_svar=="g":
            spiller_dealer = False
            print("Du har valgt at være spiller!")
            return spiller_dealer
            # break
        elif spiller_svar=="d":
            spiller_dealer = True
            print("Du har valgt at være dealer!")
            return spiller_dealer
        else:
            print ("Prøv Igen")
            continue

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

def regn_bets():
    global penge
    global pc_penge
    global bet
    global pc_bet
    if (spiller_dealer == False):
        bet = betting()
        penge = penge - bet
        return print(bet)
    else:
        pc_bet = int(pc_penge / 2)
        pc_penge = pc_penge - pc_bet
        return print("Computer har bettet: {0} og har {1} tilbage".format(pc_bet, pc_penge))

def træk_eller_stå(spiller1,dealer,deck):
    while True:
        global spiligang
        global penge
        # if (spiller_dealer == False):
        if spiller_dealer:
            print("Spiller har: {0} point og Computer har: {1} point".format(spiller1.værdi,dealer.værdi))
        else:
            print("Spiller har: {0} point og Computer har: {1} point".format(spiller1.værdi,dealer.skjultVærdi))

        svar =input("Vil du trække et kort eller stå? Tryk 't' eller 's")
        if svar=="t":
                # spiller1.tilføj_kort(k.delkort(deck))
            k.trækkort(spiller1,deck)
            vis_hånd_spiller(spiller1)
        elif svar=="s":
            print("Du har valgt at stå")
            if spiller_dealer == False:
                while dealer.værdi<16:
                    # dealer.tilføj_kort(k.delkort(deck))
                    k.trækkort(dealer,deck)
                    vis_hånd_dealer(dealer)
            spiligang = False
            return tjekvinder(spiller1,dealer)

        else:
            print("Du skal indtaste 't' eller 's'!")
            continue
        break

def tjekvinder(spiller1,dealer):
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
        return playAgain()
    elif spiller1.værdi > dealer.værdi:
        print("Spiller har vundet!")
        penge = penge + (bet * 2)
        return playAgain()
    elif dealer.værdi > spiller1.værdi:
        print("Computer har vundet!")
        pc_penge = pc_penge+(pc_bet*2)
        return playAgain()
    elif dealer.værdi == spiller1.værdi:
        print("Push! Det blev uafgjort!")
        penge = penge + bet
        pc_penge = pc_penge+pc_bet
        return playAgain()


def playAgain():
    global spillethel
    if pc_penge == 0:
        print("Computer har ikke flere penge og har tabt spillet!")
        # helespillet = False
        spillethel = False
    else:
        while True:
            svar = input("Vil du spille igen? Tryk j eller n")
            if svar == "j":
                return True
            elif svar == "n":
                # helespillet = False
                spillethel = False
                return spillethel
            else:
                print("Du skal indtaste 'j' eller 'n'!")
                continue

def spiller_er_dealer(spiller1,dealer,deck):
    global spiligang
    while dealer.værdi < 16:
        k.trækkort(dealer,deck)
        vis_hånd_dealer(dealer)
    if dealer.værdi > 21:
        print("Computer har trukket over 21!")
        print("Spiller har vundet!")
        playAgain()
        spiligang = False
        return spiligang
    else:
        træk_eller_stå(spiller1,dealer,deck)

def spillets_gang(spiller1,dealer,deck):
    global pc_penge
    while spiligang:
        # vis_hånd_spiller()
        if spiller_dealer == False:
            træk_eller_stå(spiller1,dealer,deck)
        if spiller_dealer:
            spiller_er_dealer(spiller1,dealer,deck)
        if spiller1.værdi>21:
            print("Spiller har trukket over 21!")
            print("Computer har vundet!")
            pc_penge = pc_penge+(pc_bet*2)
            return playAgain()
