# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:21:34 2020

@author: Alexandre
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

liste_type = ["Type", "Fixed acidity", "Volatile acidity", "Citric acid", "Residual sugar", "Chlorides", "Free sulfur dioxyde", "Total sulfur dioxide", "Density", "pH", "Sulphates", "Alcohol", "Quality"]

def load_data(path, wineType="w", nb_clusters=4):
    fichier = open(path, "r", encoding = "utf-8")
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
    
    l = []
    
    if(wineType=="w"):
        l = l_points_blanc
    elif(wineType=="r"):
        l = l_points_rouge
    
    labels = KMeans(n_clusters=nb_clusters, random_state=0).fit(np.array(l)).labels_
    data = {
         liste_type[1]: [e[0] for e in l],
         liste_type[2]: [e[1] for e in l],
         liste_type[3]: [e[2] for e in l],
         liste_type[4]: [e[3] for e in l],
         liste_type[5]: [e[4] for e in l],
         liste_type[6]: [e[5] for e in l],
         liste_type[7]: [e[6] for e in l],
         liste_type[8]: [e[7] for e in l],
         liste_type[9]: [e[8] for e in l],
         liste_type[10]: [e[9] for e in l],
         liste_type[11]: [e[10] for e in l],
         'cluster': labels
        }
    df = pd.DataFrame(data=data)
    
    return df

def interactive_plot(df,x,y,z):
    fig = px.scatter_3d(df, x=x, y=y, z=z,
              color='cluster')
    fig.show()
    fig.write_html('html/plot.html', auto_open=True)

def print_menu_principal():
    print("\nMenu principal\n" +
          "\n\tInteractive plot\t: p\n" + 
          "\tQuit \t\t\t: q\n")
    
def print_liste_type():
    print()
    for i in range(1,12):
        print("\t" + str(i) + " \t: " + liste_type[i])