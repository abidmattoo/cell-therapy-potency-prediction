# 🧬 Cell Therapy Potency Predictor

🚀 **Live App**: [Launch on Streamlit](https://cell-therapy-potency-prediction-cbb45woazyamu7wbrzw6uw.streamlit.app/)

This dashboard predicts **potency (%)** of a cell therapy product based on assay and manufacturing process parameters.  
Built using `RandomForestRegressor` + `SHAP` for explainability, and deployed on **Streamlit Cloud**.

---

## 🔍 Features

- Input sliders for key CMC parameters (MOI, IL-2, viability, etc.)
- Real-time potency prediction
- SHAP-based interpretability of feature contributions
- Fully interactive and publicly accessible

---

## 📁 Files

- `streamlit_potency_app.py` – Main Streamlit app
- `requirements.txt` – Python dependencies

---

## 🛠 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_potency_app.py


## 📊 Project Overview

Cell and gene therapy products rely on consistent analytical metrics to ensure therapeutic efficacy. This project demonstrates:

- Simulation of high-variance CMC analytical data
- Training of a Random Forest model to predict potency
- Evaluation via MAE and R² scores
- SHAP analysis for model interpretability

## 🔬 Simulated Parameters

- Donor Age
- Passage Number
- MOI
- Culture Days
- Transduction Efficiency (%)
- Viability (%)
- Activation Marker (%)
- IL-2 Expression (pg/mL)
- IFN-γ Expression (pg/mL)

## ✅ Key Tools Used

- `scikit-learn`
- `matplotlib`
- `pandas`
- `shap`
- `jupyter`

## 🧠 Model Output

- MAE: ~2.0%
- R²: ~0.71
- SHAP summary plots explain which features influence each prediction

## 📁 How to Run

```bash
git clone https://github.com/YOUR_USERNAME/cell-therapy-potency-prediction.git
cd cell-therapy-potency-prediction
pip install -r requirements.txt
jupyter notebook
```
---

🆕 Cytotoxicity-Based Potency Classifier (70–130%)

📄 Notebook: Cytotoxicity_Potency_Classifier.ipynb

This notebook simulates a cytotoxicity-based potency assay (e.g., One-Titer Glo) and classifies whether a batch **passes release criteria** (70–130%) based on key CMC inputs:

- Transduction efficiency
- Viability
- Activation marker expression
- Passage number

---

### 📈 Key Features:
- ✅ Binary classification model (**RandomForestClassifier**)
- 📊 Confusion matrix, ROC curve, and model accuracy
- 🔍 Feature importance analysis (feature importance ranking)

---

### 🚀 How to Use:
- Open the notebook: **Cytotoxicity_Potency_Classifier.ipynb** (or your correct filename)
- Execute all cells to simulate data, train the model, and evaluate potency classification.

---

### 🌐 Launch the Web App:
[👉 Click here to open the Cytotoxicity Potency Classifier (Streamlit App)](https://cytotoxicitypotencyclassifieripynb-hz9tt3cfnucrqcmzjf2nqu.streamlit.app/)

(Upload your CMC attributes and predict batch pass/fail based on 70–130% potency release range.)

---


## ⚙️ Streamlit App: DOE Potency Optimizer

Predict **potency (%)** based on:
- MOI
- Culture Days
- Activation Marker %

▶️ [Launch DOE Optimizer](https://cell-therapy-potency-prediction-7m3d9uyefc5zhaqwrby3ss.streamlit.app/)

---

## ❄️ Streamlit App: Stability Predictor

Simulate **potency degradation over time** under different storage conditions (2–8°C, –20°C, –80°C).  
Predict estimated shelf-life based on potency staying above 70%.

▶️ [Launch Stability Predictor](https://cell-therapy-potency-prediction-dfo2sylfcffjx9nbu6edd4.streamlit.app/)

Includes:
- ✅ Stability curve plotting
- 📉 Shelf life estimation
- 📈 Interactive temperature-based modeling

---

## 🧫 Streamlit App: Cytokine Fingerprint Potency Predictor

Predict **Potency (%)** based on simulated cytokine fingerprint (IL-2, IFN-γ, TNF-α, GM-CSF).

▶️ [Launch Cytokine Fingerprint Potency Predictor](https://cell-therapy-potency-prediction-g7vcej4k4lmvoqbqkde8vt.streamlit.app/))

Includes:
- ✅ True formula-based potency prediction
- 📈 Dynamic cytokine contribution visualization
- 🔍 Input IL-2, IFN-γ, TNF-α, GM-CSF and predict potency interactively
---

## 🧬 Parallel Line Bioassay Analyzer (Streamlit App)
st.markdown("""
### 🧪 How to Use This App

1. 📂 Prepare a CSV file with **three columns**:
   - `E_T_Ratio` (Effector:Target ratio, like 1, 2, 5, 10)
   - `Killing(%)` (% cytotoxicity or % cell killing)
   - `Sample` (Reference or Test)

2. 📈 Upload your CSV file using the uploader below.

3. 📊 View fitted parallel lines, calculated Relative Potency (RP), and download your analysis.

---

🔽 **Don't have a CSV?**  
[Download a Sample CSV file here](https://raw.githubusercontent.com/abidmattoo/cell-therapy-potency-prediction/main/sample_parallel_line_data.csv)
""")


Analyze **Reference vs Test bioassay data** using Parallel Line Analysis (PLA) and calculate **Relative Potency (RP)**.

### 📈 Features:
- Upload experimental CSV data (E:T Ratio, % Killing, Sample)
- Visualize dose-response curves (log-scale E:T ratio)
- Fit separate parallel lines for Reference and Test
- Calculate slopes, intercepts, and **Relative Potency (RP)**
- Check slope difference to assess parallelism
- Download analysis results as a CSV file

### 📂 How to Use:
- Prepare a CSV file with columns: `E_T_Ratio`, `Killing(%)`, `Sample`
- Upload it in the Streamlit app
- View fitted plots and calculated parameters
- Download your results easily

### 🚀 Launch the App:
[Open Parallel Line Bioassay Analyzer](https://cell-therapy-potency-app-eavqd49wfhzjw9euxnw2n5.streamlit.app/)

---


## 👤 Author

Abid Mattoo  
Biotech scientist exploring ML in analytical development and CMC strategy.
