# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:10:27 2021

@author: Siméon
"""

import numpy as np

def hamdist(seq1,seq2) :
    d=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i] :
            d+=1
    return d

seq1 = 'ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC'
seq2 = 'GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA' 

"""
print(hamdist(seq1,seq2))
"""
DNA_samples = ['ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC',
'GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA',
 'TTTTCCGTCGGATTTGCTATAGCCCCTGAACGCTACATGCACGAAACCAC',
 'AGTTATGTATGCACGTCATCAATAGGACATAGCCTTGTAGTTAACAG' ,
 'TGTAGCCCGGCCGTACAGTAGAGCCTTCACCGGCATTCTGTTTG' ,
 'ATTAAGTTATTTCTATTACAGCAAAACGATCATATGCAGATCCGCAGTGCGCT',
 'GGTAGAGACACGTCCACCTAAAAAAGTGA',
 'ATGATTATCATGAGTGCCCGGCTGCTCTGTAATAGGGACCCGTTATGGTCGTGTTCGATCAGAGCGCTCTA',
 'TACGAGCAGTCGTATGCTTTCTCGAATTCCGTGCGGTTAAGCGTGACAGA',
 'TCCCAGTGCACAAAACGTGATGGCAGTCCATGCGATCATACGCAAT',
 'GGTCTCCAGACACCGGCGCACCAGTTTTCACGCCGAAAGCATC',
 'AGAAGGATAACGAGGAGCACAAATGAGAGTGTTTGAACTGGACCTGTAGTTTCTCTG',
 'ACGAAGAAACCCACCTTGAGCTGTTGCGTTGTTGCGCTGCCTAGATGCAGTGG',
 'TAACTGCGCCAAAACGTCTTCCAATCCCCTTATCCAATTTAACTCACCGC',
 'AATTCTTACAATTTAGACCCTAATATCACATCATTAGACACTAATTGCCT',
 'TCTGCCAAAATTCTGTCCACAAGCGTTTTAGTTCGCCCCAGTAAAGTTGT',
 'TCAATAACGACCACCAAATCCGCATGTTACGGGACTTCTTATTAATTCTA',
 'TTTTTCGTGGGGAGCAGCGGATCTTAATGGATGGCGCCAGGTGGTATGGA' ]
def levdist(seq1,seq2) :
    mat = np.zeros((len(seq1)+1,len(seq2)+1))
    for i in range(len(seq1)+1):
        mat[i,0]=i
    for j in range(len(seq2)+1):
        mat[0,j]=j
    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1) :
            if seq1[i-1]==seq2[j-1]:
                mat[i,j]=mat[i-1,j-1]
            else:
                cost1 = mat[i-1,j] +1
                cost2 = mat[i,j-1] + 1
                cost3 = mat[i-1,j-1] + 1
                mat[i,j]= min(cost1, cost2, cost3)
    return mat[len(seq1),len(seq2)]

"""
print(levdist('python','kryptonite'))
"""

def dist_entre_seq(liste) :
    mat = np.zeros((len(liste),len(liste)))
    for i in range(len(liste)):
        for j in range(len(liste)):
            mat[i,j]= levdist(liste[i],liste[j])
    return mat
"""
print (dist_entre_seq(DNA_samples))
"""
def verif(liste):      
    mat = np.zeros((len(liste),len(liste)))
    for i in range(len(liste)):
        for j in range(len(liste)):
            mat[i,j]= dist_entre_seq(liste[i],liste[j])
    return mat        
"""
print (verif(DNA_samples))
"""
def maxmat(mat):
    M=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if M<mat[i,j]:
                M = mat[i,j]
    return M
                
def quelindicedumax(mat):
    M= maxmat(mat)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i,j]== M:
                return [i,j]
 
def smith_waterman (seq1,seq2) :
    mat=np.zeros((len(seq1)+1, len(seq2)+1))
    fleche=np.zeros((len(seq1)+1, len(seq2)+1,2))
    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            if seq1[i-1]==seq2[j-1]:
                D = 2
            else :
                D = -2
            
            mat[i,j]= max(0,mat[i-1,j-1]+D,mat[i-1,j]-1,mat[i,j-1]-1)
            
            if mat[i,j]== mat[i-1,j-1]+D:
                fleche[i,j]=[i-1,j-1]
            if mat[i,j]==mat[i-1,j]-1:
                fleche[i,j]=[i-1,j]
            if mat[i,j]==mat[i,j-1]-1:
                fleche[i,j]=[i,j-1]
            if mat[i,j] == 0 :
                fleche[i,j]= [0,0]
                
    res=[[],[]]       
    i = quelindicedumax(mat)[0]
    j = quelindicedumax(mat)[1]
    res[0]+=seq1[i-1]
    res[1]+=seq2[j-1]
    
    k = int(fleche[i,j][0])
    l = int(fleche[i,j][1])
    
    while mat[k,l]!= 0 :
        
        if k==i-1 and l==j-1 :
            res[0]= [seq1[k-1]]+res[0]
            res[1]= [seq2[l-1]]+res[1]
        if k==i-1 and l==j:
            del res[1][0]
            res[0] = [seq1[k-1]]+res[0]
            res[1] = [seq2[l-1]]+['-']+res[1]
        if k==i and l==j-1:
            del res[0][0]
            res[0]= [seq1[k-1]]+['-']+res[0]
            res[1]= [seq2[l-1]]+res[1]
        i=k
        j=l
        k = int(fleche[i,j,0])
        l = int(fleche[i,j,1])
        
    return res

def aligner (seq1,seq2):
    res = smith_waterman(seq1,seq2)
    string1 = ''
    string2 = ''
    string3 = ''
    for i in range(len(res[0])):
        string1 = res[0][-i-1] + ' ' + string1
        string3 = res[1][-i-1] + ' ' +string3
        if res[0][-i-1]!='-' and res[1][-i-1]!= '-': 
            string2 = '| ' + string2
        else :
            string2 = '  ' + string2
    resultat = string1 + '\n' + string2 + '\n' + string3
    print (resultat)
   
aligner ('ACTAGAG','GACATAT')
aligner (DNA_samples[1], DNA_samples[2])