#!/usr/bin/env python3

# Codes couleur ANSI
DEFAUT = "\033[0m"  # police et couleurs par défaut

## Couleur du texte
NOIR = "\033[30m"
ROUGE = "\033[31m"
VERT = "\033[32m"
JAUNE = "\033[33m"
BLEU =  "\033[34m" 
MAGENTA = "\033[35m" 
CYAN = "\033[36m" 
BLANC = "\033[37m" 

## Couleur du fond
FOND_NOIR = "\033[1;40m"
FOND_ROUGE = "\033[1;41m"
FOND_VERT = "\033[1;42m"
FOND_MARRON = "\033[1;43m"
FOND_BLEU = "\033[1;44m"
FOND_MAGENTA = "\033[1;45m"
FOND_CYAN = "\033[1;46m"
FOND_BLANC = "\033[1;47m"

## Style de la police et effets spéciaux
NORMAL = "\033[0m"
GRAS = "\033[1m"
NON_GRAS = "\033[21m"
SOULIGNE = "\033[4m"
NON_SOULIGNE = "\033[24m"
CLIGNOTANT = "\033[5m"
NON_CLIGNOTANT = "\033[25m"
INVERSE = "\033[7m"
NON_INVERSE = "\033[27m"


###################################################################

if __name__ == '__main__':
    print("Ce programme n'est pas destiné à être exécuté...")
