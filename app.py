import streamlit as st
import numpy as np
import pickle

# Load Model
model = pickle.load(open("C:\\Users\\admin\\OneDrive\\Desktop\\ANN_DIABETES\\ANN_DIAB.keras", "rb"))

# Page Configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)

# Title
st.title("🩺 Diabetes Prediction using ANN")
st.write("Enter patient details below to predict diabetes.")

# Input Fields
pregnancies = st.number_input("Pregnancies", min_value=0.0)
glucose = st.number_input("Glucose Level", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0.0)

# Prediction Button
if st.button("Predict"):

    # Create input array
    features = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]])

    # Prediction
    features = np.array([[1, 85, 66, 29, 0, 26.6, 0.351, 31]])

    prediction = model.predict(features)

    # Output
    if prediction[0] == 1:
        st.error("⚠️ The person is likely Diabetic")
    else:
        st.success("✅ The person is Not Diabetic")