# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:37:49 2020

@author: Alexandre

Menu interactif permettant de générer l'affichage


"""

from functions import *

print("Data Analyzer !\n")

inp = ""
nb_clusters = 0
x = 0
y = 0
z = 0

while(inp.lower() != "q"):
    
    #Affichage du menu principal
    print_menu_principal()
    inp = input("Que faire ? ")
    
    if(inp.lower() == "p"): #Demander l'affichage
        while(inp != "w" and inp.lower() != "r" and inp.lower() != "q"):
            
            #Vin rouge ou vin blanc ? Pour moi ce sera du rouge :D
            print("\n\tRed wine \t\t: r\n" + 
                  "\tWhite wine \t\t: w\n" + 
                  "\tQuit \t\t\t: q\n")
            
            inp = input("Quel vin ? ")
            
            
            
            if(inp.lower() == "w" or inp.lower() == "r"):
                
                #Quels seront les axes ?
                print_liste_type()
                
                while(int(x) <= 0): #En X
                    x = int(input("\nAxe X : "))
                while(int(y) <= 0): #En Y
                    y = int(input("\nAxe Y : "))
                while(int(z) <= 0): #En Z
                    z = int(input("\nAxe Z : "))
                
                
                while(int(nb_clusters) <= 0): #On choisit le nombre de clusters
                    nb_clusters = input("\n\nCombien de clusters ? ")
                    
                #On charge les données, et on affiche le résultat dans le navigateur
                data = load_data("winequality-global.csv", inp,int(nb_clusters))
                interactive_plot(data,liste_type[x],liste_type[y],liste_type[z])
                
        x = 0
        y = 0
        z = 0
        nb_clusters = 0
        inp = ""