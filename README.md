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

## 🆕 Cytotoxicity-Based Potency Classifier (70–130%)

📄 [Cytotoxicity_Potency_Classifier.ipynb](./Cytotoxicity_Potency_Classifier.ipynb)

This notebook simulates a **cytotoxicity-based potency assay** (e.g., One-Titer Glo) and classifies whether a batch **passes release criteria** (70–130%) based on CMC inputs like:

- Transduction efficiency
- Viability
- Activation marker expression
- Passage number

Includes:
- ✅ Binary classification model (`RandomForestClassifier`)
- 📊 Confusion matrix, ROC curve, accuracy
- 🔍 Feature importance analysis

Then open `Potency_Model_Abid.ipynb` and run the notebook.
---

## 🌐 Streamlit App: Cytotoxicity Classifier

🧬 Predict whether a cell therapy batch passes cytotoxicity-based release criteria (70–130%) using Random Forest.

▶️ [Launch Cytotoxicity Classifier on Streamlit](https://cytotoxicitypotencyclassifieripynb-hz9tt3cfnucrqcmzjf2nqu.streamlit.app/))

Includes:
- ✅ Binary classification (`RandomForestClassifier`)
- 📊 Confusion matrix, ROC curve, accuracy
- 📈 Feature importance bar plot

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
seaborn

## 👤 Author

Abid Mattoo  
Biotech scientist exploring ML in analytical development and CMC strategy.
