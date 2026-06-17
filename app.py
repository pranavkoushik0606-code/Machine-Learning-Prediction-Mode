import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("solubility_model.pkl")

st.title("🧪 Molecular Solubility Predictor")

st.write("Enter molecular descriptors below to predict solubility.")

MolLogP = st.number_input("MolLogP", value=2.0)
MolWt = st.number_input("MolWt", value=200.0)
NumRotatableBonds = st.number_input("NumRotatableBonds", value=2)
AromaticProportion = st.number_input("AromaticProportion", value=0.5)

if st.button("Predict Solubility"):

    input_data = pd.DataFrame({
        "MolLogP": [MolLogP],
        "MolWt": [MolWt],
        "NumRotatableBonds": [NumRotatableBonds],
        "AromaticProportion": [AromaticProportion]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Solubility (logS): {prediction[0]:.2f}")