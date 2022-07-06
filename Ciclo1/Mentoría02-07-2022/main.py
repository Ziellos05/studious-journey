import csv
import json

def comportamiento_de_la_accion(x,y):
    if x-y < 0:
        return "BAJA"
    elif x-y >0:
        return "SUBE"
    else:
        return "ESTABLE"


def readcsv(fileName):
    data = []
    with open(fileName, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data


def renglones(fileName):
    data = readcsv(fileName)
    renglones = []
    for i in range(len(data)):
        x = []
        b = abs(float(data[i][4]) - float(data[i][2]))
        a = str(data[i][0])
        x = [a, comportamiento_de_la_accion(float(data[i][4]), float(data[i][1])), str(b)]
        renglones = renglones + [x]
    return renglones


def writercsv(fileName, fileName2):
    lineas = renglones(fileName)
    fields=["Fecha", "Comportamiento_de_la_accion", "Diferencia_absoluta_open-high"]
    with open(fileName2, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        writer.writerow(fields)
        for i in range(len(lineas)):
            writer.writerow(lineas[i])

def writerjson(fileName, fileName3):
    data = readcsv(fileName)
    volumes = []
    for i in range(len(data)):
        volumes = volumes+[float(data[i][6])]
    differences = []
    for i in range(len(data)):
        differences = differences + [abs(float(data[i][4]) - float(data[i][2]))]
    lowest_volume=min(volumes)
    date_lowest_volume=str(data[volumes.index(lowest_volume)][0])
    mean_volume=sum(volumes)/len(volumes)
    greatest_difference=max(differences)
    date_greatest_difference=str(data[differences.index(greatest_difference)][0])
    smallest_difference=min(differences)
    date_smallest_difference=str(data[differences.index(smallest_difference)][0])
    detalles = {"date_lowest_volume": date_lowest_volume,
                "lowest_volume": lowest_volume,
                "mean_volume": mean_volume,
                "date_greatest_difference": date_greatest_difference,
                "greatest_difference": greatest_difference,
                "date_smallest_difference": date_smallest_difference,
                "smallest_difference": smallest_difference
                }
    with open(fileName3, 'w') as json_file:
        json.dump(detalles, json_file)
  
"""Fin espacio para programar funciones propias"""


def solucion():
    # ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    fileName = "AMAZON.csv"
    fileName2 = "analisis_archivo.csv"
    fileName3 = "detalles.json"
    writercsv(fileName, fileName2)
    writerjson(fileName, fileName3)
    return

solucion()