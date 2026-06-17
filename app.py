import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Molecular Solubility Predictor",
    page_icon="🧪",
    layout="wide"
)

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------
model = joblib.load("solubility_model.pkl")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("📌 Project Information")

st.sidebar.markdown("""
### 👨‍💻 Developer
Pranav Koushik

### 🤖 Model
Random Forest Regressor

### 🎯 Target
logS (Aqueous Solubility)

### 🚀 Tech Stack
- Python
- Scikit-Learn
- Streamlit
- Pandas
- Joblib
""")

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("🧪 Molecular Solubility Predictor")

st.markdown("""
This Machine Learning application predicts the **aqueous solubility of molecules**
using a **Random Forest Regression** model.

The model estimates **logS (Solubility)** from molecular descriptors.
""")

# ---------------------------------------------------
# Feature Explanation
# ---------------------------------------------------
with st.expander("ℹ️ What do these features mean?"):

    st.write("""
    **MolLogP**
    - Measures lipophilicity (fat-solubility)
    - Higher value → less water soluble

    **MolWt**
    - Molecular Weight of the compound

    **NumRotatableBonds**
    - Number of rotatable bonds
    - Indicates molecular flexibility

    **AromaticProportion**
    - Fraction of aromatic atoms
    - Indicates aromatic character of molecule
    """)

# ---------------------------------------------------
# Input Section
# ---------------------------------------------------
st.subheader("🧬 Enter Molecular Descriptors")

col1, col2 = st.columns(2)

with col1:
    MolLogP = st.number_input(
        "MolLogP",
        value=2.0,
        format="%.2f"
    )

    MolWt = st.number_input(
        "MolWt",
        value=200.0,
        format="%.2f"
    )

with col2:
    NumRotatableBonds = st.number_input(
        "NumRotatableBonds",
        value=2
    )

    AromaticProportion = st.number_input(
        "AromaticProportion",
        value=0.50,
        format="%.2f"
    )

# ---------------------------------------------------
# Prediction Button
# ---------------------------------------------------
if st.button("🔍 Predict Solubility", key="predict_button"):

    # Input Summary
    st.subheader("📋 Input Summary")

    summary_df = pd.DataFrame({
        "Feature": [
            "MolLogP",
            "MolWt",
            "NumRotatableBonds",
            "AromaticProportion"
        ],
        "Value": [
            MolLogP,
            MolWt,
            NumRotatableBonds,
            AromaticProportion
        ]
    })

    st.table(summary_df)

    # Create Input Data
    input_data = pd.DataFrame({
        "MolLogP": [MolLogP],
        "MolWt": [MolWt],
        "NumRotatableBonds": [NumRotatableBonds],
        "AromaticProportion": [AromaticProportion]
    })

    # Prediction
    prediction = model.predict(input_data)

    pred_value = float(prediction[0])

    st.subheader("📈 Prediction Result")

    st.metric(
        label="Predicted Solubility (logS)",
        value=f"{pred_value:.3f}"
    )

    # Classification
    if pred_value > -2:
        st.success("🟢 High Solubility Molecule")

    elif pred_value > -4:
        st.warning("🟡 Moderate Solubility Molecule")

    else:
        st.error("🔴 Low Solubility Molecule")

    # ---------------------------------------------------
    # Visualization
    # ---------------------------------------------------
    st.subheader("📊 Prediction Visualization")

    fig, ax = plt.subplots(figsize=(5, 3))

    ax.bar(
        ["Predicted logS"],
        [pred_value]
    )

    ax.set_ylabel("logS Value")
    ax.set_title("Predicted Solubility")

    st.pyplot(fig)

# ---------------------------------------------------
# Model Information
# ---------------------------------------------------
st.markdown("---")

st.subheader("🤖 Model Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Algorithm",
        "Random Forest"
    )

with col2:
    st.metric(
        "Target",
        "logS"
    )

with col3:
    st.metric(
        "Features",
        "4"
    )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")

st.markdown(
    """
    <center>
    <h4>Built by Pranav Koushik 🚀</h4>
    <p>Machine Learning | Streamlit | Scikit-Learn | Data Science</p>
    </center>
    """,
    unsafe_allow_html=True
)
