# Quoridor.py

import Variables
from Outils import*
from Fenetre import*
from Commandes import*
import random
import time


"""
 Fonction principale
"""
def quoridor():
    Variables.cases = creer_matrice(9, 9)
    Variables.barrieres_verticales = creer_matrice(8, 9)
    Variables.barrieres_horizontales = creer_matrice(9, 8)
    Variables.barrieres_verticales[7][3] = 1
    Variables.select_barriere = [1,4,3]
    creerFenetre()
    # Aléatoire pour celui qui commence
    joueur = random.randint(0, 1)
    ecouteClavier()
    jeu(joueur)


"""
 Fonction du jeu
 @joueur : Joueur pour qui c'est au tour de jouer
"""
def jeu(joueur):
    if(victoire() == 0):
        if(joueur == 0):
            Variables.message = "Au tour du joueur 2"
            Variables.bouton = False
            actualiserFenetre()
            time.sleep(2)
            # Déplacement de l'ordi
            #  [IA MOOVE]
            Variables.pionO = [Variables.pionO[0]+1,Variables.pionJ[1]]
            actualiserFenetre()
            jeu(1)
            # test de victoire
        else:
            Variables.message = "Au tour du joueur 1"
            Variables.bouton = True
            Variables.confirmation = 0
            Variables.selectionType = 0
            actualiserFenetre()
    else:
        Variables.message = ">> Victoire du joueur "+str(victoire())+"<<"
        Variables.bouton = False
        actualiserFenetre()


"""
 Fonction de test de victoire
"""
def victoire():
    if(Variables.pionO[0] == 8):
        return 1
    elif(Variables.pionJ[0] == 0):
        return 2
    else:
        return 0