
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


    def affiche(self, support):
        # Affiche un E
        support[self.x][self.y] = "E"

        
