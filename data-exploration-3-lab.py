import matplotlib.pyplot
from numpy import split
import pandas
import pandas as pd
import seaborn as sns
from matplotlib import rcParams
from scipy.stats import zscore

#2
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col = 0)

#3
split = df['F.Undergrad'].quantile([0,0.33, 0.66, 1.0])
df['Size'] = pd.cut(df['F.Undergrad'], include_lowest=True, bins=breaks, labels=['small', 'medium', 'large'])

#4
graph = sns.FacetGrid(df, col='Size', height=4, aspect=0.8)
graph.map(plt.scatter, 'PhD', 'Outstate', s=20, color="r")

#5
sns.scatterplot(x='PhD', y='Outstate', hue='Size', data=df, s=50)