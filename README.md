Welcome to Heart Disease project 


# Overview

This project predicts the likelihood of heart disease in patients using the **UCI Heart Disease Dataset**.
It involves **data preprocessing, feature engineering, supervised/unsupervised learning, hyperparameter tuning, and deployment** with a **Streamlit web app**.

---

## 📂 Project Structure

```
Heart_Disease_Project/
│── data/
│   └── heart_disease.csv
│
│── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_pca_analysis.ipynb
│   ├── 03_feature_selection.ipynb
│   ├── 04_supervised_learning.ipynb
│   ├── 05_unsupervised_learning.ipynb
│   └── 06_hyperparameter_tuning.ipynb
│
│── models/
│   └── final_model.pkl
│
│── ui/
│   └── app.py
│
│── deployment/
│   └── ngrok_setup.txt
│
│── results/
│   └── evaluation_metrics.txt
│
│── README.md
│── requirements.txt
│── .gitignore
```

---

## ⚙️ Installation

1. **Clone this repository**

```bash
git clone https://github.com/Salma281/Heart-Disease-project.git
cd Heart-Disease-project
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### 1. Jupyter Notebooks

Each notebook in `notebooks/` covers a project stage:

* Data preprocessing & cleaning
* PCA (dimensionality reduction)
* Feature selection
* Supervised learning (Logistic Regression, Decision Tree, Random Forest, SVM)
* Unsupervised learning (K-Means, Hierarchical)
* Hyperparameter tuning

Run them in order to reproduce results.

---

### 2. Run the Streamlit Web App

Inside the `ui/` folder, run:

```bash
streamlit run app.py
```

Then open the link shown in the terminal (`http://localhost:8501`).

---

## 🌍 Deployment with Ngrok (Optional)

If you want to share your app publicly:

1. Install **Ngrok** from [ngrok.com](https://ngrok.com).
2. Start your Streamlit app locally.
3. In a new terminal, run:

```bash
ngrok http 8501
```

Ngrok will generate a **public URL** you can share.

---

## 📊 Features Considered

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Serum Cholesterol
* Fasting Blood Sugar
* Resting ECG Results
* Max Heart Rate Achieved
* Exercise Induced Angina
* ST Depression (Oldpeak)
* Slope of ST Segment
* Number of Major Vessels (ca)
* Thal (Normal / Fixed / Reversible defect)

---

## ✅ Deliverables

✔ Cleaned dataset for modeling
✔ PCA-transformed dataset and visualizations
✔ Feature importance rankings
✔ Trained classification & clustering models
✔ Optimized final model (`final_model.pkl`)
✔ Interactive **Streamlit app** for predictions
✔ Ngrok setup for deployment
✔ Documentation (this README)

---

## 🧑‍💻 Author

👩 Salma Elanany

---

👉 This README is **ready to copy-paste** into your `README.md` file.

Do you also want me to write the **requirements.txt** content for you so it’s fully prepared for GitHub upload?
