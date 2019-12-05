import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

data=pd.read_csv("C://Users//Luis Da//Documents//9o Semestre//Inteligencia computacional//examen.csv")
correlation = data.corr()
correlation = np.abs(correlation)
graph = sns.heatmap(correlation, cmap=sns.color_palette("Blues"))
plt.show()