import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

data=pd.read_csv("~/Documentos/inteligencia computacional/train.csv")
correlation = data.corr()
#print(correlation)
correlation = np.abs(correlation)
graph = sns.heatmap(correlation, cmap=sns.color_palette("Blues"))
plt.show()