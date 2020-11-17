# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:41:15 2020

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

# Import dependencies
import plotly
import plotly.graph_objs as go
from sklearn.cluster import KMeans
import plotly.express as px
import pandas as pd 
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
    coor_B = [float(element.split(";")[i].replace('\n','')) for i in range(1,12)]
    l_points_blanc.append(coor_B)
    
for element in liste_rouge:
    coor_R = [float(element.split(";")[i].replace('\n','')) for i in range(1,12)]
    l_points_rouge.append(coor_R)

kmeans_B = KMeans(n_clusters=4, random_state=0).fit(np.array(l_points_blanc))
kmeans_R = KMeans(n_clusters=4, random_state=0).fit(np.array(l_points_rouge))

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
        
trace = go.Scatter3d(
    x=[e[5] for e in cluster0_B],  # <-- Put your data instead
    y=[e[6] for e in cluster0_B],  # <-- Put your data instead
    z=[e[7] for e in cluster0_B],  # <-- Put your data instead
    mode='markers',
    marker={
        'size': 10,
        'opacity': 0.8,
    }
)

# Configure the layout.
layout = go.Layout(
    margin={'l': 0, 'r': 0, 'b': 0, 't': 0}
)

data = [trace]

d = {
     liste_type[0]: [e[0] for e in l_points_blanc],
     liste_type[1]: [e[1] for e in l_points_blanc],
     liste_type[2]: [e[2] for e in l_points_blanc],
     liste_type[3]: [e[3] for e in l_points_blanc],
     liste_type[4]: [e[4] for e in l_points_blanc],
     liste_type[5]: [e[5] for e in l_points_blanc],
     liste_type[6]: [e[6] for e in l_points_blanc],
     liste_type[7]: [e[7] for e in l_points_blanc],
     liste_type[8]: [e[8] for e in l_points_blanc],
     liste_type[9]: [e[9] for e in l_points_blanc],
     liste_type[10]: [e[10] for e in l_points_blanc],
     'cluster': labels_B
    }
dd = pd.DataFrame(data=d)

df = px.data.iris()



fig = px.scatter_3d(dd, x=liste_type[5], y=liste_type[6], z=liste_type[7],
              color='cluster')
fig.show()
fig.write_html('first_figure.html', auto_open=True)

