import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = pd.read_csv("wholesale.csv")
categorical_feature = ['Channel','Region']
continuous_feature = ['Fresh','Milk','Grocery','Frozen','Detergents_Paper','Delicassen']
for col in categorical_feature:
 dummies = pd.get_dummies(data[col], prefix=col)
 data = pd.concat([data, dummies], axis=1)
 data.drop(col, axis=1, inplace=True)
mms = MinMaxScaler()
data_transformed = mms.fit_transform(data)
K = range(1, min(15, len(data) + 1))
Sum_of_squared_distances = []
for k in K:
 km = KMeans(n_clusters=k)
 km = km.fit(data_transformed)
 Sum_of_squared_distances.append(km.inertia_)
plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method for Optimal k')
plt.show()
