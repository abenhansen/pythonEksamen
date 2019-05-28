import kort as k
global spiller_dealer
penge=100
pc_penge = 100
##Boolean til at styre om hele spillet skal lukkes
global spillethel
##Boolean for at styre træk eller stå Funktionen, og hvornår man skal gå ud af den funktion
global spiligang
spillethel = True


# Viser hvor mange penge
def vis_penge():
    ## Variabel for spiller bet
    global bet
    #Variabel for computers bet
    global pc_bet
    ##Tjekker om spiller er dealer hvis spiller ikke er dealer skal computer nemlig vise penge i stedet
    if spiller_dealer==False:
        print("Du har så mange penge: {0}".format(penge))
    else:
        print("Computer har så mange penge: {0}".format(pc_penge))
    ## Restter bets til 0
    bet = 0
    pc_bet = 0
    return bet,pc_bet


##Funktion til at vise hånd for bruger
def vis_hånd_spiller(spiller1):
    print("Spillers hånd")
    for kort in spiller1.korthånd:
        print(kort)

##Funktion til at vise computers hånd
def vis_hånd_computer(dealer):
    print("Computer hånd")
    ##Her printer den ikke det først kort ud hvis computer er dealer
    if spiller_dealer==False:
        for kort in dealer.korthånd[1:]:
            print("Første kort skjult")
            print(kort)
    else:
        for kort in dealer.korthånd:
            print(kort)

#Funktion der så printer både computer og brugers hånd ud
def vis_alle_hænder(spiller1,dealer):
    global spiligang
    if (spiller_dealer == False):
        vis_hånd_spiller(spiller1)
        vis_hånd_computer(dealer)
    else:
        vis_hånd_computer(dealer)
        vis_hånd_spiller(spiller1)
    spiligang=True


#Funktion hvor bruger for lov til at vælge om han vil være spiller eller dealer
def spiller_type():
    ##boolean der styrer spillers rolle
    global spiller_dealer
    ##Loop der kører indtil spiller har indtastet g eller d og bliver ved hvis man ikke taster ind af de to ting
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

##Funktion der styrer bets, og spørger bruger om hvor meget han vil bette, og man skal angive et tal eller blivver man spurgt igen
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

#Funktion der regner alle bets ud og printer ud hvor meget bruger eller pc har bettet
def regn_bets():
    global penge
    global pc_penge
    global bet
    global pc_bet
    ##Hvis spiller er bruger regner den bet ud for spiller ellers regner den ud for computer
    if (spiller_dealer == False):
        bet = betting()
        penge = penge - bet
        return print(bet)
    else:
        pc_bet = int(pc_penge / 2)
        pc_penge = pc_penge - pc_bet
        return print("Computer har bettet: {0} og har {1} tilbage".format(pc_bet, pc_penge))

#Funktion der bliver ved med at køre til der er fundet en vinder af spillet
def træk_eller_stå(spiller1,dealer,deck):
    global spiligang
    global penge
    ##Loop der bliver styret af spiligang, loopet stopper enten når spiller indtaster s eller der er fundet en vinder
    while True:
        #Her printer den kun det første kort ud for computer hvis spiller er dealer ellers printer den ikke det første kort
        if spiller_dealer:
            print("Spiller har: {0} point og Computer har: {1} point".format(spiller1.værdi,dealer.værdi))
        else:
            print("Spiller har: {0} point og Computer har: {1} point".format(spiller1.værdi,dealer.skjultVærdi))
        #Her i loopet bliver spiller spurgt om han vil trække et nyt kort eller beholde sin hånd ved at indtaste s
        svar =input("Vil du trække et kort eller stå? Tryk 't' eller 's")
        if svar=="t":
                # spiller1.tilføj_kort(k.delkort(deck))
            k.trækkort(spiller1,deck)
            vis_hånd_spiller(spiller1)
        elif svar=="s":
            print("Du har valgt at stå")
            #Hvis spiller ikke er dealer får computer først lov til at trække kort når spiller har trukket alle sine, og stopper
            #Når computer når en korthånds værdi af 16
            if spiller_dealer == False:
                while dealer.værdi<16:
                    # dealer.tilføj_kort(k.delkort(deck))
                    k.trækkort(dealer,deck)
                    vis_hånd_computer(dealer)
            spiligang = False
            return tjekvinder(spiller1,dealer)
        #her stopper loopet ikke hvis man ikke indtaster t eller s
        else:
            print("Du skal indtaste 't' eller 's'!")
            continue
        break
##Funktion der tjekker hvem der har vundet
def tjekvinder(spiller1,dealer):
    global penge
    global pc_penge
    global pc_bet
    global bet
    #Printer det endelig resultat af spiller og computer ud
    print("Spiller har så mange point : {0}".format(spiller1.værdi))
    print("Computer har så mange point : {0}".format(dealer.værdi))
    #Tjeker om dealers værdi er højere end 21 hvis det er vinder spiller
    if dealer.værdi > 21:
        print("Computer har trukket over 21!")
        print("Spiller har vundet!")
        #Hvis spiller vinder får spillet sit bet i penge
        penge = penge + (bet * 2)
        return playAgain()
    #Tjekker om spiller har højest værdi
    elif spiller1.værdi > dealer.værdi:
        print("Spiller har vundet!")
        penge = penge + (bet * 2)
        return playAgain()
    #Tjekker om dealer har højest værdi i sin hånd
    elif dealer.værdi > spiller1.værdi:
        print("Computer har vundet!")
        #Hvis computer vinder skal han have sin
        pc_penge = pc_penge+(pc_bet*2)
        return playAgain()
    #Tjekker om bruger og computers hånd har samme værdi, hvis de har får de deres bet tilbage i penge
    elif dealer.værdi == spiller1.værdi:
        print("Push! Det blev uafgjort!")
        penge = penge + bet
        pc_penge = pc_penge+pc_bet
        return playAgain()


#Spørger spiller om han vil spille igen
def playAgain():
    global spillethel
    #if statement til at tjekke om computer har flere penge, hvis computer ikke har nogen penge slutter spillet og bruger vinder
    if pc_penge == 0:
        print("Computer har ikke flere penge og har tabt spillet!")
        # helespillet = False
        spillethel = False
    else:
        #Loop der bliver ved med at spørge bruger om han vil spille igen og bliver ved med at køre indtil svar j eller n er giver
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

#Kører spillet på en anden måde hvis spiller er dealer, her spiller computer sin hånd før spiller
def spiller_er_dealer(spiller1,dealer,deck):
    global spiligang
    while dealer.værdi < 16:
        k.trækkort(dealer,deck)
        vis_hånd_computer(dealer)
    ##Hvis dealers værdi ryger over 21 taber han med det samme
    if dealer.værdi > 21:
        print("Computer har trukket over 21!")
        print("Spiller har vundet!")
        playAgain()
        spiligang = False
        return spiligang
    else:
        træk_eller_stå(spiller1,dealer,deck)

#Vælger hvilken funktion der skal spilles i forhold til om bruger er spiller eller dealer
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
