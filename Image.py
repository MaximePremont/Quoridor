# Image.py

import Variables
from Outils import*


"""
 Fonction de génération d'image
"""
def generer_image():
    # Matrice de pixels dans laquelle on associera une lettre pour une couleur
    pixels = creer_matrice(69,69)
    # Tracé complet du plateau de jeu
    for a in range (9):
        for b in range (9):
            start = [8*a,8*b]
            for c in range(5):
                for d in range(5):
                    pixels[start[0]+c][start[1]+d] = "N"
            if(Variables.select_case == [a,b]):
                for e in range (5):
                    pixels[start[0]+e][start[1]] = "O"
                    pixels[start[0]+e][start[1]+4] = "O"
                for f in range (5):
                    pixels[start[0]][start[1]+f] = "O"
                    pixels[start[0]+4][start[1]+f] = "O"
            # Tracé du pion 2
            if(Variables.pionA2 == [a,b]):
                for g in range(3):
                    pixels[start[0]+2][start[1]+1+g] = "R"
                for h in range(3):
                    pixels[start[0]+1+h][start[1]+2] = "R"
            # Tracé du pion 1
            elif(Variables.pionA1 == [a,b]):
                for i in range(3):
                    pixels[start[0]+2][start[1]+1+i] = "B"
                for j in range(3):
                    pixels[start[0]+1+j][start[1]+2] = "B"
    # Tracé des barrières verticales ( classiques en vert et sélectionée en bleu )
    for k in range (8):
        for l in range (8):
            if(Variables.barrieres_verticales[k][l]):
                start_b = [k*8,l*8+5]
                for m in range (3):
                    for n in range(13):
                        pixels[start_b[0]+n][start_b[1]+m] = "V"
            if(not Variables.select_barriere[0]):
                if(Variables.select_barriere != [0,-1,-1]):
                    if(Variables.select_barriere[1] == k and Variables.select_barriere[2] == l):
                        start_b = [k*8,l*8+5]
                        for m in range (3):
                            for n in range(13):
                                pixels[start_b[0]+n][start_b[1]+m] = "T"
    # Tracé des barrières horizontales ( classiques en vert et sélectionée en bleu )
    for o in range (8):
        for p in range (8):
            if(Variables.barrieres_horizontales[o][p]):
                start_b = [o*8+5,p*8]
                for q in range (3):
                    for r in range(13):
                        pixels[start_b[0]+q][start_b[1]+r] = "V"
            if(Variables.select_barriere[0]):
                if(Variables.select_barriere != [1,-1,-1]):
                    if(Variables.select_barriere[1] == o and Variables.select_barriere[2] == p):
                        start_b = [o*8+5,p*8]
                        for q in range (3):
                            for r in range(13):
                                pixels[start_b[0]+q][start_b[1]+r] = "T"
    return pixels


"""
 Fonction de création de l'image
 @pixels : Matrice contenant les pixels
"""
def creer_image(pixels):
    # Création fichier P3 et son en-tête
    fichier=open("./images/plateau_P3.ppm","w")
    fichier.write("P3\n69 69\n255\n");
    # Utilisation de la matrice de pixels pour placer les couleurs
    for a in range(69):
        ligne = ""
        for b in range(69):
            couleur = pixels[a][b]
            if(couleur == "N"):
                ligne = ligne+"0 0 0 "
            elif(couleur == "O"):
                ligne = ligne+"255 125 0 "
            elif(couleur == "R"):
                ligne = ligne+"255 0 0 "
            elif(couleur == "B"):
                ligne = ligne+"0 0 255 "
            elif(couleur == "V"):
                ligne = ligne+"80 255 0 "
            elif(couleur == "T"):
                ligne = ligne+"40 221 227 "
            else:
                ligne = ligne+"255 255 255 "
        ligne = ligne+"\n"
        fichier.write(ligne)
    fichier.close()