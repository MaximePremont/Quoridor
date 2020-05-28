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
    coord_barriere1 = [-1,-1]
    coord_barriere2 = [-1,-1]
    if(case_actuelle[0] != case_future[0]):
        # Déplacement horizontale
        if(case_actuelle[0] < case_future[0]):
            # Vers le bas
            coord_barriere1 = [case_actuelle[0],case_actuelle[1]]
            if(case_actuelle[1] != 0):
                # Barrière sur 2 niveaux
                coord_barriere2 = [case_actuelle[0],case_actuelle[1]-1]
        else:
            # Vers le haut
            coord_barriere1 = [case_actuelle[0]-1,case_actuelle[1]]
            if(case_actuelle[1] != 0):
                # Barrière sur 2 niveaux
                coord_barriere2 = [case_actuelle[0]-1,case_actuelle[1]-1]
        if(case_actuelle[1] == 8):
            # Barrière forcément sur 2 niveaux
            coord_barriere1 = [-1,-1]
        if(coord_barriere1 != [-1,-1]):
            if(Variables.barrieres_horizontales[coord_barriere1[0]][coord_barriere1[1]]):
                barriere_presente = True
        if(coord_barriere2 != [-1,-1]):
            if(Variables.barrieres_horizontales[coord_barriere2[0]][coord_barriere2[1]]):
                barriere_presente = True
    else:
        # Déplacement vertical
        if(case_actuelle[1] < case_future[1]):
            # Vers la droite
            coord_barriere1 = [case_actuelle[0],case_actuelle[1]]
            if(case_actuelle[0] != 0):
                # Barrière sur 2 niveaux
                coord_barriere2 = [case_actuelle[0]-1,case_actuelle[1]]
        else:
            # Vers la gauche
            coord_barriere1 = [case_actuelle[0],case_actuelle[1]-1]
            if(case_actuelle[0] != 0):
                # Barrière sur 2 niveaux
                coord_barriere2 = [case_actuelle[0]-1,case_actuelle[1]-1]
        if(case_actuelle[0] == 8):
            # Barrière forcément sur 2 niveaux
            coord_barriere1 = [-1,-1]
        if(coord_barriere1 != [-1,-1]):
            if(Variables.barrieres_verticales[coord_barriere1[0]][coord_barriere1[1]]):
                barriere_presente = True
        if(coord_barriere2 != [-1,-1]):
            if(Variables.barrieres_verticales[coord_barriere2[0]][coord_barriere2[1]]):
                barriere_presente = True
    return barriere_presente  