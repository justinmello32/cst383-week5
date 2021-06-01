import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

#2
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',index_col=0)

#3
#Manually viewing the dataframe in the debugger is generally the simple way or df.info()

#4
X = df[['Outstate', 'F.Undergrad']].values     
y = (df['Private'] == 'Yes').values.astype(int) # Private = 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

#5
print(X_train[0:10])

#6
knn_class = KNeighborsClassifier(n_neighbors=3)

#7
knn_class.fit(X_train, y_train)

#8
predictions = knn_class.predict(X_test)

#9
accuracy_percent = (predictions == y_test).mean()
