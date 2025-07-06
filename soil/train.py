# train_dummy_model.py

import pickle
from sklearn.ensemble import RandomForestRegressor

# Simple dummy data (6 input features: N, P, K, Temp, Humidity, pH)
X = [
    [80, 60, 70, 26, 60, 6.5],
    [30, 20, 25, 28, 65, 5.8],
    [70, 55, 60, 27, 50, 6.2],
    [90, 40, 50, 30, 70, 7.0]
]
y = [90, 60, 85, 75]  # Viability scores

# Train a simple model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
with open("soil_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("soil_model.pkl created successfully.")
