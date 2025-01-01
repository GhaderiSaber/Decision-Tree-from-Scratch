import pandas as pd
from sklearn.preprocessing import MinMaxScaler

X = pd.DataFrame({"Area": [6574, 7865, 9832], "room_number": [5, 6, 9]})

scaler = MinMaxScaler()

X = scaler.fit_transform(X)
print(X)