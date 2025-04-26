
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(page_title="Parallel Line Bioassay Analyzer", layout="centered")
st.title("🧬 Parallel Line Bioassay Analyzer (Relative Potency Calculator)")

st.markdown("Upload bioassay data for Reference and Test samples to calculate **Relative Potency (RP)** using Parallel Line Analysis.")

uploaded_file = st.file_uploader("Upload CSV file with columns: E_T_Ratio, Killing(%), Sample", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Uploaded Data Preview")
    st.dataframe(df)

    # Plot data
    st.subheader("📈 Dose-Response Linear Plot")
    import seaborn as sns
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="E_T_Ratio", y="Killing(%)", hue="Sample", style="Sample", s=100)

    for sample_type, color in zip(["Reference", "Test"], ["blue", "orange"]):
        subset = df[df["Sample"] == sample_type]
        fit = np.polyfit(np.log10(subset["E_T_Ratio"]), subset["Killing(%)"], 1)
        fit_fn = np.poly1d(fit)
        x_vals = np.linspace(subset["E_T_Ratio"].min(), subset["E_T_Ratio"].max(), 100)
        plt.plot(x_vals, fit_fn(np.log10(x_vals)), label=f"{sample_type} Fit", linestyle="--", color=color)

    plt.xscale('log')
    plt.xlabel("E:T Ratio (log scale)")
    plt.ylabel("% Cytotoxicity / % Killing")
    plt.grid(True)
    plt.legend(title="Sample")
    st.pyplot(plt)

    # Fit lines
    ref_subset = df[df["Sample"] == "Reference"]
    test_subset = df[df["Sample"] == "Test"]
    ref_fit = np.polyfit(np.log10(ref_subset["E_T_Ratio"]), ref_subset["Killing(%)"], 1)
    test_fit = np.polyfit(np.log10(test_subset["E_T_Ratio"]), test_subset["Killing(%)"], 1)

    ref_slope, ref_intercept = ref_fit
    test_slope, test_intercept = test_fit

    # Calculate RP
    relative_potency = np.exp((test_intercept - ref_intercept) / ref_slope)

    st.subheader("📊 Calculated Parameters")
    st.write(f"Reference Slope: **{ref_slope:.2f}**")
    st.write(f"Reference Intercept: **{ref_intercept:.2f}**")
    st.write(f"Test Slope: **{test_slope:.2f}**")
    st.write(f"Test Intercept: **{test_intercept:.2f}**")
    st.write(f"**Relative Potency (RP): {relative_potency:.2f}**")

    # Optional: Check parallelism (simple slope difference)
    slope_difference = abs(ref_slope - test_slope)
    st.write(f"Slope Difference (abs): **{slope_difference:.2f}**")
