# Commandes.py

import Variables
from tkinter import*
from Outils import*
from Fenetre import*
from Quoridor import*


"""
 ## Fonction appelée par la flèche de droite
 @event--
"""
def cliqueDroite(event):
    # Cas de sélection d'un pion
    if (Variables.selectionType == 1):
        # Ne pas sortir du plateau
        if(Variables.pion1[1] != 8):
            coord = [Variables.pion1[0],Variables.pion1[1]+1]
            # Impossible d'avoir 2 pions sur une même case
            if(Variables.pion2 != coord and (not barrierePresente(Variables.pion1, coord))):
                Variables.select_case = coord
                Variables.confirmation = 1
                actualiserFenetre()
    # Cas de sélection d'une barrière
    else:
        if(Variables.select_barriere[2] != 7):
            Variables.select_barriere[2] = Variables.select_barriere[2]+1
            Variables.confirmation = 2
            actualiserFenetre()

"""
 ## Fonction appelée par la flèche de gauche
 @event--
"""
def cliqueGauche(event):
    if(Variables.selectionType == 1):
        if(Variables.pion1[1] != 0):
            coord = [Variables.pion1[0],Variables.pion1[1]-1]
            if(Variables.pion2 != coord and (not barrierePresente(Variables.pion1, coord))):
                Variables.select_case = coord
                Variables.confirmation = 1
                actualiserFenetre()
    else:
        if(Variables.select_barriere[2] != 0):
            Variables.select_barriere[2] = Variables.select_barriere[2]-1
            Variables.confirmation = 2
            actualiserFenetre()
        
        
"""
 ## Fonction appelée par la flèche du bas
 @event--
"""
def cliqueBas(event):
    if(Variables.selectionType == 1):
        if(Variables.pion1[0] != 8):
            coord = [Variables.pion1[0]+1,Variables.pion1[1]]
            if(Variables.pion2 != coord and (not barrierePresente(Variables.pion1, coord))):
                Variables.select_case = coord
                Variables.confirmation = 1
                actualiserFenetre()
    else:
        if(Variables.select_barriere[1] != 7):
            Variables.select_barriere[1] = Variables.select_barriere[1]+1
            Variables.confirmation = 2
            actualiserFenetre()


"""
 ## Fonction appelée par la flèche du haut
 @event--
"""
def cliqueHaut(event):
    if(Variables.selectionType == 1):
        if(Variables.pion1[0] != 0):
            coord = [Variables.pion1[0]-1,Variables.pion1[1]]
            if(Variables.pion2 != coord and (not barrierePresente(Variables.pion1, coord))):
                Variables.select_case = coord
                Variables.confirmation = 1
                actualiserFenetre()
    else:
        if(Variables.select_barriere[1] != 0):
            Variables.select_barriere[1] = Variables.select_barriere[1]-1
            Variables.confirmation = 2
            actualiserFenetre()


"""
 ## Fonction appelée par la touche entrer ( confirmation )
 @event--
"""
def cliqueEntrer(event):
    # Cas du pion
    if(Variables.confirmation == 1):
        Variables.pion1 = Variables.select_case
        suite()
    # Cas de la barrière
    elif(Variables.confirmation == 2):
        # Barrière horizontale ou verticales
        if(Variables.select_barriere[0]):
            if(not Variables.barrieres_horizontales[Variables.select_barriere[1]][Variables.select_barriere[2]]):
                Variables.barrieres_horizontales[Variables.select_barriere[1]][Variables.select_barriere[2]] = 1
                # Retirer une barrière au bon joueur
                if(Variables.tour == 1):
                    Variables.barrieres_restantes1 = Variables.barrieres_restantes1-1;
                else:
                    Variables.barrieres_restantes2 = Variables.barrieres_restantes2-1;
                suite()
        else:
            if(not Variables.barrieres_verticales[Variables.select_barriere[1]][Variables.select_barriere[2]]):
                Variables.barrieres_verticales[Variables.select_barriere[1]][Variables.select_barriere[2]] = 1
                # Retirer une barrière au bon joueur
                if(Variables.tour == 1):
                    Variables.barrieres_restantes1 = Variables.barrieres_restantes1-1;
                else:
                    Variables.barrieres_restantes2 = Variables.barrieres_restantes2-1;
                suite()


"""
 ## Suite de l'entrée
"""
def suite():
    # Mise à zéro des variables de sélection
    Variables.select_barriere = [0,-1,-1]
    Variables.select_case = 0
    if(Variables.tour == 1):
        Variables.pionA1 = Variables.pion1
        # Inversion des variables pour intrervertir les tours
        Variables.pion1 = Variables.pionA2
        Variables.pion2 = Variables.pionA1
        jeu(0)
    else:
        Variables.pionA2 = Variables.pion1
        # Inversion des variables pour intrervertir les tours
        Variables.pion2 = Variables.pionA2
        Variables.pion1 = Variables.pionA1
        jeu(1)
    actualiserFenetre()


"""
 ## Fonction appelée par la touche espace ( tourner une barrière )
 @event--
"""
def cliqueEspace(event):
    if(not Variables.select_barriere[0]):
        Variables.select_barriere[0] = 1
    else:
        Variables.select_barriere[0] = 0
    actualiserFenetre()


"""
 Ecoute l'entrée clavier
 @fenetre : Fenêtre à mettre à jour
 @selectionType : Type de sélection ( pion ou barrière )
"""
def ecouteClavier():
    # Association de chaque touche à sa fonction
    Variables.fenetre.bind('<Right>',cliqueDroite)
    Variables.fenetre.bind('<Left>',cliqueGauche)
    Variables.fenetre.bind('<Down>',cliqueBas)
    Variables.fenetre.bind('<Up>',cliqueHaut)
    Variables.fenetre.bind('<Return>',cliqueEntrer)
    Variables.fenetre.bind('<space>',cliqueEspace)