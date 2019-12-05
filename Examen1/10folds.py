import math
class KNN:
    def __init__(self, k=1):
        self.x=[]
        self.y=[]
        self.k=k
        self.cantidad=-1
    
    def cargarDatos(self,archivo):
        self.x=[]
        self.y=[]
        f=open(archivo)
        f.readline();
        for line in f:
            line=line.rstrip()
            self.cantidad+=1
            partes=line.split(",")
            self.y.append(partes[-1])
            self.x.append([])
            for p in partes[:-1]:
                self.x[self.cantidad].append(float(p))
        f.close()
        


    def euclideana(self,punto1, punto2):
        a=0
        for i in range(0, len(punto1)):
            a+=(punto1[i]-punto2[i])**2
        return math.sqrt(a)
        
    def clasificar(self,punto):
        distancias=[]
        
        for i in range(0, self.cantidad):
            
            dist=self.euclideana(self.x[i], punto)
            distancias.append((dist, self.y[i]))
            distancias=sorted(distancias, key=lambda x: x[0]) #se modica esta linea
            distancias = distancias[:self.k]
        tags={}
        for i in range(0, self.k):
            if distancias[i][1] in tags:
                tags[distancias[i][1]]+=1
            else:
                tags[distancias[i][1]]=1;
        maximo=0
        maxTag="";
        for key in tags.keys():
            if tags[key]>maximo:
                maximo=tags[key]
                maxTag=key
        return maxTag
        
    def cargarTesting(self,archivo):
            x=[]
            y=[]
            cantidad=-1
            f=open(archivo)
            f.readline();
            for line in f:
                line=line.rstrip()
                cantidad+=1
                partes=line.split(",")
                y.append(partes[-1])
                x.append([])
                for p in partes[:-1]:
                    x[cantidad].append(float(p))
            f.close()
            return (x,y) #testing,reales
            
        
    def clasificarTodos(self, objetos):
        contador = 1
        resultado=[]
        for objeto in objetos:
            resultado.append(self.clasificar(objeto))
            print("termina de clasificar: " + str(contador))
            contador += 1
        return resultado
        
    def accuracy(self, predicciones, reales):
        tn=0
        fn=0
        tp=0
        fp=0
        for i in range(0, len(reales)):
            if reales[i]=="0":
                if predicciones[i]=="0":
                    tn+=1
                else:
                    fp+=1
            else:#reales[i]=="1"
                if predicciones[i]=="0":
                    fn+=1
                else:
                    tp+=1
        return (tp+tn)/float(tp+tn+fp+fn)
                    
    def f1(self, predicciones, reales):
        tn=0
        fn=0
        tp=0
        fp=0
        for i in range(0, len(reales)):
            if reales[i]=="0":
                if predicciones[i]=="0":
                    tn+=1
                else:
                    fp+=1
            else:#reales[i]=="1"
                if predicciones[i]=="0":
                    fn+=1
                else:
                    tp+=1
        recall=tp/float(tp+fn)
        precision=tp/float(tp+fp)
        f1=2*(precision*recall)/(precision+recall)
        return f1


                    
                    
        

nombreReales = "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//examenReales"
nombreTesting = "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//examenTesting"
numeroPruebas = 10
accuracy = 0
f1 = 0
k =5

for i in range(1,numeroPruebas+1):
    clasificador=KNN(k)#crea objeto knn
    clasificador.cargarDatos(nombreReales + str(i) + ".csv")
    (testing, reales)=clasificador.cargarTesting(nombreTesting + str(i) + ".csv")
    predicciones=clasificador.clasificarTodos(testing)
    print("Termino predicciones de prueba: " + str(i))
    accuracy+=clasificador.accuracy(predicciones, reales)
    print("Termino accuracy de prueba: " + str(i))
    f1+=clasificador.f1(predicciones, reales)
    print("Termino la prueba: " + str(i))
    
print("\n\n")
print("Resultados al usar k = " + str(k))
print("\n\nAccuracy:")
print(accuracy/numeroPruebas)
print("\nf1")
print(f1/numeroPruebas)

