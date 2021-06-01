import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

#2
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',index_col=0)

#3
X = df[['Top10perc', 'F.Undergrad']].values  

#4   
y = (df['Outstate'] == 'Yes').values.astype(int)

#5
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

#6
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

#7
reg = KNeighborsRegressor()
reg.fit(X_train, y_train)

#8
predictions = reg.predict(X_test)

#9
predictions[:10]
y_test[:10]

#11
MSE = ((predictions - y_test)**2).mean()