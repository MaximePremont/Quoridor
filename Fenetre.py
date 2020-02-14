from tkinter import *
from PIL import Image, ImageTk
# Necessité de télécharger PIL

def creer_fenetre():
    fenetre = Tk()
    fenetre.title("Quoridor")
    fenetre.wm_iconbitmap("logo.ico")
    load = Image.open("negatif.ppm")
    render = ImageTk.PhotoImage(load)
    img = Label(fenetre, image=render)
    cl = Label(fenetre, text="Test")
    cl.pack()
    fenetre.mainloop()

creer_fenetre()
