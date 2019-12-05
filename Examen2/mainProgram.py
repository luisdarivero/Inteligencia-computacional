from knn import Knn
from MLP import MLP
from KM import KM
from OCKRA import OCKRA

class Examen2:
    
    archivos = [
        "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//Examen2//banknote.csv",
        "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//Examen2//diabetes.csv",
        "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//Examen2//liver-disorders.csv",
        "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//Examen2//ilpd.csv",
        "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//Examen2//mammographic.csv"
    ]
    
    def runClasificator(self, clasificador):
        acumuladorAUC = 0
        acumuladorTEntrenamiento = 0
        acumuladorTClasificacion = 0
        for archivo in  self.archivos:
            auc, tiempoEntrenamiento, tiempoClasificacion = clasificador.execute(archivo)
            acumuladorAUC += auc
            acumuladorTEntrenamiento += tiempoEntrenamiento
            acumuladorTClasificacion += tiempoClasificacion
            
            
        promedioAUC = acumuladorAUC / float(len(self.archivos))
        promedioTEntrenamiento = acumuladorTEntrenamiento/ float(len(self.archivos))
        promedioTClasificacion = acumuladorTClasificacion/ float(len(self.archivos))
        return (promedioAUC, promedioTEntrenamiento, promedioTClasificacion)
    

def main():
    examen = Examen2()
    #KNN
    auc, tEntrenamiento, tClasificacion = examen.runClasificator(Knn())
    print("-------------------------------------------")
    print("Resultados de KNN:")
    print("")
    print("AUC = " + str(auc))
    print("Tiempo promedio de entrenamiento = " + str(tEntrenamiento))
    print("Tiempo promedio de clasificacion = " + str(tClasificacion))
    print("-------------------------------------------")
    print("")
    #MLP
    auc, tEntrenamiento, tClasificacion = examen.runClasificator(MLP())
    print("-------------------------------------------")
    print("Resultados de MLP:")
    print("")
    print("AUC = " + str(auc))
    print("Tiempo promedio de entrenamiento = " + str(tEntrenamiento))
    print("Tiempo promedio de clasificacion = " + str(tClasificacion))
    print("-------------------------------------------")
    print("")
    #Kmeans
    auc, tEntrenamiento, tClasificacion = examen.runClasificator(KM())
    print("-------------------------------------------")
    print("Resultados de KMeans:")
    print("")
    print("AUC = " + str(auc))
    print("Tiempo promedio de entrenamiento = " + str(tEntrenamiento))
    print("Tiempo promedio de clasificacion = " + str(tClasificacion))
    print("-------------------------------------------")
    print("")
    #OCKRA
    auc, tEntrenamiento, tClasificacion = examen.runClasificator(OCKRA())
    print("-------------------------------------------")
    print("Resultados de OCKRA:")
    print("")
    print("AUC = " + str(auc))
    print("Tiempo promedio de entrenamiento = " + str(tEntrenamiento))
    print("Tiempo promedio de clasificacion = " + str(tClasificacion))
    print("-------------------------------------------")
    print("")
    
main()