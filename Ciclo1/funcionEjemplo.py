import numpy as np
import random 

def listShuffler(list, numberList):
    list2=[0]*len(list)
    for i in range(len(list)):
        x=numberList.index(i)
        list2[x]=list[i]
    print(list2)
    return list2

lista= ['V', 'i', 'v', 'i', 'm', 'o', 's', ' ', 'e', 'n', ' ', 'u', 'n', 'a', ' ', 's', 'o', 'c', 'i', 'e', 'd', 'a', 'd', '_', '_']
listaNumeros=[6, 14, 16, 13, 21, 4, 11, 5, 18, 15, 0, 22, 8, 7, 24, 2, 3, 12, 10, 9, 1, 23, 19, 20, 17]

listShuffler(lista, listaNumeros)