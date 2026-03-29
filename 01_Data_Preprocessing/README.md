# 🛠️ Data Preprocessing Pipeline & Reference Guide

## 📌 Overview
This repository contains a comprehensive guide and a structured pipeline for Data Preprocessing. It serves as a foundational reference for preparing raw data before feeding it into any Machine Learning model. The code provides essential templates and techniques required to clean, transform, and split datasets efficiently.

## 🚀 Key Techniques Covered
This guide encompasses the following critical preprocessing steps:

1. **Data Cleaning:**
   - Handling missing values.
   - Removing duplicate records.
   - Outlier detection and handling using the IQR (Interquartile Range) method.
2. **Feature Separation:**
   - Isolating the target variable (`y`) from features (`X`).
   - Automatically distinguishing between Quantitative (Numerical) and Categorical features.
3. **Data Transformation (Encoding):**
   - **Label Encoding** for ordinal data.
   - **One-Hot Encoding** for nominal data.
4. **Feature Scaling:**
   - **Normalization** (MinMaxScaler).
   - **Standardization** (StandardScaler).
5. **Feature Engineering & Dimensionality Reduction:**
   - Correlation matrix analysis using Seaborn heatmaps.
   - **PCA (Principal Component Analysis)** for reducing dimensionality.
6. **Data Splitting:**
   - Splitting the dataset into training and testing sets using `train_test_split`.

## 🛠️ Libraries Used
- `pandas`: Data manipulation and analysis.
- `scikit-learn`: Preprocessing, PCA, and data splitting.
- `seaborn` & `matplotlib`: Data visualization (Correlation heatmaps).

## 💡 How to Use
You can use this notebook as a template for your own Machine Learning projects. Simply load your dataset and apply the relevant cells to clean and prepare your data for modeling.
