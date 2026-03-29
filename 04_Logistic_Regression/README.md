# 🚢 Titanic Survival Prediction (Logistic Regression)

## 📌 Project Overview
This project solves the famous Titanic survival problem using **Logistic Regression**, framing it as a binary classification task. The goal is to predict whether a passenger survived (1) or died (0) based on features like age, gender, passenger class, and ticket fare.

## 🧠 Smart Data Cleaning & Preprocessing
Unlike basic implementations that drop all rows with missing values (losing ~80% of data due to the `deck` column), this project takes a robust engineering approach:
* Dropped highly null or redundant columns (`deck`, `alive`, `class`, `embark_town`).
* Used a `ColumnTransformer` within a `Pipeline` to impute missing `age` values with the median.
* Applied `OneHotEncoder` for categorical variables (Gender, Embarked) and `StandardScaler` for numerical stability.

## 📊 Exploratory Data Analysis (EDA)
The notebook includes visualizations demonstrating the survival distributions. A key insight visualized is that female passengers had a significantly higher survival rate than males.

## 🚀 Model & Evaluation
A Logistic Regression classifier was trained within the pipeline. The evaluation focuses on comprehensive classification metrics rather than just accuracy:
* **Accuracy Score**
* **Precision, Recall, & F1-Score** (Classification Report)
* **Confusion Matrix:** Visualized via a Seaborn heatmap to clearly show True Positives, True Negatives, False Positives, and False Negatives.

## ⚙️ How to Run
1. Ensure `titanic_data.csv` is in the same directory.
2. Open `Titanic_Survival_Prediction.ipynb`.
3. Run all cells to see the automated cleaning, pipeline training, and final matrix visualization.