import matplotlib.pyplot
import pandas
import pandas as pd
import seaborn as sns
from matplotlib import rcParams
from scipy.stats import zscore

#2
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col = 0)

#3
#I had some debugger issues with my plotting, tried to spend some time but had a lot of issues before figuring it out later on for homework.
sns.scatterplot(data = df, x = 'F.Undergrad', y = 'Expend')
sns.scatterplot(data = df, x = 'F.Undergrad', y = 'Outstate')  

#3.3
perc_accept = df['Accept'] / df['Apps']
per_enroll = df['Enroll'] / df['Accept']