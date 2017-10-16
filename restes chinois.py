# Mac Donald  Kilian
# restes chinois
# crée le 15/10/2017

from math import *

def bezout(a,b):
    x=max(a,b)
    y=min(a,b)
    i=1
    j=1
    while True:
        for num in range(x*i//y):
            j += 1
            if x*i-y*j == 1:
                return (i, j)
        i+=1

#x,y=bezout(3,35)
#print (x,y)

def chinois(liste):             #En entrée une liste de listes de 2 éléments avec le reste et le modulo
    M = 1
    for i in liste:
        M = M*i[1]
    Mpart = []
    for j in liste:
        Mpart += [int(M/j[1])]
    yliste = []
    for k in range (len(liste)):
        x, y = bezout(Mpart[k],liste[k][1])
        if Mpart[k] > liste[k][1]:
            yliste += [min(x,y)]
        else:
            yliste += [max(x,y)]
    res = 0
    for t in range(len(liste)):
        res += liste[t][0]*Mpart[t]*yliste[t]
    return (res%M,M)

test=[[1,3],[2,5],[3,7]]
print (chinois(test))
#Normalement ça marche
