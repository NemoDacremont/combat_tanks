from constantes import *
from utiles import *


def dessine_tank(tank,cr):
    cr.save()      # On démarre de zéro pour chaque nouveau dessin
            
    ma_couleur = couleur[tank.team]
        
    cr.translate(tank.x+0.5,tank.y+0.5) # On se positionne au milieu de la case

    theta = angle(tank.vx,tank.vy)
    cr.rotate(theta) # On dessine dans la direction où va le tank

    # On dessine le tank
    r,g,b = noir
    cr.set_source_rgb(r,g,b)

    # Bords épais du tank
    cr.rectangle(-0.25,0.3,0.5,0.1)
    cr.rectangle(-0.25,-0.4,0.5,0.1)
    # Bords fins du tank
    cr.rectangle(-0.4,-0.25,0.05,0.5)
    cr.rectangle(0.35,-0.25,0.05,0.5)
    cr.fill()

    # Coins du tank
    theta = 0.56  # Angle entre (Ox) et (0.4, 0.25)
    rayon = 0.45
    cr.set_line_width(3 / taille_case)   # la largeur de la ligne est affectée par le scale !
    cr.arc(0,0,rayon,theta,pi/2-theta)
    cr.arc(0,0,rayon,pi/2+theta,pi-theta)
    cr.stroke()

    cr.arc(0,0,rayon,-pi/2+theta,-theta)
    cr.stroke()
    cr.arc(0,0,rayon,-pi+theta,-pi/2-theta)
    cr.stroke()

    # L'intérieur de la tourelle
    r,g,b = ma_couleur
    cr.set_source_rgb(r,g,b)
    cr.arc(0,0,0.25,0,2*pi)
    cr.fill()

    # La tourelle
    r,g,b = noir
    cr.set_source_rgb(r,g,b)
    cr.set_line_width(3 / taille_case)   # la largeur de la ligne est affectée par le scale
    cr.arc(0,0,0.25,0,2*pi)
    cr.stroke()

    # Les 4 points
    r,g,b = noir
    cr.set_source_rgb(r,g,b)
    d = 0.20
    cr.rectangle(d,d,0.05,0.05)
    cr.rectangle(d,-d,0.05,-0.05)
    cr.rectangle(-d,d,-0.05,0.05)
    cr.rectangle(-d,-d,-0.05,-0.05)
    cr.fill()

    # L'intérieur du canon
    r,g,b = ma_couleur
    cr.set_source_rgb(r,g,b)

    cr.save()
    cr.rotate(tank.angle_canon)
    cr.move_to(0.25,0.05)
    cr.line_to(0.48,0.05)
    cr.line_to(0.48,0.07)
    cr.line_to(0.50,0.07)
    cr.line_to(0.50,-0.07)
    cr.line_to(0.48,-0.07)
    cr.line_to(0.48,-0.06)
    cr.line_to(0.48,-0.05)
    cr.line_to(0.25,-0.05)
    cr.fill()

    # Le canon
    cr.set_line_width(2 / taille_case)   # la largeur de la ligne est affectée par le scale
    cr.move_to(0.25,0.05)
    cr.line_to(0.47,0.05)
    cr.line_to(0.47,0.07)
    cr.line_to(0.50,0.07)
    cr.line_to(0.50,-0.07)
    cr.line_to(0.47,-0.07)
    cr.line_to(0.47,-0.06)
    cr.line_to(0.47,-0.05)
    cr.line_to(0.25,-0.05)
    cr.stroke()
    cr.restore()

    cr.restore() # Restauration du contexte global

def dessine_balle(balle,cr):
    cr.save()      #    cr.identity_matrix()  # On démarre de zéro pour chaque nouveau dessin
    cr.translate(balle.x+0.5,balle.y+0.5) # On se positionne au milieu de la case

    theta = angle(balle.vx,balle.vy)
    cr.rotate(theta) # On dessine dans la direction où va la balle

    # On dessine la balle
    r,g,b = noir
    cr.set_source_rgb(r,g,b)

    cr.set_line_width(2 / taille_case)   # la largeur de la ligne est affectée par le scale

    # Bout pointu
    cr.move_to(0,   0.1)
    cr.line_to(0.2, 0.)
    cr.line_to(0,  -0.1)
    cr.line_to(0,   0.1)
    cr.fill()

    # Intérieur du corps de la balle
    r,g,b = gris
    cr.set_source_rgb(r,g,b)        
    cr.move_to(0, 0.1)
    cr.line_to(-0.4, 0.1)
    cr.line_to(-0.4, -0.1)
    cr.line_to(0 , -0.1)
    cr.fill()

    # Bord du corps de la balle
    cr.move_to(0, 0.1)
    cr.line_to(-0.4, 0.1)
    cr.line_to(-0.4, -0.1)
    cr.line_to(0 , -0.1)
    cr.stroke()


    r,g,b = noir
    cr.set_source_rgb(r,g,b)        
    # Ailettes

    cr.move_to(-0.2,0.1)
    cr.line_to(-0.25, 0.15)
    cr.line_to(-0.45, 0.15)
    cr.line_to(-0.4, 0.1)
    cr.fill()

    cr.move_to(-0.2, -0.1)
    cr.line_to(-0.25, -0.15)
    cr.line_to(-0.45, -0.15)
    cr.line_to(-0.4, -0.1)
    cr.fill()

    # Ailette centrale
    cr.move_to(-0.2, 0)
    cr.line_to(-0.45, 0)
    cr.stroke()

    cr.restore()



###################################################################

if __name__ == '__main__':
    print("Ce programme n'est pas destiné à être exécuté...")
    
