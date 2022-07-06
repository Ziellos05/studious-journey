## SECUENCIAS

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
# print(a)
# print(mix[4])

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

# mix.sort()
# mixn=[1, 5, 7, 2, 4, 5]
# mixn.sort()
# mixn.reverse()
# print(mixn)

# FOR
    
# def contadorFor(n):
#     for i in range(1,n+1):
#         print (i)
        
# contadorFor(5)

# WHILE

# def contadorWhile(n):
#   i = 0
#   while i <= n:
#       print (i)
#       i += 1

# contadorWhile(5)

# Ciclos while permiten repetirse hasta no cumplir una condición de entrada

# nombre = 'roland'
# # while not nombre:
# #     nombre = input('Escribe tu nombre')
# #     print(nombre)

# # print(nombre)

# while nombre:
#     nombre = input("Escribe tu nombre")