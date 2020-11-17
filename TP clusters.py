# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 08:43:02 2020

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

axe_X = 7
axe_Y = 10

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
  

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel(liste_type[axe_X])
ax.set_ylabel(liste_type[axe_Y])      
plt.scatter([e[axe_X-1] for e in cluster0_B],[e[axe_Y-1] for e in cluster0_B], s=1, color = 'green')
plt.scatter([e[axe_X-1] for e in cluster1_B],[e[axe_Y-1] for e in cluster1_B], s=1, color = 'red')
plt.scatter([e[axe_X-1] for e in cluster2_B],[e[axe_Y-1] for e in cluster2_B], s=1, color = 'blue')
plt.scatter([e[axe_X-1] for e in cluster3_B],[e[axe_Y-1] for e in cluster3_B], s=1, color = 'yellow')
plt.savefig("Blanc - " + liste_type[axe_Y] + " en fonction de " + liste_type[axe_X],dpi=3000)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel(liste_type[axe_X])
ax.set_ylabel(liste_type[axe_Y])      
plt.scatter([e[axe_X-1] for e in cluster0_R],[e[axe_Y-1] for e in cluster0_R], s=1, color = 'green')
plt.scatter([e[axe_X-1] for e in cluster1_R],[e[axe_Y-1] for e in cluster1_R], s=1, color = 'red')
plt.scatter([e[axe_X-1] for e in cluster2_R],[e[axe_Y-1] for e in cluster2_R], s=1, color = 'blue')
plt.scatter([e[axe_X-1] for e in cluster3_R],[e[axe_Y-1] for e in cluster3_R], s=1, color = 'yellow')
plt.savefig("Rouge - " + liste_type[axe_Y] + " en fonction de " + liste_type[axe_X],dpi=3000)