#import necessary modules
import csv
with open('./train.csv','rt')as f:
    data = csv.reader(f)
    lines = 0
    classes = dict()
    for row in data:
        if lines == 15:
            print("La altura del ejemplo 15 es: " + row[0])
        lines = lines + 1
        if row[2] not in classes:
            classes[row[2]] = 1
        else:
            classes[row[2]] = classes.get(row[2]) + 1
    maxKey = 0
    maxValue = 0
    for key, value in classes.items():
        if value > maxValue:
            maxValue = value
            maxKey = key

    print("El numero de lineas que tiene el archivo es: " + str(lines))
    print("El numero de clases en el set es: " + str(len(classes)))
    print("La llave mas utilizada es: " + maxKey)
