import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

data=pd.read_csv("~/Documentos/inteligencia computacional/twitter.csv")
#data=data[["SS","urls", "class"]]
correlation = data.corr()["class"]
correlation2 = data.corr()
correlation = np.abs(correlation)
#correlation =np.sort(correlation)
print(correlation)


graph = sns.heatmap(correlation2, cmap=sns.color_palette("Blues"))
plt.show()