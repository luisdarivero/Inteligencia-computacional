import math
import random

class NB:
    def __init__(self):
        self.unique=0;
        self.pHam=0;
        self.pSpam=0;
        self.palabrasHam={};
        self.palabrasSpam={};
        self.cantidadHam=0;
        self.cantidadSpam=0;
        
    def train(self, mails):
        ham=0;
        spam=0;
        unicas={}
        for mail in mails:
            partes=mail.split("\t")
            if partes[0]=="ham":
                ham+=1
                for palabra in partes[1].split(" "):
                    if palabra not in self.palabrasHam:
                        self.palabrasHam[palabra]=0
                    self.palabrasHam[palabra]+=1
                    self.cantidadHam+=1
                    if palabra not in unicas:
                        unicas[palabra]=0;                    
            else:
                spam+=1
                for palabra in partes[1].split(" "):
                    if palabra not in self.palabrasSpam:
                        self.palabrasSpam[palabra]=0
                    self.palabrasSpam[palabra]+=1
                    self.cantidadSpam+=1
                    if palabra not in unicas:
                        unicas[palabra]=0;
                    
            total=ham+spam
            self.pHam=ham/total
            self.pSpam=spam/total
            self.unique=len(unicas.keys())
                
    def probSpam(self,frase):
            prob=math.log(self.pSpam)
            for palabra in frase.split(" "):
                p=0
                if palabra in self.palabrasSpam:
                    p=self.palabrasSpam[palabra]
                probPalabra=math.log((float(p)+1)/(self.cantidadSpam+self.unique))
                prob*=probPalabra
            return prob
            
    def probHam(self,frase):
            prob=math.log(self.pHam)
            for palabra in frase.split(" "):
                p=0
                if palabra in self.palabrasHam:
                    p=self.palabrasHam[palabra]
                probPalabra=math.log((float(p)+1)/(self.cantidadHam+self.unique))
                prob*=probPalabra
            return prob
            
    def classify(self, phrase):
        spam=self.probSpam(phrase)
        ham=self.probHam(phrase)
        if spam>ham:
            return "spam"
        else:
            return "ham"
    
    def test(self, mails):
        tp=0
        tn=0
        fp=0
        fn=0
        for mail in mails:
            partes=mail.split("\t")
            classFound=self.classify(partes[1])
            if partes[0]=="ham":
                if classFound=="ham":
                    tn+=1
                else:
                    fp+=1
            else:
                if classFound=="spam":
                    tp+=1
                else:
                    fn+=1
        #return (tp,tn, fp, fn)
        recall=tp/float(tp+fn)
        precision=tp/float(tp+fp)
        f1=2*(precision*recall)/(precision+recall)
        
        accuracy = (tp+tn)/float(tp+tn+fp+fn)
        return (f1,accuracy)
        
   
def readFile(archivo):
    f=open(archivo)
    lista = []
    for line in f:
        line=line.rstrip()
        lista.append(line)
    f.close()
    return lista
    
    
def aleatorios(n):
    largo = int (n*0.2)
    listaAleatorios = []
    while(len(listaAleatorios) < largo):
        listaAleatorios.append(randmNumber(1,n))
        listaAleatorios = list(dict.fromkeys(listaAleatorios))
    return listaAleatorios
        
def randmNumber(min,max):
    return random.randint(min,max)
    
def generarFolds(listaOriginal,  listaAleatorios):
        listaPruebas = []
        listaEntrenamiento = []
        contador = 1
        
        for item in listaOriginal:
            
            if(contador in listaAleatorios):
                listaPruebas.append(item)
                
            else:
                listaEntrenamiento.append(item)
            contador += 1
            
        listaReturn = []
        listaReturn.append(listaEntrenamiento)
        listaReturn.append(listaPruebas)
        return listaReturn
        
def main():
    #Se genera la lista de archivos
    fileName = "Inteligencia-computacional/Naive Bayes/spam"
    emailList = readFile(fileName)
    
    pF1 = 0
    pAccuracy = 0
    
    for x in range(10):
        #Se generan datos aleatorios
        datosEnDataset = 5574
        listaAleatorios = aleatorios(datosEnDataset)
        folds = generarFolds(emailList, listaAleatorios)
        listaEntrenamiento = folds[0]
        listaPruebas = folds[1]
        
        #Se crea el objeto NB
        nb = NB()
        #se entrena el modelo
        nb.train(listaEntrenamiento)
        #Se prueba el fold
        resultadoTest = nb.test(listaPruebas)
        pF1 += resultadoTest[0]
        pAccuracy += resultadoTest[1]
    pF1 = pF1/10
    pAccuracy = pAccuracy/10
    
    print("F1: " + str(pF1))
    print("Accuracy: " + str(pAccuracy))
    
main()
        
