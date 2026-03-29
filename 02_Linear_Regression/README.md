# 🚗 Car Price Prediction using Linear Regression

## 📌 Project Overview
This mini-project demonstrates the application of **Multiple Linear Regression** to solve a real-world business problem: estimating the market value of an automobile based on its technical specifications (e.g., horsepower, engine size, body style, miles-per-gallon). 

## 🛠️ Machine Learning Pipeline
Instead of manual sequential processing, this project employs an end-to-end `scikit-learn` Pipeline ensuring code modularity and preventing Data Leakage. The pipeline includes:
1. **Target Variable Handling:** Removing records with missing prices.
2. **Data Imputation:** Handling missing numerical data (Median) and categorical data (Mode).
3. **Feature Scaling:** Standardization using `StandardScaler`.
4. **Encoding:** Transforming text/categorical variables via `OneHotEncoder`.
5. **Modeling:** Training a Multiple `LinearRegression` model.

## 📊 Dataset
The dataset `imports.csv` contains multiple attributes of cars, encompassing both physical dimensions, engine specifications, and fuel economy.

## 📈 Evaluation Metrics Used
* **Mean Absolute Error (MAE):** Average error in dollar amount.
* **Root Mean Squared Error (RMSE):** Penalizes larger errors heavily.
* **R-squared ($R^2$):** Measures the proportion of the variance in the car price that is predictable from the vehicle features.

## ⚙️ How to Run
1. Ensure the `imports.csv` dataset is in the same directory.
2. Open the `Car_Price_Prediction_Model.ipynb` notebook.
3. Run all cells sequentially.