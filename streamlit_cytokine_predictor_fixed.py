
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cytokine Potency Predictor (Fixed)", layout="centered")
st.title("🧬 Cytokine Fingerprint Potency Predictor (Corrected)")
st.markdown("Predict **Potency (%)** based on cytokine concentrations using the true underlying formula.")

# Sidebar inputs
st.sidebar.header("Cytokine Inputs (pg/mL)")
IL2 = st.sidebar.slider("IL-2 (pg/mL)", 100, 800, 400)
IFNg = st.sidebar.slider("IFN-γ (pg/mL)", 150, 1000, 500)
TNFa = st.sidebar.slider("TNF-α (pg/mL)", 50, 400, 200)
GMCSF = st.sidebar.slider("GM-CSF (pg/mL)", 30, 250, 100)

# True potency calculation based on known simulation formula
predicted_potency = (
    0.002 * IL2
    + 0.0015 * IFNg
    + 0.003 * TNFa
    + 0.0025 * GMCSF
)

predicted_potency = np.clip(predicted_potency, 20, 100)

# Output
st.subheader("📈 Predicted Potency")
st.metric(label="Predicted Potency (%)", value=f"{predicted_potency:.2f}")

# Optional: visualize cytokine contribution
st.subheader("📊 Cytokine Contributions")
cytokine_contributions = {
    "IL-2 Contribution": 0.002 * IL2,
    "IFN-γ Contribution": 0.0015 * IFNg,
    "TNF-α Contribution": 0.003 * TNFa,
    "GM-CSF Contribution": 0.0025 * GMCSF
}
fig, ax = plt.subplots()
ax.barh(list(cytokine_contributions.keys()), list(cytokine_contributions.values()))
ax.set_xlabel("Potency Contribution (%)")
ax.set_title("Individual Cytokine Contributions to Potency")
st.pyplot(fig)
