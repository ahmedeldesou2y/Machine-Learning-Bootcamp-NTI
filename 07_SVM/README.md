# 🎗️ Breast Cancer Classification (Support Vector Machines)

## 📌 Project Overview
This project applies a **Support Vector Machine (SVM)** classifier to the well-known Breast Cancer Wisconsin dataset. The objective is to accurately classify tumor nuclei as either **Malignant (M)** or **Benign (B)** based on 30 computed geometric features (e.g., radius, texture, perimeter).

## ⚠️ The Necessity of Feature Scaling
SVM is a mathematical optimization algorithm that attempts to find the optimal hyperplane maximizing the margin between classes in a high-dimensional space. Because it computes distances between data points, **Feature Scaling is mandatory**.
* **Solution:** A `scikit-learn` Pipeline was implemented with `StandardScaler` to ensure all 30 features have a mean of 0 and a variance of 1, preventing features with large numerical ranges (like `area`) from overshadowing smaller ones (like `smoothness`).

## 🛠️ Data Preprocessing & Pipeline
* **Data Cleaning:** Removed the irrelevant `id` column and an empty `Unnamed: 32` artifact column to prevent noise.
* **Target Encoding:** Utilized `LabelEncoder` to convert 'B' and 'M' into 0 and 1, respectively.
* **Pipeline:** Sequentially integrated `StandardScaler` and `SVC(kernel='linear')`.

## 📈 Evaluation & Clinical Relevance
In medical diagnostics, minimizing False Negatives (predicting a tumor is benign when it is actually malignant) is critical. The evaluation includes:
1. **Confusion Matrix:** To visually inspect the count of True Positives, True Negatives, False Positives, and False Negatives.
2. **Classification Report:** Detailing Precision, Recall, and F1-scores.
3. **ROC Curve (Receiver Operating Characteristic):** Plotted to visualize the trade-off between the True Positive Rate and False Positive Rate, calculating the Area Under the Curve (AUC) to quantify the model's diagnostic ability.

## ⚙️ How to Run
1. Ensure the `Cancer_Data (1).csv` dataset is present.
2. Open the `Breast_Cancer_Classification_SVM.ipynb` notebook.
3. Run the cells sequentially to observe the pipeline execution and the generation of clinical evaluation plots.