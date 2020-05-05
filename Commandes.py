import Variables
from tkinter import*
from Fenetre import*
from Outils import*
from Quoridor import*

"""
 ## Fonction appelée par la flèche de droite
 @event--
"""
def cliqueDroite(event):
    if (Variables.selectionType == 1):
        if(Variables.pionJ[1] != 8):
            coord = [Variables.pionJ[0],Variables.pionJ[1]+1]
            if(Variables.pionO != coord and (not barrierePresente(Variables.pionJ, coord))):
                Variables.select_case = coord
                Variables.confirmation = 1
                actualiserFenetre()
    #else:
        # Barrière suite

"""
 ## Fonction appelée par la flèche de gauche
 @event--
"""
def cliqueGauche(event):
    if(Variables.selectionType == 1):
        if(Variables.pionJ[1] != 0):
            coord = [Variables.pionJ[0],Variables.pionJ[1]-1]
            if(Variables.pionO != coord and (not barrierePresente(Variables.pionJ, coord))):
                Variables.select_case = coord
                Variables.confirmation = 1
                actualiserFenetre()
    #else:
        # Barrière suite

"""
 ## Fonction appelée par la flèche du bas
 @event--
"""
def cliqueBas(event):
    if(Variables.selectionType == 1):
        if(Variables.pionJ[0] != 8):
            coord = [Variables.pionJ[0]+1,Variables.pionJ[1]]
            if(Variables.pionO != coord and (not barrierePresente(Variables.pionJ, coord))):
                Variables.select_case = coord
                Variables.confirmation = 1
                actualiserFenetre()
    #else:
        # Barrière suite

"""
 ## Fonction appelée par la flèche du haut
 @event--
"""
def cliqueHaut(event):
    if(Variables.selectionType == 1):
        if(Variables.pionJ[0] != 0):
            coord = [Variables.pionJ[0]-1,Variables.pionJ[1]]
            if(Variables.pionO != coord and (not barrierePresente(Variables.pionJ, coord))):
                Variables.select_case = coord
                Variables.confirmation = 1
                actualiserFenetre()
    #else:
        # Barrière suite

"""
 ## Fonction appelée par la touche entrer
 @event--
"""
def cliqueEntrer(event):
    if(Variables.confirmation == 1):
        Variables.pionJ = Variables.select_case
        Variables.select_case = 0
        actualiserFenetre()
        jeu(0)
    elif(Variables.confirmation == 2):
         print("Placement barrière")
         # barrière suite
         actualiserFenetre()
         jeu(0)

"""
 ## Fonction appelée par la touche entrer
 @event--
"""
def cliqueEspace(event):
    if(Variables.select_barriere[0] == 0):
        Variables.select_barriere[0] = 1
        actualiserFenetre()
    else:
        Variables.select_barriere[0] = 0
        actualiserFenetre()

"""
 Ecoute l'entrée clavier
 @fenetre : Fenêtre à mettre à jour
 @selectionType : Type de sélection ( pion ou barrière )
"""
def ecouteClavier():
    Variables.fenetre.bind('<Right>',cliqueDroite)
    Variables.fenetre.bind('<Left>',cliqueGauche)
    Variables.fenetre.bind('<Down>',cliqueBas)
    Variables.fenetre.bind('<Up>',cliqueHaut)
    Variables.fenetre.bind('<Return>',cliqueEntrer)
    Variables.fenetre.bind('<space>',cliqueEspace)