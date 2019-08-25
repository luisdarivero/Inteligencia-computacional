import csv
import math


#Funcion que obtiene la distancia entre dos puntos
def uclidiana(x1, y1, x2, y2):
    diferencia1 = (x2 - x1)**2
    diferencia2 = (y2-y1) **2
    return math.sqrt(diferencia1 + diferencia2)
    
#Funcion que compara las distancias y guarda solo las 3 distancias mas cercanas
def compararDato(dist, lista, obj):
    try:
        if(dist < lista[0][0]):
            lista[2] = lista[1][:]
            lista[1] = lista[0][:]
            lista[0] = [dist, obj]
        elif(dist < lista[1][0]):
            lista[2] = lista[1][:]
            lista[1] = [dist, obj]
        elif(dist < lista[2][1]):
            lista[2] = [dist, obj]
    except:
        temp = [dist, obj]
        lista = [temp,temp,temp]
    
    return lista
    

def main():
    alto = float(input("Ingresa el alto del objeto: "))
    ancho = float(input("Ingresa el ancho del objeto: "))
    cercano = []

    with open('Inteligencia-computacional/2aClase/train.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            dist = uclidiana(alto,ancho,float(row[0]), float(row[1]))
            cercano = compararDato(dist, cercano, int(row[2]))
            
        print ("Tomando solo un punto de referencia Knn, el elemento que ingresaste es de tipo: " + str(cercano[0][1]))
        obj = cercano[0][1] + cercano[1][1] + cercano[2][1]
        if(obj >= 2):
            obj = "1"
        else:
            obj = "0"
        print ("Tomando Tres puntos de referencia Knn, el elemento que ingresaste es de tipo: " + obj)
        
        
try:
    main()
except Exception as e:
    print("Se detecto el siguiente error de configuracion de tu sistema al correr el codigo: " + str(e))
    
