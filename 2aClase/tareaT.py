import csv
import math



def uclidiana(x1, y1, x2, y2):
    diferencia1 = (x2 - x1)**2
    diferencia2 = (y2-y1) **2
    return math.sqrt(diferencia1 + diferencia2)

    

def main():
    alto = float(input("Ingresa el alto del objeto: "))
    ancho = float(input("Ingresa el ancho del objeto: "))
    cercano = []

    with open('train.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            dist = uclidiana(alto,ancho,float(row[0]), float(row[1]))
            try:
                if(dist < cercano[0]):
                    cercano = [dist, row[2]]
            except:
                cercano = [dist, row[2]]
        print ("El elemento que ingresaste es de tipo: " + cercano[1])
        
        
try:
    main()
except Exception as e:
    print("Se detecto el siguiente error de configuracion de tu sistema al correr el codigo: " + str(e))
    
