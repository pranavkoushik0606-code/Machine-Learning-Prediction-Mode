# 🧪 Molecular Solubility Predictor

A Machine Learning web application that predicts the **aqueous solubility (logS)** of molecules using a **Random Forest Regression** model.

🔗 **Live Demo:**  
https://molecular-solubility-predictor.streamlit.app

---

## 📖 Project Overview

Molecular solubility is an important property in pharmaceutical and chemical research. This project uses a Machine Learning model trained on molecular descriptors to predict the solubility of molecules in water.

The application provides an easy-to-use web interface built with Streamlit where users can enter molecular descriptors and instantly obtain a solubility prediction.

---

## 🚀 Features

✅ Predict molecular solubility (logS)

✅ Interactive Streamlit web application

✅ Input feature explanations

✅ Solubility classification

- 🟢 High Solubility
- 🟡 Moderate Solubility
- 🔴 Low Solubility

✅ Cloud deployment using Streamlit Cloud

✅ User-friendly interface

---

## 🧬 Input Features

| Feature | Description |
|----------|------------|
| MolLogP | Lipophilicity of molecule |
| MolWt | Molecular Weight |
| NumRotatableBonds | Number of rotatable bonds |
| AromaticProportion | Fraction of aromatic atoms |

---

## 🤖 Machine Learning Model

### Algorithm Used
Random Forest Regressor

### Target Variable
logS (Aqueous Solubility)

### Libraries Used

- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Streamlit

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Random Forest Regression

### Web Framework
- Streamlit

### Data Processing
- Pandas
- NumPy

### Deployment
- GitHub
- Streamlit Cloud

---

## 📂 Project Structure

```text
Machine-Learning-Prediction-Mode/
│
├── app.py
├── solubility_model.pkl
├── requirements.txt
├── ML_MODEL.ipynb
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/pranavkoushik0606-code/Machine-Learning-Prediction-Mode.git
```

Move into project directory:

```bash
cd Machine-Learning-Prediction-Mode
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

### Home Page

- Project description
- Input feature details
- Molecular descriptor inputs
- Solubility prediction

---

## 🎯 Future Improvements

- SMILES molecule input
- Advanced molecular descriptors
- Multiple ML model comparison
- Prediction history
- Download prediction reports
- Dark mode support

---

## 👨‍💻 Author

**Pranav Koushik**

B.Tech Computer Science Engineering
