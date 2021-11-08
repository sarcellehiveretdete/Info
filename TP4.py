# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:14:41 2021

@author: Siméon
"""
import numpy as np

#Task 1
def liste_aleatoire(n):
    L=[np.random.randint(0,100) for i in range (n)]
    return (L)

X=(liste_aleatoire(10000))

def function_insertion (liste):
    i=1
    while (i<len(liste)):
        x=liste[i]
        j=i
        while (j>0) and (liste[j-1]>x):
            liste[j]=liste[j-1]
            j=j-1
        liste[j]=x
        i+=1
    return (liste)
"""
print(function_insertion(X))
"""
#Task 2
def function_siftdown(liste, start, end):
    root=start
    while ((2*root)+1 <= end):
        child=(2*root)+1
        sw=root
        if (liste[sw]< liste[child]):
            sw= child
        if ((child+1<= end) and (liste[sw]<= liste[child+1])):
            sw=child+1
        if(sw==root):
            return liste
        else:
            (liste[root],liste[sw])=(liste[sw],liste[root])
            root=sw
    return (liste)

def function_heapify(liste, end):
    start=(end-1)//2
    while start >= 0:
        liste= function_siftdown(liste, start, len(liste)-1)
        start-=1
    return (liste)

def Heapsort (liste):
    liste= function_heapify(liste, len(liste)-1)
    end=len(liste)-1
    while end > 0:
        liste[end],liste[0]=liste[0],liste[end]
        end-=1
        liste=function_siftdown(liste, 0, end)
    return (liste)
"""
print (Heapsort(X))
"""
#Task 3
import time as t
def time (function, liste):
        A=t.time()
        function(liste)
        B=t.time()
        return (B-A)
"""   
time (Heapsort, X)
time (function_insertion, X)
"""
def liste_aleatoire_taille2_puissance_n (k):
    n= np.random.randint (3,13)
    L=np.random.randint(k,size=2**n)
    return (L)

import matplotlib.pyplot as plt

def vitesse_graphique(k):
    x=[i for i in range (3,13)]
    L=[np.random.randint(k,size=2**i) for i in range (3,13)]
    fx= [time(Heapsort,L[i]) for i in range (0,10)]
    gx= [time(function_insertion,L[i]) for i in range (0,10)]
    plt.plot(x, fx , "blue")
    plt.plot(x, gx , "red")
    plt.show()
""" 
print (vitesse_graphique (500))  
"""
#Task 6

def time2 (function, liste, valeur):
        A=t.time()
        function(liste, valeur)
        B=t.time()
        return (B-A)
    
def search(valeur, liste):
    i=0
    while ((liste[i]!= valeur) and (i< len(liste))):
        i+=1
    return (i)

def dichotomie (liste, valeur):
    l=len (liste)
    if l==1:
        return liste[0]==valeur
    while l!= 1:
        if liste[l//2] == valeur:
            return True
        if valeur > liste[l//2]:
            return dichotomie(valeur,liste[l//2:l])
        return dichotomie(valeur,liste[0:l//2])
    
def vitesse_graphique2 (n ,valeur):
    x=[i for i in range (n)]
    L=[np.random.randint(50,size=i) for i in range (n)]
    
    fx= [time2(search, L[i], valeur) for i in range (n)]
    gx= [time2(dichotomie, L[i], valeur) for i in range (n)]
    plt.plot(x, fx , "blue")
    plt.plot(x, gx , "red")
    plt.show()
    
print(vitesse_graphique2(100, 17))
        
                
        
            
            
                        
            
        
           
           
