from tkinter import *

"""
 Crée et affiche la fenêtre
 @barrieres_restantesJ : Nombre de barrières qu'il reste au joueur
 @message : Message à afficher
 @bouton : Si on peut appuyer sur les boutons ou non
"""
def creerFenetre(barrieres_restantesJ, message, bouton):
    fenetre = Tk()
    fenetre.title("Quoridor")
    fenetre.wm_iconbitmap("./images/logo.ico")
    fenetre.geometry("800x800")
    
    actualiserFenetre(fenetre, barrieres_restantesJ, message, bouton)
    
    return fenetre

"""
 Met à jour la fenêtre
 @fenetre : Fenêtre à mettre à jour
 @barrieres_restantesJ : Nombre de barrières qu'il reste au joueur
 @message : Message à afficher
 @bouton : Si on peut appuyer sur les boutons ou non
"""
def actualiserFenetre(fenetre, barrieres_restantesJ, message, bouton):
    P3toP6()
    
    render = PhotoImage(file="./images/plateau_P6.ppm")
    render = render.zoom(10,10)
    img = Label(fenetre, image=render)
    img.image = render
    img.place(x=50, y=5)
    
    barrieresTexte = Label(fenetre, text="Barrières restantes : "+str(barrieres_restantesJ))
    barrieresTexte.place(x=50, y=710)
    
    messageTexte = Label(fenetre, text=message)
    messageTexte.place(x=300, y=720)
    
    if(bouton):
        boutonPion = Button(fenetre, text="Pion", command=cliquePion)
        boutonPion.place(x = 300, y = 750)
        boutonBarriere = boutonPion = Button(fenetre, text="Barrière", command=cliqueBarriere)
        boutonBarriere.place(x = 400, y = 750)
    else:
        boutonPion = Button(fenetre, text="Pion", state=DISABLED)
        boutonPion.place(x = 300, y = 750)
        boutonBarriere = boutonPion = Button(fenetre, text="Barrière", state=DISABLED)
        boutonBarriere.place(x = 400, y = 750)
    
    fenetre.update()

"""
 ## Fonction appelée par le bouton Pion
"""
def cliquePion():
    # Appel de la fonction clavier

"""
 ## Fonction appelée par le bouton Barriere
"""
def cliqueBarriere():
    # Appel de la fonction clavier

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