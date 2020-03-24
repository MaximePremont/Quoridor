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