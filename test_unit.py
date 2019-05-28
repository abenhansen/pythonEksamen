from unittest import TestCase
from spilfunktioner import spiller_type
from spilfunktioner import betting
from spilfunktioner import *


class Testspilfunktioner(TestCase):

    #Være sikker på om der bliver retuneret en værdi
    def test_spiller_type(self):
        self.assertNotEqual(spiller_type(),[True,False])
        # self.assertIsInstance(spiller_type(), bool)

    # Test for at se om output er en int
    def test_betting(self):
         self.assertIsInstance(betting(), int)

    ##Være sikker på det bliver retuneret en boolean
    def test_playagain(self):
        self.assertIsInstance(playAgain(),bool)

    #Være sikker på at pc_bet og bet bliver reset til 0
    def test_vis_penge(self):
        self.assertEqual(vis_penge(),(0,0))

