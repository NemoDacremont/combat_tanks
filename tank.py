from entite import Entite
from couleurs_ansi import *

import math

from constantes import *
from utiles import *
from dessin import *

class Tank(Entite):
    def __init__(self, x: int = 1, y: int = 1, vx: float = 0.1, vy: float = 0.2, angle_canon : float = 0.0, pv: int = 1, team: int = 1):
        super().__init__(x, y, vx, vy)
        self.angle_canon = angle_canon
        self.pv = pv
        self.team = team


    def bouge(self):
        super().bouge()
        

    def tirer(self):
        pass

    def orienterCanon(self, angle: float):
        self.angle_canon += angle


    def localiserDegats(self):
        pass


    def regarder(self):
        pass


    def recoitDonnees(self):
        pass


    def update(self):
        super().update()


    def affiche(self, cr):
        """Affichage du tank."""
        dessine_tank(self,cr)
        
        

###################################################################

if __name__ == '__main__':
    print("Ce programme n'est pas destiné à être exécuté...")
