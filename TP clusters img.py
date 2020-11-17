# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:56:09 2020

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

from sklearn.cluster import KMeans
import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df = px.data.iris()

fichier = open("winequality-global.csv", "r", encoding = "utf-8")

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

l_points_rouge = []

for element in liste_blanc:
    coor_B = [float(element.split(";")[1].replace('\n','')),
            float(element.split(";")[2].replace('\n','')),
            float(element.split(";")[3].replace('\n','')),
            float(element.split(";")[4].replace('\n','')),
            float(element.split(";")[5].replace('\n','')),
            float(element.split(";")[6].replace('\n','')),
            float(element.split(";")[7].replace('\n','')),
            float(element.split(";")[8].replace('\n','')),
            float(element.split(";")[9].replace('\n','')),
            float(element.split(";")[10].replace('\n','')),
            float(element.split(";")[11].replace('\n',''))]
    l_points_blanc.append(coor_B)
    
for element in liste_rouge:
    coor_R = [float(element.split(";")[1].replace('\n','')),
            float(element.split(";")[2].replace('\n','')),
            float(element.split(";")[3].replace('\n','')),
            float(element.split(";")[4].replace('\n','')),
            float(element.split(";")[5].replace('\n','')),
            float(element.split(";")[6].replace('\n','')),
            float(element.split(";")[7].replace('\n','')),
            float(element.split(";")[8].replace('\n','')),
            float(element.split(";")[9].replace('\n','')),
            float(element.split(";")[10].replace('\n','')),
            float(element.split(";")[11].replace('\n',''))]
    l_points_rouge.append(coor_R)
    

X_B = np.array(l_points_blanc)
X_R = np.array(l_points_rouge)

kmeans_B = KMeans(n_clusters=4, random_state=0).fit(X_B)
kmeans_R = KMeans(n_clusters=4, random_state=0).fit(X_R)

labels_B = kmeans_B.labels_
labels_R = kmeans_R.labels_

cluster0_B = []
cluster1_B = []
cluster2_B = []
cluster3_B = []

cluster0_R = []
cluster1_R = []
cluster2_R = []
cluster3_R = []

for i in range(len(l_points_blanc)):
    if(labels_B[i] == 0):
        cluster0_B.append(l_points_blanc[i])
    elif(labels_B[i] == 1):
        cluster1_B.append(l_points_blanc[i])
    elif(labels_B[i] == 2):
        cluster2_B.append(l_points_blanc[i])
    elif(labels_B[i] == 3):
        cluster3_B.append(l_points_blanc[i])
        
for i in range(len(l_points_rouge)):
    if(labels_R[i] == 0):
        cluster0_R.append(l_points_blanc[i])
    elif(labels_R[i] == 1):
        cluster1_R.append(l_points_blanc[i])
    elif(labels_R[i] == 2):
        cluster2_R.append(l_points_blanc[i])
    elif(labels_R[i] == 3):
        cluster3_R.append(l_points_blanc[i])
  
for x in range(1,len(liste_type)-1):
    for y in range(1,len(liste_type)-1):
        for z in range(1,len(liste_type)-1):
            if(x != y and x != z and y != z):
                plt.close("all")
                
                fig = plt.figure()
                ax = fig.add_subplot(111, projection="3d")
                ax.set_xlabel(liste_type[x])
                ax.set_ylabel(liste_type[y])      
                ax.set_zlabel(liste_type[z])
                ax.scatter([e[x-1] for e in cluster0_B],[e[y-1] for e in cluster0_B],[e[z-1] for e in cluster0_B], s=1, color = 'green')
                ax.scatter([e[x-1] for e in cluster1_B],[e[y-1] for e in cluster1_B],[e[z-1] for e in cluster1_B], s=1, color = 'red')
                ax.scatter([e[x-1] for e in cluster2_B],[e[y-1] for e in cluster2_B],[e[z-1] for e in cluster2_B], s=1, color = 'blue')
                ax.scatter([e[x-1] for e in cluster3_B],[e[y-1] for e in cluster3_B],[e[z-1] for e in cluster3_B], s=1, color = 'yellow')
                plt.savefig("3D - Blanc - x " + liste_type[x] + " - y " + liste_type[y] + " - z  " + liste_type[z],dpi=3000)
                
                plt.close()
                
                fig = plt.figure()
                ax = fig.add_subplot(111, projection="3d")
                ax.set_xlabel(liste_type[x])
                ax.set_ylabel(liste_type[y])      
                ax.set_ylabel(liste_type[z])      
                ax.scatter([e[x-1] for e in cluster0_R],[e[y-1] for e in cluster0_R],[e[z-1] for e in cluster0_R], s=1, color = 'green')
                ax.scatter([e[x-1] for e in cluster1_R],[e[y-1] for e in cluster1_R],[e[z-1] for e in cluster1_R], s=1, color = 'red')
                ax.scatter([e[x-1] for e in cluster2_R],[e[y-1] for e in cluster2_R],[e[z-1] for e in cluster2_R], s=1, color = 'blue')
                ax.scatter([e[x-1] for e in cluster3_R],[e[y-1] for e in cluster3_R],[e[z-1] for e in cluster3_R], s=1, color = 'yellow')
                plt.savefig("3D - Rouge - x " + liste_type[x] + " - y " + liste_type[y] + " - z " + liste_type[z],dpi=3000)