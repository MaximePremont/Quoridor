# Variables.py


# Joueur qui joue actuellement
tour = 0;

# Coordonées des pions pour l'affichage
pionA2= [0,4]
pionA1= [8,4]

# Coordonnées des pions niveau logique
pion2 = [0,4]
pion1 = [8,4]

# Plateau de jeu ( matrices )
cases = 0
barrieres_verticales = 0
barrieres_horizontales = 0

# Case sélectionnée pour le déplacement
select_case = 0

# Séléction pour placer une barrière
# @arg0 -> Orientation ( 0 verticale | 1 horizontale )
# @args1/2 -> Position
select_barriere = [0, -1,-1]

# Barrières restantes pour chaquer joueur
barrieres_restantes1 = 8
barrieres_restantes2 = 8

# Variables pour le fenêtre ( bouton barrière, message de tour, object tekinter )
bouton = False
message = ""
fenetre = 0

# Chose que le joueur place : 0 Rien, 1 Pion, 2 Barière
selectionType = 0

# Confirmation : 0 Pas de confirmation, 1 Confirmation d'un pion, 2 Confirmation d'une barrière
confirmation = 0