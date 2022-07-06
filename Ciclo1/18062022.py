import numpy as np

## TUPLAS

# colores=("Azul","Verde","Rojo","Amarillo","Blanco","Negro","Gris")

# print(colores[0])
# print(colores[-1])
# colores[0] = "Café" # Intentando modificar un valor de la tupla
# print(colores[0])


## DICCIONARIOS

# edades = {"Ana": 25, "David": 18, "Lucas": 35, "Ximena": 30, "Ale": 20}

# print(edades["Lucas"])

## LISTAS

# mix = ['carro', 'bicicleta', 150, "carne", 500.5, ['teléfono', 1], 150]

# print(mix)

# a = mix[2]
# a = a+50
# mix[2] = a
# print(a)
# print(mix[5][0])

# Con esta función se obtiene el número de elementos de la lista
# print(len(mix))

# Con esta función se agregan elementos
# mix.append(1997)
# print(mix)

# Con esta función se busca cuantas veces hay un dato
# print(mix.count(150))

# Agrega un rango de elementos en la lista
# mix.extend(range(1,6))
# print(mix)

# Función que permite encontrar la posición de un dato
# print(mix.index("carne"))
# mix[3]="pollo"
# print(mix)

# mix.insert(1, "avión")
# print(mix)

# print(mix.pop())
# print(mix)

# mix.remove("carne")
# print(mix)

# mix.reverse()
# print(mix)
# b = mix[1]
# b.reverse()
# mix[1] = b
# print(mix)

# # mix.sort()
# mixn=[1, 5, 7, 2, 4, 5]
# mixn.sort()
# mixn.reverse()
# print(mixn)

# sample_list = [1, 2, 3]

# print(sample_list)

# np_list = np.array(sample_list)

# print(np_list)

# print(np.array(['este', 'es', 'un', 'vector']))

# my_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# print(my_matrix)

# print(np.array(my_matrix))

# print(np.arange(0,5))

# print(np.ones(4))

# print(np.linspace(0, 9, 10))

# print(np.eye(13))

# print(np.random.rand(3))

# arr = np.array([0,1,2,3,4,5,6,7,8])

# print(arr)

# arr= np.reshape(arr ,(3,3))

# print(arr)


# arr= arr.reshape(2,2)

# print(arr)

# simple_array = np.array([1, 2, 13, 4])

# print(simple_array)

# print(simple_array.max())

# print(simple_array.argmax())

# numpyMatrix = np.array([[101,  97,  99,  95, 110],
#  [ 32, 111, 118,  95, 110],
#  [115, 100, 111,  86, 101],
#  [115, 105,  97, 117, 109],
#  [ 32,  32, 105, 100, 105]])

# print(numpyMatrix*2)

# numpyMatrix = numpyMatrix.flatten()

# print(numpyMatrix)

# numpyMatrix = numpyMatrix.tolist()

# print(numpyMatrix)

# for i in range(len(numpyMatrix)):
#     numpyMatrix[i]=numpyMatrix[i]*2
    
# print(numpyMatrix)

# numpyMatrix = np.array(numpyMatrix)

# print(numpyMatrix)

# numpyMatrix= np.reshape(numpyMatrix ,(5,5))

# print(numpyMatrix)
    
# x=0
# while x<10:
#     print(x)
#     x=x+1

# b1 = 'b1'

# def listGenerator(string):
#     list1=[]
#     list1[:0]=string
#     return list1

# print(listGenerator(b1)[0])