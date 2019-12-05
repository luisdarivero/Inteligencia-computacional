from sklearn.cluster import KMeans
from sklearn.metrics import roc_curve, auc
import numpy as np
import math
import random
import time

class KM:
    def aleatorios(self,n):
        largo = int (n*0.8)
        listaAleatorios = []
        while(len(listaAleatorios) < largo):
            listaAleatorios.append(self.randmNumber(1,n))
            listaAleatorios = list(dict.fromkeys(listaAleatorios))
        return listaAleatorios
            
    def randmNumber(self,min,max):
        return random.randint(min,max)
        
    def fold(self, lista):
        listaAleatorios = self.aleatorios(len(lista)-1)
        nuevaLista = []
        for x in range(0,len(lista)-1):
            if(x in listaAleatorios):
                nuevaLista.append(lista[x])
        
        return nuevaLista
            


    def cargarDatos(self,archivo):
                x=[]
                y=[]
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
                    temp = x[cantidad]
                    if(temp[len(temp)-1] == 0):
                        y.append(temp)
                f.close()
                return (y,x)
                
    
    def obtenerCentros(self,x,k):
        clusters=KMeans(n_clusters=k).fit(x)
        return clusters.cluster_centers_
        
    def euclidMin(self,centros, objetos):
        minimos=[]
        for objeto in objetos:
            minimo=np.linalg.norm(centros[0]-objeto)
            for centro in centros[1:]:
                valor=np.linalg.norm(centro-objeto)
                if valor<minimo:
                    minimo=valor
            minimos.append(minimo)
        return minimos
        
    
    
    def cargar(self, archivo):
        (real,bot) = self.cargarDatos(archivo)
        real = self.fold(real)
        cantidadReales=len(real)
        cantidadTraining=math.floor(cantidadReales*.8)
        training=real[:int(cantidadTraining)]
        testing=real[int(cantidadTraining):]
        labels=[]
        for i in range(0, len(testing)):
            labels.append(0)
        testing.extend(bot)
        for i in range(0, len(bot)):
            labels.append(1)
        return (np.array(training), np.array(testing), np.array(labels))
        
    def KMeansClassifier(self, training, testing):
        centros= self.obtenerCentros(training, 10)
        distancias=self.euclidMin(centros, testing)
        return distancias
        
    def execute(self, archivo):
        #Entrenamiento
        start = time.time()
        datos = self.cargar(archivo)
        training = datos[0]
        testing = datos[1]
        labels = datos[2]
        distanciasKMeans = self.KMeansClassifier(training, testing)
        end = time.time()
        tiempoEntrenamiento = (end - start)
        
        #Clasificacion
        start = time.time()
        fpr, tpr, thresholds=roc_curve(labels, distanciasKMeans)
        aucCalc = auc(fpr, tpr)
        end = time.time()
        tiempoClasificacion = (end - start)
        
        return(aucCalc, tiempoEntrenamiento, tiempoClasificacion)
        

        
    