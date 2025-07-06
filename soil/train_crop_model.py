# crop_recommendation.py – Train and Save Crop Recommendation Model

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("C:/Users/vign0/OneDrive/Desktop/web/soil/data/Crop_recommendation.csv")

# Split features and target label
X = df.drop("label", axis=1)
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model to a crop_model.pkl
joblib.dump(model, "crop_model.pkl")

# Print accuracy (no emoji to avoid Unicode error)
print("Model trained and saved as crop_model.pkl")
print("Accuracy on test set:", model.score(X_test, y_test))
