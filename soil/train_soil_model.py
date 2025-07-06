# train_soil_model.py – Train soil viability prediction model

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load the same crop dataset for demonstration
df = pd.read_csv("C:/Users/vign0/OneDrive/Desktop/web/soil/Crop_recommendation.csv")

# Generate dummy soil viability score for training (just for demo)
# You can replace this with actual expert-based values if available
df["viability"] = 60 + ((df["N"] + df["P"] + df["K"]) % 40) * 0.5  # values between 60–80

# Select features relevant to soil condition
X = df[["N", "P", "K", "temperature", "humidity", "ph"]]
y = df["viability"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "soil_model.pkl")

# Print model performance
score = model.score(X_test, y_test)
print("Soil viability model trained and saved as 'soil_model.pkl'")
print("Model R² Score on Test Set:", round(score, 4))
