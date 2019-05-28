import kort as k
import spilfunktioner as sf
import spiller as h

deck = [] # Laver et array der skal indhole hele kort spillet
number_of_hands=0
k.lavDeck(deck)  #Her laver vi kortene, giver dem farver og numre
k.blandKort(deck)
sf.spiller_type()

while sf.spillethel:
    sf.vis_penge()
    spiller1 = h.Hånd()
    dealer = h.Hånd()
    k.tjek_hånd(deck)
    sf.regn_bets()
    k.første_runde_del(spiller1,dealer,deck)
    sf.vis_alle_hænder(spiller1,dealer)
    sf.spillets_gang(spiller1, dealer, deck)


