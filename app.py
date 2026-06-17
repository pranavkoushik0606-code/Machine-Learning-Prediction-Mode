import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("solubility_model.pkl")

st.title("🧪 Molecular Solubility Predictor")

st.markdown("""
This Machine Learning application predicts the aqueous solubility of molecules
using a Random Forest Regression model.

### Input Features
- MolLogP
- MolWt
- NumRotatableBonds
- AromaticProportion
""")

st.subheader("Enter Molecular Descriptors")

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

pred_value = float(prediction[0])

st.success(
    f"Predicted Solubility (logS): {pred_value:.3f}"
)

if pred_value > -2:
    st.info("🟢 High Solubility Molecule")
elif pred_value > -4:
    st.warning("🟡 Moderate Solubility Molecule")
else:
    st.error("🔴 Low Solubility Molecule")
st.subheader("Model Information")

st.write("Algorithm: Random Forest Regressor")
st.write("Target Variable: logS")

model = joblib.load("solubility_model.pkl")
st.sidebar.title("🧪 Project Info")

st.sidebar.write("Developer: Pranav Koushik")

st.sidebar.write("Model: Random Forest Regressor")

st.sidebar.write("Target: logS (Solubility)")
