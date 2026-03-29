## 🚀 Professional Data Preprocessing Pipeline

In real-world Machine Learning projects, writing sequential preprocessing steps can lead to **Data Leakage** and messy code. The industry standard approach is to use `scikit-learn`'s **Pipelines** and **ColumnTransformers**.

### Why use this approach?
1. **Prevents Data Leakage:** Ensures that parameters like scaling metrics (mean, variance) are learned *only* from the training set and applied consistently to the test set.
2. **Reproducibility:** Bundles all preprocessing steps into a single object, making it incredibly easy to process new, unseen data in production.
3. **Clean Code:** Replaces multiple `for` loops and scattered transformations with a highly readable and modular architecture.

Below is a universal template. You can adjust the `strategy` in the imputers or the type of scaler/encoder based on your specific dataset requirements.


# 1. Import Essential Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# ==========================================
# 2. Load Your Dataset (Example)
# df = pd.read_csv('your_dataset.csv')
# df.drop_duplicates(inplace=True) # Basic cleaning step
# ==========================================

# 3. Separate Features (X) and Target (y)
# Replace 'target_column' with your actual target variable name
# X = df.drop('target_column', axis=1)
# y = df['target_column']

# 4. Automatically identify Numerical and Categorical columns
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = X.select_dtypes(include=['object', 'category']).columns

print(f"Numerical Columns: {list(numerical_cols)}")
print(f"Categorical Columns: {list(categorical_cols)}")

# 5. Define Preprocessing Steps (Pipelines)

# A. Numerical Data Pipeline: 
#    - Impute missing values using the mean (can be changed to 'median')
#    - Scale data to have a mean of 0 and variance of 1
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# B. Categorical Data Pipeline:
#    - Impute missing values using the most frequent value (mode)
#    - Apply One-Hot Encoding (ignoring unknown categories in future data)
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# 6. Combine Pipelines into a ColumnTransformer
# This allows applying specific transformations to specific columns simultaneously
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# 7. Split the Data into Training and Testing Sets (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Execute the Preprocessing Pipeline
# CRITICAL: We only use fit_transform on the TRAINING data to avoid data leakage
X_train_processed = preprocessor.fit_transform(X_train)

# We use transform ONLY on the TESTING data
X_test_processed = preprocessor.transform(X_test)

print("✅ Professional Data Preprocessing Pipeline Executed Successfully!")
