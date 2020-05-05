# Variables.py


pionO = [0,4]
pionJ = [8,4]
cases = 0
barrieres_verticales = 0
barrieres_horizontales = 0
select_case = 0
barrieres_restantesO = 8
barrieres_restantesJ = 8
bouton = False
message = ""
fenetre = 0
# Chose que le joueur place : 0 Rien, 1 Pion, 2 Barière
selectionType = 0
# Confirmation : 0 Pas de confirmation, 1 Confirmation d'un pion, 2 Confirmation d'une barrière
confirmation = 0
# Séléction pour placer une barrière
# @arg0 -> Orientation ( 0 verticale | 1 horizontale )
# @args1/2 -> Position
select_barriere = [0, -1,-1]