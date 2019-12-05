from sklearn.cluster import KMeans
import math

def cargarDatos(archivo):
    x=[]
    cantidad=-1
    f=open(archivo)
    f.readline();
    for line in f:
        line=line.rstrip()
        cantidad+=1
        partes=line.split(",")
        #y.append(float(partes[-1]))
        x.append([])
        for p in partes:
            x[cantidad].append(float(p))
    f.close()
    return x
            
def centros(x, k):
    cluster=KMeans(n_clusters=k)
    
def obtenerCentros(x,k):
    clusters = KMeans(n_clusters=k).fit(x)
    return clusters.cluster_centers_
    
def euclideana(punto1, punto2):
    a=0
    for i in range(0, len(punto1)):
        a+=(punto1[i]-punto2[i])**2
    return math.sqrt(a)
    
def promedioCentroideMasCercano(x, centros):
    acumulador = 0
    for i in x:
        cercano = None
        for c in centros:
            dist = euclideana(i,c)
            if(cercano == None):
                cercano = dist
            elif(dist<cercano):
                cercano = dist
        acumulador += cercano
    promedio = acumulador / len(x)
    return promedio
    
    
def main():
    #distancias de las k
    kValues = [3,5,10]
    #se cargan los archivos
    botFile = cargarDatos("C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//Kmeans1//bot.csv")
    realFile = cargarDatos("C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//Kmeans1//real.csv")
    
    
    for k in kValues:
        centros = obtenerCentros(realFile,k)
        
        promedio = promedioCentroideMasCercano(realFile, centros)
        print ("En el archivo 'real' para k= " + str(k) + " El promedio es: " + str(promedio))
        
        promedioBot = promedioCentroideMasCercano(botFile, centros)
        print ("En el archivo 'bot' para k= " + str(k) + " El promedio es: " + str(promedioBot))
        
        print("\n")
    
        
    
    
    
main()