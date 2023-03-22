#!/bin/env python3

# Modules personnels
from entite import Entite

# Modules généraux
from couleurs_ansi import *

C_BALLE = FOND_ROUGE + " " + NORMAL

inf = float("inf")

class Balle(Entite):
    def __init__(self, x: int = 10, y: int = 10, vx: float = 1, vy: float = 1, degat: float = 10, portee: float = inf):
        super().__init__(x, y, vx, vy)
        self.degat = degat
        self.portee = portee

    def bouge(self):
        super().bouge()
        self.portee -= abs(self.vx + 1j * self.vy)
    
    def update(self):
        super().update()

    def affiche(self, support: list):
        support[self.x][self.y] = C_BALLE
  
