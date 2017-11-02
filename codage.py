from random import randrange
from functools import reduce
from math import *

def bezout(a,b):
    assert a >= b
    (r, u, v, r1, u1, v1) = (a, 1, 0, b, 0, 1)
    premiere_fois = True    
    while premiere_fois or r1 != 0:
        premiere_fois = False
        q = r//r1
        r, u, v, r1, u1, v1 = (r1, u1, v1, r - q *r1, u - q*u1, v - q*v1)
    return (u, v)

x,y=bezout(3,35)
#print (x,y)
"""
def chinois(liste):             #En entrée une liste de listes de 2 éléments avec le reste et le modulo
    M = 1
    for i in liste:
        M = M*i[1]
    Mpart = []
    for j in liste:
        Mpart += [int(M//j[1])]
    yliste = []
    for k in range (len(liste)):
        x, y = bezout(Mpart[k],liste[k][1])
        yliste+=[x]
    res = 0
    for t in range(len(liste)):
        res += liste[t][0]*Mpart[t]*yliste[t]
    return (res%M,M)"""

	
def chinois(liste):
    product = reduce(int.__mul__, [i[1] for i in liste])
    S = 0
    for rj, pj in liste:
        S += rj * bezout(product//pj, pj)[0] * product//pj
    return S % product, product
test=[[9,11],[3,13],[42,200]]
print(chinois(test))

preums = [9239, 8629, 8221, 8089, 3881, 1669]
cle = 2**607 - 1

def encryption(M, p, premiers):
    return [M + premier * randrange(50000, 200000) + p * randrange(2**20, 2**50) for premier in premiers]
    #return [M + premier * 2300 + p * 2**12 for premier in premiers]



def decrypter(L, p, premiers):
    etape1 = [c % p for c in L]
    print (etape1)
    M, _ = chinois([(c % pi, pi) for c, pi in zip(etape1, premiers)])
    print(M,_)
    return M

preum=[11,13,7]
print(decrypter(encryption(42, cle, preum), cle, preum))
