# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

my_file = open("/amuhome/b21201528/Téléchargements/input", "r")
data = my_file.read()
my_file.close ()

data_splitted = data.split("\n")

array = [[int(data_splitted[i][j])  for  i  in  range(32)] for  j in  range(32)]

array1= np.array(array)

array2= array1
print(array2)

def V (i,j):
    k=0
    for i in range (0,32):
        for j in range (0,32):
            if array1[i-1][j-1]==1:
                k+=1
            if array1[i-1][j]==1:
                k+=1
            if array1[i-1][j+1]==1:
                k+=1
            if array1[i][j-1]==1:
                k+=1
            if array1[i][j+1]==1:
                k+=1
            if array1[i+1][j-1]==1:
                k+=1
            if array1[i+1][j]==1:
                k+=1
            if array1[i+1][j+1]==1:
                k+=1
            if (k=2 or k=3) and array1[i][j]=1)
                array2[i][j]==1
            if k==2:
                array2[i][j]==array1[i][j]
            else:
                array2[i][j]==0
print(array2)
                
                