import matplotlib.pyplot
import pandas
import pandas as pd
import seaborn as sns
from matplotlib import rcParams
from scipy.stats import zscore

#2
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv')

#3
#Completing with Dataframe explorer to get familar with data.

#4
df.info()
df.describe()

#5
df.drop(['usid','fnlwgt'], axis=1, inplace=True)

#6
df.head()

#7
df['education_num'].describe()

#8
df['education_num'].hist()