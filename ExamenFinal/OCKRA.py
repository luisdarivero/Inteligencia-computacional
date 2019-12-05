from sklearn.cluster import KMeans
from sklearn.metrics import roc_curve, auc
import numpy as np
import math
import random
import time

class OCKRA:
    def aleatorios(self,n):
        largo = int (n*0.8)
        listaAleatorios = []
        while(len(listaAleatorios) < largo):
            listaAleatorios.append(self.randmNumber(1,n))
            listaAleatorios = list(dict.fromkeys(listaAleatorios))
        return listaAleatorios
            
    def randmNumber(self,min,max):
        return random.randint(min,max)
        
    def fold(self,lista):
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
    
    def cargar(self,archivo):
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
        
    def KMeansClassifier(self,training, testing):
        centros=self.obtenerCentros(training, 10)
        distancias=self.euclidMin(centros, testing)
        return distancias
        #plt.figure(1)
        #plt.plot(fpr, tpr)
        #plt.show()
        
    
    
    def execute(self,archivo):
        
        #Entrenamiento
        start = time.time()
        (training, testing, labels)=self.cargar(archivo)
        cantidadCaracteristicas=training.shape[1]
        distancias=[]
        for i in labels:
            distancias.append(0)
        distancias=np.array(distancias)
        end = time.time()
        tiempoEntrenamiento = (end - start)
        
        #Clasificacion
        start = time.time()
        cantidadClasificadores=30
        caracteristicas=[]
        for i in range(0, cantidadCaracteristicas):
            caracteristicas.append(i)
        for i in range(0, cantidadClasificadores):
            random.shuffle(caracteristicas)
            elegir=caracteristicas[:random.randint(3, cantidadCaracteristicas)];
            distancias=distancias+np.array(self.KMeansClassifier(training[:,elegir], testing[:,elegir]))
        distancias=distancias/cantidadClasificadores
        fpr, tpr, thresholds=roc_curve(labels, distancias)
        end = time.time()
        tiempoClasificacion = (end - start)
        
        return(auc(fpr, tpr), tiempoEntrenamiento, tiempoClasificacion)
        
    def executeFinal(self,X_train, X_test, y_test):
        #Entrenamiento
        training = X_train
        testing = X_test
        labels = y_test
        
        training = np.array(training)
        testing = np.array(testing)
        labels = np.array(labels)
        
        cantidadCaracteristicas=training.shape[1]
        distancias=[]
        for i in labels:
            distancias.append(0)
        distancias=np.array(distancias)
        
        #Clasificacion
        cantidadClasificadores=10
        caracteristicas=[]
        for i in range(0, cantidadCaracteristicas):
            caracteristicas.append(i)
        for i in range(0, cantidadClasificadores):
            random.shuffle(caracteristicas)
            elegir=caracteristicas[:random.randint(3, cantidadCaracteristicas)];
            distancias=distancias+np.array(self.KMeansClassifier(training[:,elegir], testing[:,elegir]))
        distancias=distancias/cantidadClasificadores
        fpr, tpr, thresholds=roc_curve(labels, distancias)
        
        return auc(fpr, tpr)
    
     
        
    
        
    
    