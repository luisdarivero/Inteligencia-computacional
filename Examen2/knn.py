from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import time

class Knn():

    def crearListas(self,FileName):
        f=open(FileName)
        l = f.readline()
        x= []
        y=[]
        for line in f:
            line=line.rstrip()
            temp = line.split(",")
            temp = map(lambda x: float(x),temp)
            y.append(temp.pop())
            x.append(temp)
        
        return [x,y] #x atributos, y labels
        
    def getAUC(self, predicciones, reales):
        tn=0
        fn=0
        tp=0
        fp=0
        for i in range(0, len(reales)):
            
            if reales[i]==0:
                if predicciones[i]==0:
                    tn+=1
                else:
                    fp+=1
            else:#reales[i]=="1"
                if predicciones[i]==0:
                    fn+=1
                else:
                    tp+=1
        #print("tn=" + str(tn) + ", fn=" + str(fn) + ", tp=" + str(tp) + ", fp=" + str(fp))
        recall=tp/float(tp+fn)
        try:
            specificity = tn / float(tn + fp)
        except:
            specificity = 1
        return (recall+specificity)/2.0
        

    def execute(self, archivo):
        #Entrenenamiento
        start = time.time()
        listas = self.crearListas(archivo)
        X = listas[0]
        y = listas[1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
        knn = KNeighborsClassifier(n_neighbors = 3)
        knn.fit(X_train,y_train)
        end = time.time()
        tiempoEntrenamiento = (end - start)
        
        #Clasificacion
        start = time.time()
        predictions = knn.predict(X_test)
        auc = self.getAUC(predictions, y_test)
        end = time.time()
        tiempoClasificacion = (end - start)
        
        
        return(auc, tiempoEntrenamiento, tiempoClasificacion)
    
