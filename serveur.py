#!/bin/env python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib
import os
import os.path
import random
import math
import time

# Modules perso
from couleurs_ansi import *
from constantes import *
from utiles import *

# Objets perso
from tank import Tank
from balle import Balle


DELAI = 1

# Une classe pour les signaux
class Handler:
    def on_windowMain_destroy(self,window):
        Gtk.main_quit()
        return(True)

    def on_drawingarea_draw(self,window,context):
        serveur.affiche(context)
        return(True)


class Serveur():
    def __init__(self, n: int):
        self.nbTank = n
        self.tanks = [Tank(), Tank(x = random.randint(1,10), y=random.randint(1,10))]
        self.balles = [Balle(), Balle(x = random.randint(1,10))]

        # récupération du fichier glade
        self.builder = Gtk.Builder()
        WHERE_AM_I = os.path.abspath(os.path.dirname(__file__))
        self.glade_file = os.path.join(WHERE_AM_I, 'tanks.glade')


        # Initialisation de l'interface, assignation des variables widget
        self.builder.add_from_file(self.glade_file)       
        self.window = self.builder.get_object("windowMain")
        self.drawingarea = self.builder.get_object("drawingarea")


        # Quelques initialisations
        self.window.set_title("La grande bataille des tanks")
        self.tailleX, self.tailleY = self.window.get_size()
        
        self.builder.connect_signals(Handler())  # On connect les signaux

        self.window.show_all()  # On affiche la fenêtre principale

        self.continueJeu = True


    def updateEntites(self):
        for tank in self.tanks:
            tank.update()

        for balle in self.balles:
            balle.update()
    
    def jouer(self):
        if not self.continueJeu:
            self.terminer()
            

    def affiche(self,cr):
        """Dessin de tous les objets."""
        self.tailleX, self.tailleY = self.window.get_size()
        cr.save()

        # On met le fond (blanc)
        r,g,b = blanc
        cr.set_source_rgb(r,g,b)
        cr.rectangle(0,0,self.tailleX,self.tailleY)
        cr.fill()

        cr.scale(taille_case,taille_case)
        
        for t in self.tanks:
            t.affiche(cr)

        for b in self.balles:
            b.affiche(cr)            
        cr.restore()

    def top(self):
        """Top d'horloge : on effectue les actions."""

        # On s'assure qu'il n'y a plus d'évènement à traiter (c'est peu probable)
        while Gtk.events_pending():
            Gtk.main_iteration_do(False)           
        
        for t in self.tanks:
            t.bouge()
            t.x %= (self.tailleX // taille_case)  # On est sur un tore
            t.y %= (self.tailleY // taille_case)

            theta = angle(t.vx,t.vy)
            theta += random.random()/20  # Petit changement de direction

            # Petit changement de la norme de la vitesse
            v = norme(t.vx,t.vy)
            modif_max = vitesse_max/200
            if v+modif_max > vitesse_max:
                v = vitesse_max -2*modif_max + modif_max*random.random()
            elif v-modif_max < 0:
                v = 2*modif_max*random.random()
            else:
                v = v - modif_max + 2*modif_max*random.random()
                
            # On recalcule vx et vy
            t.vx = v*math.cos(theta)
            t.vy = v*math.sin(theta)

            # On vise quelque part
            t.orienterCanon((random.random()-0.5)/2)


            # On tire une balle de temps en temps
            if random.randint(1,20) == 1:
                theta = angle(t.vx,t.vy)
                vbx = v_balle*math.cos(t.angle_canon+theta)
                vby = v_balle*math.sin(t.angle_canon+theta)
                
                b = Balle(x = t.x, y = t.y, vx = vbx, vy = vby)
                self.balles.append(b)


        for b in self.balles:
            b.bouge()
            b.x %= (self.tailleX // taille_case)  # On est sur un tore
            b.y %= (self.tailleY // taille_case)
                

        self.drawingarea.queue_draw()
        return True

                


########################################################            
if __name__ == '__main__':

    serveur = Serveur(1)
    GLib.timeout_add(100,serveur.top)  # Toutes les 100 millisecondes, on a un top d'horloge
    Gtk.main()
