import kort as k
import spilfunktioner as sf
import spiller as h

deck = [] # Laver et array der skal indhole hele kort spillet
k.lavDeck(deck)  #Her laver vi kortene, giver dem farver og numre
k.blandKort(deck) #Blander kort
sf.spiller_type() #Spørger spiller om han vil være spiller eller dealer

#loop for at være sikker på hele spillet kører
while sf.spillethel:
    sf.vis_penge() #Først viser den hvor mange penge spiller eller computer har og resseter bets til 0
    spiller1 = h.Hånd() #Laver spillers hånd objekt
    dealer = h.Hånd()#Laver computers hånd objekt
    k.tjek_hånd(deck)#Tjekker hvor mange gange spillet har kørt og putter alle kortene tilbage i listen og blannder efter 4 spil
    sf.regn_bets() #Regner alle bets ud og viser dem til bruger
    k.første_runde_del(spiller1,dealer,deck)#Deler 2 kort ud til computer og bruger
    sf.vis_alle_hænder(spiller1,dealer) #printer spiller og computers hånd
    sf.spillets_gang(spiller1, dealer, deck) #Spillet selv der sørger for at spillet er igang


