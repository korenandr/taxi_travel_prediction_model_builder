import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression


df = pd.read_csv('taxi_dataset_with_target.csv', index_col=0)

X = df.drop(['trip_duration', 'pickup_datetime', 'passenger_count', 'store_and_fwd_flag'], axis=1)
Y = df['trip_duration']

model=LinearRegression()
model.fit(X.values, Y)

joblib.dump(model, "./model.joblib")
