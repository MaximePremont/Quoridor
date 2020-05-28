# Fenetre.py

import Variables
from Image import*
from tkinter import *


"""
 Crée et affiche la fenêtre
"""
def creerFenetre():
    Variables.fenetre = Tk()
    Variables.fenetre.title("Quoridor")
    Variables.fenetre.wm_iconbitmap("./images/logo.ico")
    Variables.fenetre.geometry("800x800")
    
    actualiserFenetre()


"""
 Met à jour la fenêtre
"""
def actualiserFenetre():
    creer_image(generer_image())
    # L'affichage ne peut ce faire qu'avec du P6
    P3toP6()
    
    # Affichage de l'image P6 générée
    render = PhotoImage(file="./images/plateau_P6.ppm")
    render = render.zoom(10,10)
    img = Label(Variables.fenetre, image=render)
    img.image = render
    img.place(x=50, y=5)
    
    # Si pas de partie en cours
    if(Variables.tour == 0):
        
        # Mise à zéro des textes et désactivation des boutons
        barrieresTexte = Label(Variables.fenetre, text="                                    ")
        barrieresTexte.place(x=50, y=710)
        barrieresTexte = Label(Variables.fenetre, text="                                    ")
        barrieresTexte.place(x=50, y=730)
        
        boutonPion = Button(Variables.fenetre, text="Pion", state=DISABLED)
        boutonPion.place(x = 300, y = 750)
        
        boutonBarriere = boutonPion = Button(Variables.fenetre, text="Barrière", state=DISABLED)
        boutonBarriere.place(x = 400, y = 750)
        
    else:
        # Textes de barrières restantes
        barrieresTexte = Label(Variables.fenetre, text="Barrières restantes joueur 1 : "+str(Variables.barrieres_restantes1)+"    ")
        barrieresTexte.place(x=50, y=710)
        barrieresTexte = Label(Variables.fenetre, text="Barrières restantes joueur 2 : "+str(Variables.barrieres_restantes2)+"    ")
        barrieresTexte.place(x=50, y=730)
        
        # Bouton permettant de choisir de déplacer le pion
        boutonPion = Button(Variables.fenetre, text="Pion", command=cliquePion)
        boutonPion.place(x = 300, y = 750)
        
        # Bouton permettant de choisir de poser une barrière
        # Note: Bouton actif ou non selon le nombre de barrières restantes
        if(Variables.bouton):
            boutonBarriere = boutonPion = Button(Variables.fenetre, text="Barrière", command=cliqueBarriere)
            boutonBarriere.place(x = 400, y = 750)
        else:
            boutonBarriere = boutonPion = Button(Variables.fenetre, text="Barrière", state=DISABLED)
            boutonBarriere.place(x = 400, y = 750)
    
    # Texte global ( victoire ou joueur à qui c'est le tour )
    messageTexte = Label(Variables.fenetre, text=Variables.message+"                                             ")
    messageTexte.place(x=300, y=720)
    
    Variables.fenetre.update()


"""
 ## Fonction appelée par le bouton Pion
"""
def cliquePion():
    # Type de sélection 1 -> Pion
    Variables.selectionType = 1
    # Retirer la barrière en sélection si il y en a une
    if(Variables.select_barriere != [0,-1,-1]):
        Variables.select_barriere = [0,-1,-1]
        actualiserFenetre()


"""
 ## Fonction appelée par le bouton Barriere
"""
def cliqueBarriere():
    # Type de sélection 1 -> Barrière
    Variables.selectionType = 2
    Variables.select_barriere = [0,0,0]
    # Retirer la case de sélection de déplacement du pion si il y en a une
    if(Variables.select_case != 0):
        Variables.select_case = 0
    actualiserFenetre()


"""
 Permet de convertir l'image P3 en image P6
"""
def P3toP6():
    fs=open("./images/plateau_P3.ppm","r")
    fd=open("./images/plateau_P6.ppm", "w")
    txt = fs.readline().strip()
    # Définition de l'en tête du P6
    fd.write("P6 69 69 255 ")
    initialized = 0
    while(txt != ""):
        if(txt[0] != "#"):
            if(initialized < 3):
                initialized = initialized + 1
            else:
                nums = txt.split(" ")
                for i in range (len(nums)):
                    if(nums[i] != "\n" and nums[i] != ""):
                        # Ecriture des couleurs sous forme chars et non de texte
                        fd.write(chr(int(nums[i])))
        txt = fs.readline()
    fs.close()
    fd.close()