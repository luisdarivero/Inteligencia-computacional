

def escribirArchivo(archivo, cadena):
    f=open(archivo, 'w')
    f.write(cadena)
    f.close()

def borrarSaltosLineaEnArchivo(archivo,nuevoArchivo):
    f=open(archivo)
    fNew=open(nuevoArchivo, 'w')
    for line in f:
        line=line.rstrip()
        fNew.write(line)
    f.close()
    fNew.close()

def fileToSTR(archivo):
    f=open(archivo)
    cadena = ""
    for line in f:
        line=line.rstrip()
        cadena += line
    f.close()
    return cadena

def escribirDatosEnArchivo(listaDatos):
    encabezado = "Estado, Nombre socursal, Direccion\n"
    fNew=open("HTMLTesla/datosTesla.csv", 'w')
    fNew.write(encabezado)
    for estado in listaDatos:

        Nombreestado = obtenerEstado(estado)
        listaSocursalesEstado = obtenerSocursales(estado)
        for socursal in listaSocursalesEstado:
            datosSocursal = obtenerDatosSocursal(socursal)
            line = Nombreestado+","+datosSocursal
            fNew.write(line + "\n")
    fNew.close()

def fillFile(fileName):
    newFile = fileName + "New" + ".csv"

    f=open(fileName + ".csv")
    fNew=open(newFile, 'w')

    for line in f:
        #Se procesa la linea
        line= line.split(",")
        for x in range(len(line)):
            if(line[x] == ""):
                line[x] = "-1"
        resultString = ",".join(line)
        #Se guarda
        fNew.write(resultString)

    f.close()
    fNew.close()

def main():
    archivo = "Apply_Rate_2019"
    fillFile(archivo)

main()
