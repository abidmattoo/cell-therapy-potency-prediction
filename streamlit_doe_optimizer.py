
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="DOE Potency Optimizer", layout="centered")
st.title("🧬 DOE Potency Optimizer")
st.markdown("Predict **Potency (%)** based on CMC parameters: MOI, Culture Days, and Activation Marker (%)")

# Sidebar sliders
st.sidebar.header("Input CMC Parameters")
MOI = st.sidebar.slider("MOI", 2.0, 10.0, 5.0)
culture_days = st.sidebar.slider("Culture Days", 7, 14, 10)
activation_marker = st.sidebar.slider("Activation Marker (%)", 40.0, 90.0, 65.0)

# Predict potency using the DOE model (same formula used in simulation)
predicted_potency = (
    0.5 * MOI
    + 1.2 * culture_days
    + 0.8 * activation_marker
    - 0.05 * MOI * culture_days
    + 0.02 * culture_days * activation_marker
)

predicted_potency = np.clip(predicted_potency + np.random.normal(0, 5), 20, 150)  # add slight noise

# Display prediction
st.subheader("📈 Predicted Potency")
st.metric(label="Predicted Potency (%)", value=f"{predicted_potency:.2f}")

# Optimization Hint
st.info("🔍 Hint: Highest potency observed at MOI ~2, Culture Days ~14, Activation Marker ~90%.")
