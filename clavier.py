from tkinter import*

clavier = Tk()
"""
Deplace le pion ou la barriere vers droite,gauche, haut,bas
@event : evenement à verifier
"""
def droite(event):
    if (selection == pion):
        if(pion_present == True or barriere_present == True):
            print( "erreur")
        else:
            pion1 = [0,4+1]
            print("Pour confirmer appuyez sur entrer")
    else :
        if(pion_present == True or barriere_present == True):
            print( "erreur")
        else:
            barrieres_verticales = [0,8]
            
def gauche(event):
    pion1 = [0,4-1]
    print(pion1,"Pour confirmer appuyez sur entrer")
def bas(event):
    pion1 = [0+1,4]
    print(pion1,"Pour confirmer appuyez sur entrer")
    i=i+1
def haut(event):
     pion1 = [0-1,4]
     print(pion1,"Pour confirmer appuyez sur entrer")
def entrer(event):
    pion1 = [0-1,4]
    print(pion1)

clavier.bind('<Right>',droite)
clavier.bind('<Left>',gauche)
clavier.bind('<Down>',bas)
clavier.bind('<Up>',haut)
clavier.bind('<Return>',entrer)

"""
 Vérifie la présence d'un d'une barriere sur une case
 @case : Case à vérifier
"""
def barriere_present(case):
    if(case == barrieres_verticales):
        return True
    else:
        return False
    if(case == barrieres_horizontales):
        return True
    else:
        return False
