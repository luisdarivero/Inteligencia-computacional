# -*- coding: utf-8 -*-
import random

def aleatorios(n):
    largo = int (n*0.05)
    listaAleatorios = []
    while(len(listaAleatorios) < largo):
        listaAleatorios.append(randmNumber(1,n))
        listaAleatorios = list(dict.fromkeys(listaAleatorios))
    return listaAleatorios
        
def randmNumber(min,max):
    return random.randint(min,max)
    
def generarArchivos(archivo, nombreTesting, nombreReales, listaAleatorios):
        
        f=open(archivo)
        fTesting = open(nombreTesting, 'w')
        fReales = open(nombreReales, 'w')
        
        l = f.readline()
        fTesting.write(l)
        fReales.write(l)
        
        contador = 1
        for line in f:
            
            if(contador in listaAleatorios):
                fTesting.write(line)
                
            else:
                fReales.write(line)
            contador += 1
            
        f.close()
        fTesting.close()
        fReales.close()
    
def main():
    
    
    for i in range (1,11):
        #se genera una lista con numeros aleatorios
        listaA = aleatorios(22545)#numero de lineas que tiene el archivo
        #archivo inicial
        archivo = "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//examen.csv"
        #Archivo con los datos de testing -- se va a crear
        testing = "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//examenTesting"+str(i)+".csv"
        #archivo con los datos reales -- se va a crear
        reales = "C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//examenReales"+str(i)+".csv"
        generarArchivos(archivo,testing,reales,listaA)
        print("creación de archivos finalizada")
    
main()