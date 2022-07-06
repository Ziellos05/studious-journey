import numpy as np
import random

def listGenerator(string):
    list1=[]
    list1[:0]=string
    return list1
    
def listShuffler(list, numberList):
    list2=[0]*len(list)
    for i in range(len(list)):
        x=numberList.index(i)
        list2[i]=list[x]
        list2[i]=ord(list2[i])
    return list2

def listUnshuffler(list, numberList):
    list2=[0]*len(list)
    for i in range(len(list)):
        x=numberList.index(i)
        list2[x]=list[i]
        list2[x]=chr(list2[x])
    return list2

def encriptado(texto):
    wordsList = listGenerator(texto)
    run = ''
    while run != 'stop':
        if '0' != listGenerator(str(pow(len(wordsList),0.5)))[len(listGenerator(str(pow(len(wordsList),0.5))))-1] or '.' != listGenerator(str(pow(25,0.5)))[len(listGenerator(str(pow(25,0.5))))-2]:
            wordsList.append('_')
        else:
            run = 'stop'
    clave = np.arange(len(wordsList))
    clave=sorted(clave, key=lambda k: random.random())
    wordsList=listShuffler(wordsList, clave)
    wordsList = np.array(wordsList)
    shape = (int(pow(len(wordsList),0.5)),int(pow(len(wordsList),0.5)))
    wordsList=wordsList.reshape(shape)
    return wordsList, clave

def desencriptado(matriz_encriptado, clave):
    order=matriz_encriptado.flatten().tolist()
    order=listUnshuffler(order,clave)
    message=''
    for i in order:
        message=message+i
    character = "_"
    message = ''.join( x for x in message if x not in character)
    return message

comentario = "Hola mundo"
encriptado=encriptado(comentario)    
print(encriptado[0])
print(encriptado[1])
print(desencriptado(encriptado[0], encriptado[1]))