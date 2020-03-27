import Variables
from Outils import*
from Fenetre import*

"""
 Fonction principale
"""
def quoridor():
    Variables.cases = creer_matrice(9, 9)
    Variables.barrieres_verticales = creer_matrice(8, 9)
    Variables.barrieres_horizontales = creer_matrice(9, 8)
    creerFenetre()