from tkinter import *

"""
 Crée et affiche la fenêtre
"""
def creer():
    fenetre = Tk()
    fenetre.title("Quoridor")
    fenetre.wm_iconbitmap("./images/logo.ico")
    fenetre.geometry("800x800")
    
    """
    cl = Label(fenetre, text="Test")
    cl.pack()
    """
    mettre_a_jour(fenetre)
    return fenetre

"""
 Met à jour la fenêtre
 @fenetre : Fenêtre à mettre à jour
"""
def mettre_a_jour(fenetre):
    P3toP6()
    render = PhotoImage(file="./images/plateau_P6.ppm")
    render = render.zoom(10,10)
    img = Label(fenetre, image=render)
    img.image = render
    img.place(x=50, y=5)
    fenetre.update()

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

creer()
