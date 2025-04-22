# Cell Therapy Potency Prediction using Machine Learning

This project simulates critical quality attributes (CQAs) for a cell therapy product and trains a machine learning model to predict **potency (%)** using Random Forest regression. The notebook includes SHAP explainability to visualize the contribution of input parameters to each prediction.

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

Then open `Potency_Model_Abid.ipynb` and run the notebook.

## 👤 Author

Abid Mattoo  
Biotech scientist exploring ML in analytical development and CMC strategy.
