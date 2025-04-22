
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import shap
import matplotlib.pyplot as plt

st.set_page_config(page_title="Potency Predictor", layout="centered")
st.title("🔬 Cell Therapy Potency Predictor")
st.markdown("Use the sliders to input CMC parameters and predict **potency (%)** of the product.")

# Sidebar inputs
st.sidebar.header("Input Parameters")
passage_number = st.sidebar.slider("Passage Number", 1, 4, 2)
MOI = st.sidebar.slider("MOI", 2.0, 10.0, 5.0)
culture_days = st.sidebar.slider("Culture Days", 7, 14, 10)
transduction_eff = st.sidebar.slider("Transduction Efficiency (%)", 30.0, 90.0, 60.0)
viability = st.sidebar.slider("Viability (%)", 75.0, 99.0, 90.0)
activation_marker = st.sidebar.slider("Activation Marker (%)", 20.0, 95.0, 70.0)
IL2 = st.sidebar.slider("IL-2 Expression (pg/mL)", 50.0, 1200.0, 500.0)
IFNg = st.sidebar.slider("IFN-γ Expression (pg/mL)", 50.0, 1400.0, 600.0)
donor_age = st.sidebar.slider("Donor Age", 20, 65, 40)

# Simulate training data (same as your model)
np.random.seed(101)
n_samples = 300
train_df = pd.DataFrame({
    "donor_age": np.random.randint(20, 65, n_samples),
    "passage_number": np.random.randint(1, 5, n_samples),
    "MOI": np.random.uniform(2, 10, n_samples),
    "culture_days": np.random.randint(7, 15, n_samples),
    "transduction_efficiency": np.random.uniform(30, 90, n_samples),
    "viability_percent": np.random.uniform(75, 99, n_samples),
    "activation_marker_percent": np.random.uniform(20, 95, n_samples),
    "IL2_expression": np.random.uniform(50, 1200, n_samples),
    "IFNg_expression": np.random.uniform(50, 1400, n_samples)
})
noise = np.random.normal(0, 5, n_samples)
train_df["potency_percent"] = (
    0.015 * train_df["IL2_expression"]
    + 0.01 * train_df["IFNg_expression"]
    + 0.15 * train_df["activation_marker_percent"]
    + 0.08 * train_df["transduction_efficiency"]
    + 0.08 * train_df["viability_percent"]
    - 6.0 * train_df["passage_number"]
    + noise
).clip(20, 100)

# Train model
X_train = train_df.drop(columns=["potency_percent"])
y_train = train_df["potency_percent"]
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Input for prediction
input_data = pd.DataFrame([{
    "donor_age": donor_age,
    "passage_number": passage_number,
    "MOI": MOI,
    "culture_days": culture_days,
    "transduction_efficiency": transduction_eff,
    "viability_percent": viability,
    "activation_marker_percent": activation_marker,
    "IL2_expression": IL2,
    "IFNg_expression": IFNg,
}])

# Prediction
predicted_potency = model.predict(input_data)[0]

# Output
st.subheader("📈 Predicted Potency")
st.metric("Potency (%)", f"{predicted_potency:.2f}")

# SHAP explainability
with st.expander("🧠 Feature Contributions (SHAP)", expanded=False):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_data)

    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write("SHAP Summary (single prediction):")
    shap.initjs()
    shap.force_plot(explainer.expected_value, shap_values[0], input_data.iloc[0], matplotlib=True, show=False)
    st.pyplot(bbox_inches='tight', dpi=300, pad_inches=0.1)
