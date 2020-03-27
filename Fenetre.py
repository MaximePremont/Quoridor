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
    P3toP6()
    
    render = PhotoImage(file="./images/plateau_P6.ppm")
    render = render.zoom(10,10)
    img = Label(Variables.fenetre, image=render)
    img.image = render
    img.place(x=50, y=5)
    
    barrieresTexte = Label(Variables.fenetre, text="Barrières restantes : "+str(Variables.barrieres_restantesJ)+"    ")
    barrieresTexte.place(x=50, y=710)
    
    messageTexte = Label(Variables.fenetre, text=Variables.message+"                                             ")
    messageTexte.place(x=300, y=720)
    
    if(Variables.bouton):
        boutonPion = Button(Variables.fenetre, text="Pion", command=cliquePion)
        boutonPion.place(x = 300, y = 750)
        boutonBarriere = boutonPion = Button(Variables.fenetre, text="Barrière", command=cliqueBarriere)
        boutonBarriere.place(x = 400, y = 750)
    else:
        boutonPion = Button(Variables.fenetre, text="Pion", state=DISABLED)
        boutonPion.place(x = 300, y = 750)
        boutonBarriere = boutonPion = Button(Variables.fenetre, text="Barrière", state=DISABLED)
        boutonBarriere.place(x = 400, y = 750)
    
    Variables.fenetre.update()

"""
 ## Fonction appelée par le bouton Pion
"""
def cliquePion():
    Variables.selectionType = 1
    # Suite

"""
 ## Fonction appelée par le bouton Barriere
"""
def cliqueBarriere():
    Variables.selectionType = 2
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
                        fd.write(chr(int(nums[i])))
        txt = fs.readline()
    fs.close()
    fd.close()