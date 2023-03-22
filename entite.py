from constantes import *

class Entite:
    def __init__(self, x: int, y: int, vx: int, vy: int):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        
    def bouge(self):
        self.x += self.vx
        self.y += self.vy


    def update(self):
        self.bouge()


    def affiche(self, cr):
        # Affichage par défaut :  un carré noir
        cr.save()
        cr.identity_matrix()  # On démarre de zéro pour chaque nouveau dessin

        cr.scale(taille_case,taille_case)

        cr.translate(self.x+0.5,self.y+0.5) # On se positionne au milieu de la case

        r,g,b = noir
        cr.set_source_rgb(r,g,b)
        cr.rectangle(-0.5,-0.5,1.0,1.0)
        cr.fill()
        cr.restore()

        
        



###################################################################

if __name__ == '__main__':
    print("Ce programme n'est pas destiné à être exécuté...")
        
