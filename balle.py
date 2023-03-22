#!/bin/env python3

# Modules personnels
from entite import Entite

# Modules généraux
from couleurs_ansi import *
from constantes import *
from utiles import *
from dessin import *

inf = float("inf")

class Balle(Entite):
    def __init__(self, x: int = 10, y: int = 10, vx: float = 0.2, vy: float = 0.3, degat: float = 10, portee: float = inf):
        super().__init__(x, y, vx, vy)
        self.degat = degat
        self.portee = portee

    def bouge(self):
        super().bouge()
        self.portee -= abs(self.vx + 1j * self.vy)
    
    def update(self):
        super().update()

    def affiche(self, cr):
        dessine_balle(self,cr)



###################################################################

if __name__ == '__main__':
    print("Ce programme n'est pas destiné à être exécuté...")
        
