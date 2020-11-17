# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:53:45 2020

@author: Alexandre

Propriétés intéressantes :
    - Type de vin [0]
    - Qualité [12]
    - Degré d'alcool [11]
    - pH [9]
    
Mise à l'écehlle du pH : 
    2.72 --> 0
    4.01 --> 100
    
    => new = (ph - 2.72)*77.519
    
3 "clusters" de Qualité :
    - 3,4,5
    - 6
    - 7,8,9    

"""

#import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#df = px.data.iris()

fichier = open("winequality-global.csv", "r", encoding = "utf-8")

#print(fichier.read())

liste_type = ["Type", "Fixed acidity", "Volatile acidity", "Citric acid", "Residual sugar", "Chlorides", "Free sulfur dioxyde", "Total sulfur dioxide", "Density", "pH", "Sulphates", "Alcohol", "Quality"]

liste_blanc = []

liste_rouge = []

#On execute une fois pour ignorer les labels de colonne
ligne = fichier.readline()


ligne = fichier.readline()

while ligne != "" :
    
    if(ligne[0] == '0'):
        liste_blanc.append(ligne)
    else:
        liste_rouge.append(ligne)
    
    ligne = fichier.readline()
    

l_points_blanc = []

blanc_X = []
blanc_Y = []
blanc_Z = []

l_points_rouge = []

rouge_X = []
rouge_Y = []
rouge_Z = []


"""
for element in liste_blanc:
    coor = (float(element.split(";")[12].replace('\n','')),float(element.split(";")[9]),float(element.split(";")[11]))
    l_points_blanc.append(coor)
    
    #blanc_X.append(coor[0])
    #blanc_Y.append(coor[1])
    
    #blanc_X.append(float(element.split(";")[axe_X].replace('\n','')))
    #blanc_Y.append(float(element.split(";")[axe_Y].replace('\n','')))
    
    blanc_Z.append(coor[2])


for element in liste_rouge:
    
    #Mis à l'échelle (pH) : 
    #coor = (float(element.split(";")[12].replace('\n','')),(float(element.split(";")[9])-2.72)*77.519,float(element.split(";")[11]))
    
    #Pas mis à l'échelle (pH) : 
    coor = (float(element.split(";")[12].replace('\n','')),float(element.split(";")[9]),float(element.split(";")[11]))
    
    
    l_points_rouge.append(coor)
    rouge_X.append(coor[0])
    rouge_Y.append(coor[1])
    rouge_Z.append(coor[2])
"""
for i in range(1, len(liste_type)):
    for j in range(1, len(liste_type)):
        rouge_X = []
        rouge_Y = []
        blanc_X = []
        blanc_Y = []
        if(i != j):
            for element in liste_rouge:
                rouge_X.append(float(element.split(";")[i].replace('\n','')))
                rouge_Y.append(float(element.split(";")[j].replace('\n','')))
                
            fig = plt.figure()
            #ax = fig.add_subplot(111,projection='3d')
            ax = fig.add_subplot(111)
            ax.set_xlabel(liste_type[i])
            ax.set_ylabel(liste_type[j])
            #ax.set_zlabel('Degré')
            #ax.scatter(blanc_X, blanc_Y, blanc_Z, color = 'green', s=5)
            #ax.scatter(rouge_X, rouge_Y, rouge_Z, color = 'red', s=1)
            
            plt.scatter(rouge_X,rouge_Y, color='red', s=1)
            plt.savefig(liste_type[j] + " en fonction de " + liste_type[i] + " rouge",dpi=3000)
            
        
"""        
X = np.array(rouge_X)
Y = np.array(rouge_Y)
Z = np.array(rouge_Z)

#print(rouge_Y)
    
fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
ax = fig.add_subplot(111)
ax.set_xlabel(str(axe_X_name))
ax.set_ylabel(str(axe_Y_name))
#ax.set_zlabel('Degré')
#ax.scatter(blanc_X, blanc_Y, blanc_Z, color = 'green', s=5)
#ax.scatter(rouge_X, rouge_Y, rouge_Z, color = 'red', s=1)

plt.scatter(blanc_X,blanc_Y, s=1)
plt.savefig(str(axe_X) + " " + str(axe_Y) + " blanc",dpi=3000)

plt.show()



#fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
#              color='species')
#fig.show()
"""