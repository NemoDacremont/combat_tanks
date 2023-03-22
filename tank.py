#!/bin/env python3

from entite import Entite
from couleurs_ansi import *

C_TANK = FOND_BLEU + " " + NORMAL

class Tank(Entite):
    def __init__(self, x: int = 1, y: int = 1, vx: float = 1, vy: float = 1, pv: int = 1, team: int = 1):
        super().__init__(x, y, vx, vy)
        self.pv = pv
        self.team = team


    def bouge(self):
        super().bouge()
        

    def tirer(self):
        pass


    def orienterCanon(self, angle: float):
        pass


    def localiserDegats(self):
        pass


    def regarder(self):
        pass


    def recoitDonnees(self):
        pass


    def update(self):
        super().update()


    def affiche(self, support):
        support[self.x][self.y] = C_TANK
        
        
