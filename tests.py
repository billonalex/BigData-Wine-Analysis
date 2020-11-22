# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:00:55 2020

@author: Alexandre
"""

from functions import *


import plotly
import plotly.graph_objs as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import warnings
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


data = load_data("winequality-global.csv", 
                                     wineType="w",
                                     nb_clusters=int(4),
                                     scaled="n")

pca = PCA()

print(pca.fit(data))