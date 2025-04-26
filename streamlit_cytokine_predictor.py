
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Cytokine Potency Predictor", layout="centered")
st.title("🧬 Cytokine Fingerprint Potency Predictor")
st.markdown("Predict **Potency (%)** based on input cytokine concentrations.")

# Sidebar inputs
st.sidebar.header("Cytokine Inputs (pg/mL)")
IL2 = st.sidebar.slider("IL-2 (pg/mL)", 100, 800, 400)
IFNg = st.sidebar.slider("IFN-γ (pg/mL)", 150, 1000, 500)
TNFa = st.sidebar.slider("TNF-α (pg/mL)", 50, 400, 200)
GMCSF = st.sidebar.slider("GM-CSF (pg/mL)", 30, 250, 100)

# Synthetic model re-training (since Streamlit is stateless)
np.random.seed(456)
n_samples = 300
df_cytokines = pd.DataFrame({
    "IL2_pg_ml": np.random.uniform(100, 800, n_samples),
    "IFNg_pg_ml": np.random.uniform(150, 1000, n_samples),
    "TNFa_pg_ml": np.random.uniform(50, 400, n_samples),
    "GMCSF_pg_ml": np.random.uniform(30, 250, n_samples)
})
noise = np.random.normal(0, 5, n_samples)
df_cytokines["Potency(%)"] = (
    0.002 * df_cytokines["IL2_pg_ml"]
    + 0.0015 * df_cytokines["IFNg_pg_ml"]
    + 0.003 * df_cytokines["TNFa_pg_ml"]
    + 0.0025 * df_cytokines["GMCSF_pg_ml"]
    + noise
).clip(20, 100)

X = df_cytokines.drop(columns=["Potency(%)"])
y = df_cytokines["Potency(%)"]
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict based on user input
input_df = pd.DataFrame([{
    "IL2_pg_ml": IL2,
    "IFNg_pg_ml": IFNg,
    "TNFa_pg_ml": TNFa,
    "GMCSF_pg_ml": GMCSF
}])

predicted_potency = model.predict(input_df)[0]

# Output
st.subheader("📈 Predicted Potency")
st.metric(label="Predicted Potency (%)", value=f"{predicted_potency:.2f}")
