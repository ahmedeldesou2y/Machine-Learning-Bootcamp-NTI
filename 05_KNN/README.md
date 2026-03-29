# 🚢 Titanic Survival Prediction (K-Nearest Neighbors)

## 📌 Project Overview
Following the Logistic Regression implementation, this project tackles the Titanic survival classification problem using the **K-Nearest Neighbors (KNN)** algorithm. This allows for a comparative analysis of how different algorithms handle the same dataset.

## ⚠️ The Importance of Scaling in KNN
Unlike tree-based models, KNN is a distance-based algorithm (calculating the Euclidean distance between points). If features are on entirely different scales (e.g., `fare` ranging up to 500 while `age` is under 100), the features with larger scales will disproportionately influence the distance calculation.
* **Solution:** This project strictly embeds `StandardScaler` within the `scikit-learn` Pipeline to ensure all numerical features contribute equally to the distance metrics.

## 🛠️ Machine Learning Pipeline
* **Imputation:** Median for continuous values, Mode for categorical values.
* **Encoding:** `OneHotEncoder` for demographic and class data.
* **Scaling:** `StandardScaler` (Mandatory for KNN).
* **Classifier:** `KNeighborsClassifier`.

## 📈 Visualizations & Hyperparameter Tuning
Beyond the standard evaluation metrics (Accuracy, F1-Score, and Confusion Matrix), this notebook includes a programmatic approach to **Hyperparameter Tuning**. 
It features a custom visualization plotting the **Model Accuracy vs. K-Value**, dynamically iterating through values $K=1$ to $K=20$ to visually identify the optimal number of neighbors that yields the highest accuracy.

## ⚙️ How to Run
1. Ensure `titanic_data.csv` is in the same directory.
2. Open `Titanic_Survival_KNN_Classifier.ipynb`.
3. Run the cells to observe the pipeline execution, confusion matrix, and the optimal K-value graph.