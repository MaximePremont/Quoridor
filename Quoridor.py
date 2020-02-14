"""
 Initialisation des variables
"""
cases = []
pion1 = []
pion2 = []
barrieres = []


"""
 Fonction principale
"""
def quoridor():
    cases = creer_matrice(17, 17)
    pion1 = [16,8]
    pion2 = [0,8]

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


"""
 Vérifie la présence d'une barrière sur telle case
 @case : Case à vérifier
"""
def barriere_presente(case):
    presente = False
    for i in range(len(barrieres)):
        if(barrieres[i] == case):
            presente = True
    return presente


"""
 Fonction de génération d'image
 @select_case : Case sélectionnée
 @pion1 : Case du pion 1
 @pion2 : Case du pion 2
 @barrieres : Liste des barrières
"""
def generer_image(select_case, pion1, pion2, barrieres):
    #Suite


"""
 Crée une matrice vide
 @lignes : Nombre de lignes
 @colonnes : Nombre de colonnes
"""
def creer_matrice(lignes, colonnes):
    tableau = []
    for i in range (colonnes):
        ligne = [0]*lignes
        tableau.append(ligne)
    return tableau
