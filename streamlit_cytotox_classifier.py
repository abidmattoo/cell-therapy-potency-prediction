
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cytotoxicity Potency Classifier", layout="centered")
st.title("🧬 Cytotoxicity-Based Potency Classifier")
st.markdown("Predict whether a cell therapy batch will **pass cytotoxicity release criteria (70–130%)** using CMC parameters.")

# Sidebar sliders for input
st.sidebar.header("🧪 CMC Input Parameters")
passage = st.sidebar.slider("Passage Number", 1, 4, 2)
MOI = st.sidebar.slider("MOI", 2.0, 10.0, 5.0)
culture_days = st.sidebar.slider("Culture Days", 7, 14, 10)
transduction = st.sidebar.slider("Transduction Efficiency (%)", 30.0, 90.0, 60.0)
viability = st.sidebar.slider("Viability (%)", 75.0, 99.0, 90.0)
activation = st.sidebar.slider("Activation Marker (%)", 20.0, 95.0, 70.0)
donor_age = st.sidebar.slider("Donor Age", 20, 65, 40)

# Generate synthetic dataset and retrain model (same logic as notebook)
np.random.seed(303)
n_samples = 300
df = pd.DataFrame({
    "donor_age": np.random.randint(20, 65, n_samples),
    "passage_number": np.random.randint(1, 5, n_samples),
    "MOI": np.random.uniform(2, 10, n_samples),
    "culture_days": np.random.randint(7, 15, n_samples),
    "transduction_efficiency": np.random.uniform(30, 90, n_samples),
    "viability_percent": np.random.uniform(75, 99, n_samples),
    "activation_marker_percent": np.random.uniform(20, 95, n_samples)
})
noise = np.random.normal(0, 10, n_samples)
df["cytotoxicity_percent"] = (
    0.6 * df["transduction_efficiency"]
    + 0.4 * df["viability_percent"]
    + 0.2 * df["activation_marker_percent"]
    - 5.0 * df["passage_number"]
    + noise
).clip(20, 150)
df["release_pass"] = df["cytotoxicity_percent"].between(70, 130).astype(int)

# Train classifier
X = df.drop(columns=["cytotoxicity_percent", "release_pass"])
y = df["release_pass"]
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# User input prediction
input_df = pd.DataFrame([{
    "donor_age": donor_age,
    "passage_number": passage,
    "MOI": MOI,
    "culture_days": culture_days,
    "transduction_efficiency": transduction,
    "viability_percent": viability,
    "activation_marker_percent": activation
}])
pred = model.predict(input_df)[0]
prob = model.predict_proba(input_df)[0][1]

# Show result
st.subheader("🧾 Prediction Result")
if pred == 1:
    st.success(f"✅ PASS (Probability: {prob:.2f})")
else:
    st.error(f"❌ FAIL (Probability: {prob:.2f})")

# Feature importance
st.subheader("📊 Feature Importance")
importances = model.feature_importances_
features = input_df.columns
sorted_indices = np.argsort(importances)[::-1]

fig, ax = plt.subplots()
ax.barh(features[sorted_indices], importances[sorted_indices])
ax.set_xlabel("Importance Score")
ax.set_title("Random Forest Feature Importances")
ax.invert_yaxis()
st.pyplot(fig)
