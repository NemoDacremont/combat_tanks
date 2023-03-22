#!/bin/env python3

import os
from couleurs_ansi import *
import time

from tank import Tank
from balle import Balle


DELAI = 1

class Serveur():
    def __init__(self, n: int, h: int, l: int):
        self.nbTank = n
        self.tanks = [Tank()]
        self.balles = [Balle()]

        
        self.support = [[" " for _ in range(l)] for _ in range(h)]
        self.continueJeu = True


    def updateEntites(self):
        for tank in self.tanks:
            tank.update()

        for balle in self.balles:
            balle.update()
    

    def jouer(self):
        while self.continueJeu:
            self.updateEntites()
            self.affiche()
            time.sleep(DELAI)
            

    def affiche(self):
        os.system("clear")
        for tank in self.tanks:
            tank.affiche(self.support)

        for balle in self.balles:
            balle.affiche(self.support)

        for i in range(len(self.support)):
            print("".join(self.support[i]))
                

serveur = Serveur(1, 20, 20)

serveur.jouer()

