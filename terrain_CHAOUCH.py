# terrain_CHAOUCH
###################################################################
# groupe <MIASHS TD02>
# David Daulasim
# Gaetan Bres
# Line-Sephora Assouan
# Sede Saizonou
# Souhaila Chaouch
# Ramata Dia 
# https://github.com/uvsq21921099/Projet2_generation_de_terrain_de_jeu
#####################################################################

########################
# import des librairies:

import tkinter as tk
import random as rd

#############
# constantes:  

largeur = 500
hauteur = 500
cote = 10
nbcol =  largeur // cote
nbligne = hauteur // cote
nombre_carre = 2500
P = nombre_carre // 2
T = 5
nbcarre_bleu = 0
cpt = 0
n = 4
couleur = ["blue", "brown"]

#######################
# Variables globales
liste = []


########################
#Les fonctions utilisées:

def grille():
    """permet de dessiner une grille """
    x0 = 0
    x1 = largeur
    y = 0
    while y < hauteur:
        y += cote
        canvas.create_line((x0,y),(largeur, y), fill = 'black')
    y = 0
    x0 = 0
    
    while x0 < largeur:
        x0 += cote
        canvas.create_line((x0,y),(x0, hauteur), fill = 'black')

def terrain_hasard():
    """permet de generer un terrain au hasard"""
    global nbcarre_bleu, cpt
    cpt +=1
    if cpt <= n:
        for j in range(0, 500, cote):
            for i in range(0,500, cote):
                carre = canvas.create_rectangle((i,j),(i + cote, j+cote), fill = rd.choice(couleur))
 x,y = 20,20   

def positionnement_personnage(event): #un clic gauche permettra de placer la balle sur la case de son choix
    global perso
    perso = canvas.create_oval(event.x,event.y, event.x+20, event.y+20, fill='violet')



def deplacement_du_personnage(event): 
    global dep, dx, dy
    canvas.move(perso, event.dx*dep, event.dy*dep)

def depl_gauche(event):
    global dx, dy
    event.dx = -1
    event.dy = 0
    canvas.move(perso)

def depl_droite(event):
    global dx, dy
    event.dx = 1
    event.dy = 0
    canvas.move(perso)
 
def depl_haut():
    global dy, dx
    event.dy = -1 
    event.dx = 0 
    canvas.move(perso)
 
def depl_bas(event):
    global dy, dx
    event.dy = 1 
    event.dx = 0
    canvas.move(perso)         
######################
# programme principal:

racine = tk.Tk()
racine.title('terrain_CHAOUCH')
#######################
# création des widgets:

canvas = tk.Canvas(racine, width = largeur, height = hauteur, bg="white")
boutton = tk.Button(racine, text = 'generer', command = terrain_hasard )
grille()

# liason des évenement
canvas.bind ("<Button-1>", positionnement_personnage )
canvas.bind ("<Left>", depl_gauche)
canvas.bind ("<Right>", depl_droite)
canvas.bind ("<Up>", depl_haut)
canvas.bind ("<Down>", depl_bas)
########################
# placement des widgets:

boutton.grid(column =0 ,row = 1)
canvas.grid(column =0 ,row = 0)

#####################
# boucle principale:
racine.mainloop()
