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
    creerFenetre()
    time.sleep(10)
    # Aléatoire pour celui qui commence ( 0 : Ordi, 1 : Joueur )
    joueur = random.randint(0, 1)
    if(joueur == 0):
        Variables.message = "C'est à votre adversaire de commencer !"
    else:
        Variables.message = "C'est à vous de commencer !"
    actualiserFenetre()
    time.sleep(5)
    ecouteClavier()
    jeu(joueur)

def jeu(joueur):
        # test de victoire
        if(joueur == 0):
            Variables.message = "C'est au tour de votre de adversaire..."
            Variables.bouton = False
            actualiserFenetre()
            time.sleep(2)
            Variables.pionO = [Variables.pionO[0]+1,Variables.pionJ[1]]
            actualiserFenetre()
            jeu(1)
            # test de victoire
        else:
            Variables.message = "A vous de jouer !"
            Variables.bouton = True
            Variables.confirmation = 0
            Variables.selectionType = 0
            actualiserFenetre()
            