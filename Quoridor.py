from Outils import*
from Image import*
from Fenetre import*

"""
 Fonction principale
"""
def quoridor():
    cases = creer_matrice(9, 9)
    barrieres_verticales = creer_matrice(8, 9)
    barrieres_horizontales = creer_matrice(9, 8)
    pion1 = [0,4]
    pion2 = [8,4]
    select_case = [0,0]
    barreres_restantes1 = 8
    barreres_restantes2 = 8
    creer_image(generer_image(select_case, pion1, pion2, barrieres_verticales, barrieres_horizontales))
    creerFenetre()
    # ecouteClavier(fenetre, selectionType)

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