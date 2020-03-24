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
 Vérifie la présence d'un pion sur une case
 @case : Case à vérifier
 @pion : Numéro du pion à tester
"""
def pion_present(case, pion):
    if(pion == 1):
        if(case == pion1):
            return True
        else:
            return False
    else:
        if(case == pion2):
            return True
        else:
            return False