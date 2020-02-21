
"""
 Fonction principale
"""
def quoridor():
    cases = creer_matrice(9, 9)
    barrieres_verticales = creer_matrice(8, 9)
    barrieres_horizontales = creer_matrice(9, 8)
    pion1 = [0,4]
    pion2 = [8,4]
    select_case = 0
    barrieres_verticales[1][0] = 1
    barrieres_horizontales[6][2] = 1
    creer_image(generer_image(select_case, pion1, pion2, barrieres_verticales, barrieres_horizontales))

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
 Fonction de génération d'image
 @select_case : Case sélectionnée
 @pion1 : Case du pion 1
 @pion2 : Case du pion 2
 @barrieres_verticales : Liste des barrières verticales
 @barrieres_horizontales : Liste des barrières horizontales
"""
def generer_image(select_case, pion1, pion2, barrieres_verticales, barrieres_horizontales):
    pixels = creer_matrice(69,69)
    for a in range (9):
        for b in range (9):
            start = [8*a,8*b]
            for c in range(5):
                for d in range(5):
                    pixels[start[0]+c][start[1]+d] = "N"
            if(select_case == [a,b]):
                for e in range (5):
                    pixels[start[0]+e][start[1]] = "O"
                    pixels[start[0]+e][start[1]+4] = "O"
                for f in range (5):
                    pixels[start[0]][start[1]+f] = "O"
                    pixels[start[0]+4][start[1]+f] = "O"
            if(pion1 == [a,b]):
                for g in range(3):
                    pixels[start[0]+2][start[1]+1+g] = "R"
                for h in range(3):
                    pixels[start[0]+1+h][start[1]+2] = "R"
            elif(pion2 == [a,b]):
                for i in range(3):
                    pixels[start[0]+2][start[1]+1+i] = "B"
                for j in range(3):
                    pixels[start[0]+1+j][start[1]+2] = "B"
    for k in range (8):
        for l in range (8):
            if(barrieres_verticales[k][l] == 1):
                start_b = [k*8,l*8+5]
                for m in range (3):
                    for n in range(13):
                        pixels[start_b[0]+n][start_b[1]+m] = "V"
    for o in range (8):
        for p in range (8):
            if(barrieres_horizontales[o][p] == 1):
                start_b = [o*8+5,p*8]
                for q in range (3):
                    for r in range(13):
                        pixels[start_b[0]+q][start_b[1]+r] = "V"
    return pixels

"""
 Fonction de création de l'image
 @pixels : Matrice contenant les pixels
"""
def creer_image(pixels):
    fichier=open("plateau.ppm","w")
    fichier.write("P3\n69 69\n255\n");
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
            else:
                ligne = ligne+"255 255 255 "
        ligne = ligne+"\n"
        fichier.write(ligne)
    fichier.close()


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

