
from MLP import MLP
from KM import KM
from OCKRA import OCKRA
from sklearn.model_selection import train_test_split
# Wilcoxon signed-rank test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import wilcoxon


        
class ExamenFinal:
    
    archivo = "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//ExamenFinal//Apply_Rate_2019.csv"
    
    def runClasificator(self,clasificador, binario):
        acumuladorAUC = 0
        listaAUC = []
        folds = 10
        for x in  range(folds):
            if(binario):
                X_train, X_test, y_train, y_test = self.generateFold(self.archivo)
                auc = clasificador.executeFinal(X_train, X_test, y_train, y_test)
                
            else:
                X_train, X_test, y_train, y_test = self.generateFold(self.archivo)
                X_train, y_train = self.parseOneClass(X_train, y_train )
                auc = clasificador.executeFinal(X_train, X_test, y_test)
                
            acumuladorAUC += auc
            listaAUC.append(auc)
                
            
        promedioAUC = acumuladorAUC / float(folds)
        return (promedioAUC, listaAUC)
        
    def parseOneClass(self,X_train, y_train ):
        rango = range(len(y_train) -1)
        rango.reverse()
        
        
        
        for i in rango:
            if(y_train[i] == 1):
                del y_train[i]
                del X_train[i]
                
        
        return(X_train, y_train)
        
    def generateFold(self, archivo):
        listas = self.crearListas(archivo)
        X = listas[0]
        y = listas[1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
        return (X_train, X_test, y_train, y_test)
        
    def crearListas(self, FileName):
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
        
    def analisisEstadistico(self, binario, unaClase):
        stat, p = wilcoxon(binario, unaClase)
        print('Statistics=%.3f, p=%.3f' % (stat, p))
        # interpret
        alpha = 0.05
        if p > alpha:
       	    print('Same distribution (fail to reject H0)')
        else:
       	    print('Different distribution (reject H0)')
    

def main():
    examen = ExamenFinal()
    
    #MLP
    auc, listaAUC = examen.runClasificator(MLP(), True)
    print("-------------------------------------------")
    print("Resultados de MLP:")
    print("")
    print("AUC = " + str(auc))
    print("Resultados individuales = " + str(listaAUC))
    print("-------------------------------------------")
    print("")
    
    
    #Kmeans
    auc, listaKM = examen.runClasificator(KM(), False)
    print("-------------------------------------------")
    print("Resultados de KMeans:")
    print("")
    print("AUC = " + str(auc))
    print("Resultados individuales = " + str(listaKM))
    print("-------------------------------------------")
    print("")
    
    
    #OCKRA
    auc, listaOCKRA = examen.runClasificator(OCKRA(), False)
    print("-------------------------------------------")
    print("Resultados de OCKRA:")
    print("")
    print("AUC = " + str(auc))
    print("Resultados individuales = " + str(listaOCKRA))
    print("-------------------------------------------")
    print("")
    
    #Analisis Estadistico 
    
    print("")
    print("Analisis estadistico de MLP vs KM:")
    examen.analisisEstadistico(listaAUC, listaKM)
    
    print("")
    print("Analisis estadistico de MLP vs OCKRA:")
    examen.analisisEstadistico(listaAUC, listaOCKRA)
    
    
    
    
    
    
main()