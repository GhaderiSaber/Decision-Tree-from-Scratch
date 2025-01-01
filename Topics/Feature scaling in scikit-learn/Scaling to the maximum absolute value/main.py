X = [[8, -2, 3], [2, 25, 0], [4, 0, -2]]

from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
X = scaler.fit_transform(X)
print(X)
