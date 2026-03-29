# 🚀 Breast Cancer Classification (Ensemble Methods Benchmark)

## 📌 Project Overview
This project represents the pinnacle of predictive modeling in this repository. It systematically evaluates and benchmarks **8 different Ensemble Learning algorithms** on the Breast Cancer Wisconsin dataset to identify the most robust and accurate classification model.

## 🧠 What is Ensemble Learning?
Instead of relying on a single algorithm (like one Decision Tree), Ensemble Learning combines the predictions of multiple machine learning models (weak learners) to reduce variance, minimize bias, and drastically improve overall predictive performance.

## 🛠️ Models Benchmarked
The codebase programmatically loops through, trains, and tests the following algorithms:
1. **Voting Classifiers:** Both `Hard Voting` and `Soft Voting` (combining Decision Tree, Logistic Regression, and SVC).
2. **Bagging & Pasting:** Using a Logistic Regression base estimator with and without bootstrap sampling.
3. **Random Forest:** An ensemble of randomized Decision Trees.
4. **Boosting Algorithms:** * `AdaBoost` (Adaptive Boosting)
   * `Gradient Boosting`
   * `XGBoost` (eXtreme Gradient Boosting - industry standard for tabular data).

## ⚙️ Engineering Decisions
* **Data Scaling:** `StandardScaler` was applied to the entire feature space. While Random Forest and Boosting trees do not require scaling, it is absolutely mandatory for the Logistic Regression and SVC models utilized within the Voting and Bagging architectures.
* **Target Encoding:** The `LabelEncoder` was explicitly used to transform the target variable to `0` and `1`, a strict requirement for the XGBoost architecture.

## 📈 Visualizations
The notebook concludes with a dynamic, sorted **Horizontal Bar Chart** (using Seaborn) that visually ranks the models based on their testing accuracy, allowing for an immediate, data-driven decision on which model to deploy in a production environment.