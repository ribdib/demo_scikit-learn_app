import pandas as pd
import pickle

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


pipeline = make_pipeline(StandardScaler(),LinearRegression())

train_data = pd.read_csv("MOCK_DATA.csv")
train_features = train_data[["color", "weight", "rating"]]
train_label = train_data[["price"]]

model = pipeline.fit(train_features.values, train_label.values)

model_name = 'mock_model.sav'
pickle.dump(model, open(model_name, 'wb'))