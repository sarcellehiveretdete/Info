# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:34:03 2021

@author: Siméon
"""
import numpy as np
fichier= open("C:/Users/Siméon/Downloads/input","r")
data=fichier.read()
fichier.close()

data_splitted = data.split("\n")

Matrice=[[int(data_splitted[j][i]) for i in range (32)]for j in range (32)]
"""
def affichage (Matrice):
    for i in range (32):
        print (Matrice[i])
affichage(Matrice)

"""
Matrice1=np.array(Matrice)

def k_value (i,j,Matrice):
    k=0
    for a in range (i-1,i+2):
        for b in range (j-1,j+2):
            k+=Matrice[a][b]
    k-=Matrice[i][j]
    return k

def game_of_life (Matrice):
    M=np.zeros((32,32))
    for i in range (1,len(Matrice)-1):
        for j in range (1,len(Matrice)-1):
            if ((Matrice[i][j]==0) and (k_value(i,j,Matrice)==3)):
                M[i][j]=1
            if ((Matrice[i][j]==1) and (k_value(i,j,Matrice)==2 or k_value(i,j,Matrice)==3)):
                M[i][j]=1
    return (M)

def time (t,Matrice):
    for i in range (t):
        Matrice= game_of_life(Matrice)
    return(Matrice)

import matplotlib.pyplot as plt
"""
plt.imshow(Matrice1)
plt.show(block=False)
plt.imshow(game_of_life(Matrice1))
plt.show(block=False)
plt.imshow(game_of_life(game_of_life(Matrice1)))
plt.show(block=False)
plt.imshow(game_of_life(game_of_life(game_of_life(Matrice1))))
plt.show(block=False)
"""
def graph (t,Matrice):
    for i in range (t):
        plt.imshow(time(i,Matrice))
        plt.show(block=False)
"""
graph (50, Matrice1)
"""
import matplotlib.animation as animation

def random_grid (x):
    R=np.zeros ((x,x))
    for i in range (x):
        for j in range (x):
            R[i][j]=np.random.randint (0,2)
    return(R)       
"""
graph(10, random_grid(32))
"""
A=random_grid(32)
fig , ax = plt.subplots () 
img = ax.imshow(A, cmap='gray')

def updater(frame_number, img,  M ):
    M=time(frame_number,M)
    img.set_data(M)
    return img
"""   
print (10, img, random_grid(10))
"""
ani = animation.FuncAnimation(fig, updater, fargs=(img , A),frames =100, repeat=False ,interval =200)
plt.show()
