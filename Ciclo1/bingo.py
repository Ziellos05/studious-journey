from random import shuffle as s
import funciones.funSeparada as funSeparada

def bingo(balotera):
    s(balotera)
    sumB=0
    sumI=0
    sumN=0
    sumG=0
    sumO=0
    listaGanadora=[]
    i=0
    while sumB < 5 or sumI < 5 or sumN < 4 or sumG < 5 or sumO < 5:
        if funSeparada.letra(balotera[i]) == 'B':
            sumB=sumB+1
        elif funSeparada.letra(balotera[i]) == 'I':
            sumI=sumI+1
        elif funSeparada.letra(balotera[i]) == 'N':
            sumN=sumN+1
        elif funSeparada.letra(balotera[i]) == 'G':
            sumG=sumG+1
        else:
            sumO=sumO+1
        listaGanadora.append(balotera[i])
        i = i+1
    return listaGanadora
    
balotera=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'I16', 'I"17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'I24', 'I25', 'I26', 'I27', 'I28', 'I29', 'I30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'G46', 'G47', 'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60', 'O61', 'O62', 'O63', 'O64', 'O65', 'O66', 'O67', 'O68', 'O69', 'O70', 'O71', 'O72', 'O73', 'O74', 'O75']

print(bingo(balotera))