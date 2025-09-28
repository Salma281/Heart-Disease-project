"""
Steps to Run the App:
1) Open integrated terminal from Ui folder
2) paste : streamlit run app.py
"""

import streamlit as st
import pandas as pd
import joblib


# Load the trained model
model = joblib.load("../models/final_model.pkl")

st.title("❤️Heart Disease Prediction App")
st.write("Enter patient details and get prediction if heart disease is likely.")

# Collect user input
age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", [1, 2, 3, 4])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved (thalach)", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", [1, 2, 3])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thal (3 = normal, 6 = fixed defect, 7 = reversible defect)", [3, 6, 7])

# Convert categorical inputs if necessary
sex_val = 1 if sex == "Male" else 0
# Build dataframe from inputs
raw_input = pd.DataFrame({
    "age": [age],
    "sex": [sex_val],
    "cp": [cp],
    "trestbps": [trestbps],
    "chol": [chol],
    "fbs": [fbs],
    "restecg": [restecg],
    "thalach": [thalach],
    "exang": [exang],
    "oldpeak": [oldpeak],
    "slope": [slope],
    "ca": [ca],
    "thal": [thal]
})

# Apply same one-hot encoding as training
input_data = pd.get_dummies(
    raw_input, 
    columns=["cp", "restecg", "slope", "thal"], 
    drop_first=True
)

# Align input columns with training features
model_features = model.feature_names_in_
for col in model_features:
    if col not in input_data.columns:
        input_data[col] = 0  # add missing dummy column

# Reorder to match training
input_data = input_data[model_features]


# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("Patient is likely to have heart disease.")
        st.error("Kindley, visit your Doctor.")
    else:
        st.success("Patient is unlikely to have heart disease.")
