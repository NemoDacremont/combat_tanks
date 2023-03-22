import math

from constantes import *


def norme(x,y):
    return (x**2+y**2)**0.5


def angle(x,y):
    if x == 0:
        if y >= 0:
            theta = pi/2
        else:
            theta = -pi/2
    else:
        theta = math.atan(y/x)
        if x<0:
            theta = pi+theta
    return theta



###################################################################

if __name__ == '__main__':
    print("Ce programme n'est pas destiné à être exécuté...")
