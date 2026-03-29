# 🍦 Ice Cream Sales Forecasting (Polynomial Regression)

## 📌 Project Overview
This project applies **Polynomial Regression** to model the non-linear relationship between temperature and ice cream sales. In many real-world scenarios, a simple straight line (Linear Regression) is insufficient to capture the true trend of the data. By transforming the features into polynomial degrees, we allow the model to fit a curve, drastically improving prediction accuracy.

## 📈 The Business Problem
Ice cream sales do not increase linearly with temperature. They tend to plateau at very cold temperatures and spike exponentially during heatwaves. This project acts as a demand-forecasting tool to help businesses optimize inventory based on weather forecasts.

## 🛠️ Machine Learning Pipeline
The project utilizes a robust `scikit-learn` Pipeline containing:
1. **`StandardScaler`**: Scales the temperature data to ensure numerical stability.
2. **`PolynomialFeatures`**: Transforms the 1D temperature data into higher-dimensional polynomial features (e.g., $X, X^2$).
3. **`LinearRegression`**: Fits the transformed features to predict sales.

## 📊 Dataset
The dataset `Ice_cream selling data.csv` consists of two continuous variables:
* `Temperature (°C)` (Independent Variable)
* `Ice Cream Sales (units)` (Dependent/Target Variable)

## 💡 Key Results & Visualizations
The repository includes exploratory data analysis (EDA) and a final evaluation plot that superimposes the predicted polynomial curve (red line) over the actual data points (blue dots), visually demonstrating the model's accuracy and fitness.

## ⚙️ How to Run
1. Ensure the dataset `Ice_cream selling data.csv` is in the same directory.
2. Open the `Ice_Cream_Sales_Forecasting.ipynb` notebook.
3. Run the cells sequentially to observe the pipeline execution and the generated visualizations.