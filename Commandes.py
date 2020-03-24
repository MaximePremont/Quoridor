from tkinter import*
from Fenetre import*
from Outils import*

clavier = Tk()

def droite(event):
    if (selectionType == pion):
        if(pion_present == True ):
            print( "erreur")
        else:
            select_case = [0,0+1]
            #print("Pour confirmer appuyez sur entrer")
    else :
        if(pion_present == True ):
            print( "erreur")
        else:
            barrieres_verticales = [0,8]
            
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
 Ecoute l'entrée clavier
 @fenetre : Fenêtre à mettre à jour
 @selectionType : Type de sélection ( pion ou barrière )
"""
def ecouteClavier(fenetre, selectionType):
    clavier.bind('<Right>',droite)
    clavier.bind('<Left>',gauche)
    clavier.bind('<Down>',bas)
    clavier.bind('<Up>',haut)
    clavier.bind('<Return>',entrer)
