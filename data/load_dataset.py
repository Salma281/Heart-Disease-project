from ucimlrepo import fetch_ucirepo 
import pandas as pd

# Fetch dataset from UCI
heart_disease = fetch_ucirepo(id=45)

# Extract features (X) and target (y)
X = heart_disease.data.features
y = heart_disease.data.targets

# Combine into one dataframe
# For clarity, analysis & storage
df = pd.concat([X, y], axis=1)

# Save into your project data folder
df.to_csv("data/heart_disease.csv", index=False)

print("Dataset saved to data/heart_disease.csv")
