# Outils.py
import Variables

"""
 Crée une matrice vide
 @lignes : Nombre de lignes
 @colonnes : Nombre de colonnes
"""
def creer_matrice(lignes, colonnes):
    tableau = []
    for i in range (lignes):
        colonne = [0]*colonnes
        tableau.append(colonne)
    return tableau


"""
 Vérifie si il y à une barrière entre les cases
 @case_actuelle : Coordonnées de la première case ( actuelle )
 @case_future : Coordonnées de la saconde case ( future )
"""
def barrierePresente(case_actuelle, case_future):
    barriere_presente = False
    coord_barriere1 = 0
    coord_barriere2 = 0
    print(Variables.barrieres_horizontales)
    if(case_actuelle[0] != case_future[0]):
        # Horizontale
        if(case_actuelle[0] < case_future[0]):
            coord_barriere1 = [case_actuelle[0]-2,case_actuelle[1]]
            if(case_actuelle[1] != 0):
                coord_barriere2 = [case_actuelle[0]-2,case_actuelle[1]-1]
        else:
            coord_barrire1 = [case_actuelle[0]-1,case_actuelle[1]]
            if(case_actuelle[1] != 0):
                coord_barrire2 = [case_actuelle[0]-1,case_actuelle[1]-1]
        if(Variables.barrieres_horizontales[coord_barriere1[1]][coord_barriere1[0]] == 1):
            barriere_presente = True
    else:
        # Verticale
        if(case_actuelle[1] < case_future[1]):
           coord_barriere1 = [case_actuelle[0],case_actuelle[1]]
           if(case_actuelle[0] != 0):
               coord_barriere2 = [case_actuelle[0]-1,case_actuelle[1]]
        else:
            coord_barriere1 = [case_actuelle[0],case_actuelle[1]-1]
            if(case_actuelle[0] != 0):
                coord_barriere2 = [case_actuelle[0]-1,case_actuelle[1]-1]
        if(Variables.barrieres_verticales[coord_barriere1[1]][coord_barriere1[0]] == 1):
            barriere_presente = True
    print(barriere_presente)
    return barriere_presente
        