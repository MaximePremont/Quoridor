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
    pionO = [0,4]
    pionJ = [8,4]
    select_case = [0,0]
    barrieres_restantesO = 8
    barrieres_restantesJ = 8
    creer_image(generer_image(select_case, pion1, pion2, barrieres_verticales, barrieres_horizontales))
    fenetre = creerFenetre(barrieres_restantesJ)
    # ecouteClavier(fenetre, selectionType)