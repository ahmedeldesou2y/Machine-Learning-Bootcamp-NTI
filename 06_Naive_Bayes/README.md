# 🩺 Diabetes Prediction (Gaussian Naive Bayes)

## 📌 Project Overview
This project focuses on predicting the likelihood of a patient having diabetes based on a large dataset (approx. 100,000 records). We leverage the **Gaussian Naive Bayes** algorithm, a probabilistic classifier based on applying Bayes' theorem with strong (naive) independence assumptions between the features. 

## 🧠 Medical Data Handling
The dataset contains critical health indicators like Blood Glucose Levels, HbA1c, and BMI. To ensure model robustness:
* **Outlier Removal:** Biologically improbable extreme BMI values were filtered out using the Interquartile Range (IQR) method.
* **Feature Pruning:** The free-text `clinical_notes` column was removed to focus purely on structured numerical and categorical data, as NLP techniques are outside the scope of this specific predictive model.

## 🛠️ Machine Learning Pipeline
An automated `scikit-learn` Pipeline was constructed:
* **Categorical Encoding:** `OneHotEncoder` for demographic data (Gender, Location, Smoking History).
* **Numerical Scaling:** `StandardScaler` to ensure all biological metrics are on a stable scale for the Gaussian distribution assumption.
* **Model:** `GaussianNB` from `sklearn.naive_bayes`.

## 📈 Visualizations
* **Exploratory Data Analysis (EDA):** A scatter plot illustrating the clear clustering of diabetic patients at higher intersections of Blood Glucose and HbA1c levels.
* **Confusion Matrix:** Evaluates the classification performance, highlighting the model's ability to correctly identify True Positives (actual diabetic patients).

## ⚙️ How to Run
1. Ensure the dataset `diabetes_dataset_with_notes (1).csv` is present.
2. Open `Diabetes_Prediction_NaiveBayes.ipynb`.
3. Execute all cells to run the pipeline, view the EDA, and analyze the model's diagnostic accuracy.