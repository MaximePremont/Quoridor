from tkinter import*
from Variables import*
from Fenetre import*
from Outils import*

from Quoridor import*

###############################################################################
"""
def gauche(event):
    if (selectionType == pion):
        if(pion_present == True):
            print( "erreur")
        else:
            select_case = [0,4-1]
            #print("Pour confirmer appuyez sur entrer")
    else :
        if(pion_present == True): 
            print( "erreur")
        else:
            barrieres_verticales = [0,8]
def bas(event):
    if (selectionType == pion):
        if(pion_present == True ):
            print( "erreur")
        else:
            select_case = [0+1,0]
            #print("Pour confirmer appuyez sur entrer")
    else :
        if(pion_present == True ):
            print( "erreur")
        else:
            barrieres_verticales = [0+1,8]
def haut(event):
    if(selectionType == pion):
        if(pion_present == True):
            print( "erreur")
        else:
            if(select_case == [0-1,0]):
                print("erreur")
            else:
                select_case = [1-1,0]
    else:
        if(pion_present == True):
            print( "erreur")
        else:
            barrieres_verticales = [0,8+1]
"""
###############################################################################


"""
 ## Fonction appelée par la flèche de droite
 @event--
"""
def cliqueDroite(event):
    if (Variables.selectionType == 1):
        if(Variables.pionJ[1] != 8):
            Variables.select_case = [Variables.pionJ[0],Variables.pionJ[1]+1]
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
            Variables.select_case = [Variables.pionJ[0],Variables.pionJ[1]-1]
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
            Variables.select_case = [Variables.pionJ[0]+1,Variables.pionJ[1]]
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
            Variables.select_case = [Variables.pionJ[0]-1,Variables.pionJ[1]]
            actualiserFenetre()
    #else:
        # Barrière suite

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
    #Variables.fenetre.bind('<Return>',entrer)
    
def test():
    quoridor()
    Variables.selectionType = 1
    ecouteClavier()