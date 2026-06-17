import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("solubility_model.pkl")

# Page title
st.title("🧪 Molecular Solubility Predictor")

# Sidebar
st.sidebar.title("Project Information")
st.sidebar.write("Developer: Pranav Koushik")
st.sidebar.write("Model: Random Forest Regressor")
st.sidebar.write("Target: logS")

# Description
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

# Inputs
MolLogP = st.number_input("MolLogP", value=2.0)
MolWt = st.number_input("MolWt", value=200.0)
NumRotatableBonds = st.number_input("NumRotatableBonds", value=2)
AromaticProportion = st.number_input("AromaticProportion", value=0.5)

# Prediction button
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

# Model information
st.markdown("---")
st.subheader("Model Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Algorithm", "Random Forest")

with col2:
    st.metric("Target", "logS")
