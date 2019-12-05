import random

def fillFile(fileName):
    newFile = fileName + "New" + ".csv"

    f=open(fileName + ".csv")
    fNew=open(newFile, 'w')

    for line in f:
        #Se procesa la linea
        line= line.split(",")
        del line[9]
        del line[8]
        del line[0]
        for x in range(len(line)):
            if(line[x] == ""):
                line[x] = "-1"
        line[6] = line[6] + "\n"
        resultString = ",".join(line)
        #Se guarda
        fNew.write(resultString)

    f.close()
    fNew.close()

def oneClass(fileName):
    newFile = fileName + "OneClass" + ".csv"

    f=open(fileName + ".csv")
    fNew=open(newFile, 'w')

    fNew.write(f.readline())
    for line in f:
        #Se procesa la linea
        cadena = line.rstrip()
        if(cadena[len(cadena)-1] == "0"):
            fNew.write(line)
    f.close()
    fNew.close()

def countRows(fileName):
    f=open(fileName + ".csv")
    contador = 0
    for line in f:
        #Se procesa la linea
        contador += 1

    f.close()
    return contador

def aleatorios(n):
    largo = int (n*0.1)
    listaAleatorios = []
    while(len(listaAleatorios) < largo):
        listaAleatorios.append(randmNumber(1,n))
        listaAleatorios = list(dict.fromkeys(listaAleatorios))
    return listaAleatorios

def randmNumber(min,max):
        return random.randint(min,max)

def reducirArchivo(fileName):
    newFile = fileName + "Reduced" + ".csv"

    f=open(fileName + ".csv")
    fNew=open(newFile, 'w')

    for line in f:
        #Se procesa la linea
        if(randmNumber(1,20) == 1):
            fNew.write(line)


    f.close()
    fNew.close()

def main():
    archivo = "Apply_Rate_2019"
    reducirArchivo(archivo)

main()
