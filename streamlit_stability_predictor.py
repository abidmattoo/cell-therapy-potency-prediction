
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stability Predictor", layout="centered")
st.title("🧬 Stability Predictor: Potency vs. Time")

st.markdown("Simulate how potency (%) degrades over time under different storage conditions.")

# Sidebar for input
st.sidebar.header("Storage Condition")
condition = st.sidebar.selectbox("Select Storage Condition", ["2-8C", "-20C", "-80C"])

# Stability parameters
k_values = {
    "2-8C": 0.10,
    "-20C": 0.04,
    "-80C": 0.01
}

# Time points
time_months = np.linspace(0, 18, 100)  # up to 18 months

# Calculate predicted potency
k = k_values[condition]
potency = 100 * np.exp(-k * time_months)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time_months, potency, label=f"Stability at {condition}", color="blue")
ax.axhline(70, color="red", linestyle="--", label="70% Release Threshold")
ax.set_xlabel("Time (Months)")
ax.set_ylabel("Potency (%)")
ax.set_title("Predicted Potency Over Time")
ax.grid(True)
ax.legend()

st.pyplot(fig)

# Shelf life estimation
shelf_life = np.interp(70, potency[::-1], time_months[::-1])
if shelf_life >= 18:
    st.success("✅ Shelf Life: >18 months (Potency remains above 70%)")
else:
    st.warning(f"⚠️ Estimated Shelf Life: {shelf_life:.1f} months")
