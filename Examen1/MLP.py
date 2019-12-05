from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

def crearListas(FileName):
    f=open(FileName)
    l = f.readline()
    x= []
    y=[]
    for line in f:
        line=line.rstrip()
        temp = line.split(",")
        y.append(temp.pop())
        x.append(temp)
    
    return [x,y]

def main():
    listas = crearListas("C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//examen.csv")
    X = listas[0]
    y = listas[1]
    #Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
    #Featuring scalling
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    #training and predictions
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
    mlp.fit(X_train, y_train)
    predictions = mlp.predict(X_test)
    #evaluating the algorithm
    print(confusion_matrix(y_test,predictions))
    print(classification_report(y_test,predictions))
main()