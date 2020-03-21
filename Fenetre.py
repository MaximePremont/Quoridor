from tkinter import *
from PIL import Image, ImageTk
# Necessité de télécharger PIL

def creer_fenetre():
    fenetre = Tk()
    fenetre.title("Quoridor")
    fenetre.wm_iconbitmap("logo.ico")
    
    #load = Image.open("plateau_P3.ppm")
    #render = ImageTk.PhotoImage(load)
    render = PhotoImage(file="plateau_P6.ppm")
    img = Label(fenetre, image=render)
    img.image = render
    img.place(x=0, y=0)
    
    """
    cl = Label(fenetre, text="Test")
    cl.pack()
    """
    
    fenetre.mainloop()

#creer_fenetre()

def P3toP6():
    fs=open("plateau_P3.ppm","r")
    fd=open("plateau_P6.ppm", "w")
    txt = fs.readline().strip()
    fd.write("P6\n69 69 255\n")
    initialized = 0
    while(txt != ""):
        if(txt[0] != "#"):
            if(initialized < 3):
                initialized = initialized + 1
            else:
                nums = txt.split(" ")
                print(txt)
                for i in range (len(nums)):
                    if(nums[i] != "\n" and nums[i] != ""):
                        fd.write(chr(int(nums[i])))
                #fd.write("\n")
        txt = fs.readline()
    fs.close()
    fd.close()


