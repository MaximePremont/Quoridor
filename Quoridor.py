# Quoridor.py

import Variables
from Outils import*
from Fenetre import*
from Commandes import*
import time

"""
 Fonction principale
"""
def quoridor():
    Variables.cases = creer_matrice(9, 9)
    Variables.barrieres_verticales = creer_matrice(8, 9)
    Variables.barrieres_horizontales = creer_matrice(9, 8)
    Variables.barrieres_verticales[7][3] = 1
    creerFenetre()
    ecouteClavier()
    jeu(1)


"""
 Fonction du jeu
 @joueur : Joueur pour qui c'est au tour de jouer
"""
def jeu(joueur):
    if(victoire() == 0):
        if(joueur == 0):
            Variables.tour = 2;
            Variables.message = "Au tour du joueur 2"
            if(Variables.barrieres_restantes2 == 0):
                Variables.bouton = False
            else:
                Variables.bouton = True
            Variables.confirmation = 0
            Variables.selectionType = 0
            actualiserFenetre()
        else:
            Variables.tour = 1;
            # ICI ===
            # pion1 = pionA1
            # pion2 = pionA2
            Variables.message = "Au tour du joueur 1"
            if(Variables.barrieres_restantes1 == 0):
                Variables.bouton = False
            else:
                Variables.bouton = True
            Variables.confirmation = 0
            Variables.selectionType = 0
            actualiserFenetre()
            # INVERSION ===
            #   pion1 = pionA2
            #   pion2 = pionA1
    else:
        Variables.message = ">> Victoire du joueur "+str(victoire())+" <<"
        Variables.bouton = False
        actualiserFenetre()


"""
 Fonction de test de victoire
"""
def victoire():
    if(Variables.pionA2[0] == 8):
        return 2
    elif(Variables.pionA1[0] == 0):
        return 1
    else:
        return 0

# Appel de la fonction principale lors du démarrage
quoridor()