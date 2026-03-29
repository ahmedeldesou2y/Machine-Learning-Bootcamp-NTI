# 🌳 Breast Cancer Classification (Decision Tree)

## 📌 Project Overview
Following the SVM implementation, this project utilizes a **Decision Tree Classifier** on the Breast Cancer Wisconsin dataset. This provides a direct comparison between a "Black Box" mathematical model (SVM) and a highly interpretable, rule-based model (Decision Tree).

## 🧠 The "No-Scaling" Rule for Tree Models
A critical engineering decision in this pipeline is the **intentional omission of Feature Scaling** (e.g., `StandardScaler`). 
Unlike distance-based algorithms (KNN, SVM), Tree-based models partition data based on threshold conditions (e.g., `radius_mean <= 14.5`). These splits are mathematically scale-invariant, making standardization computationally redundant and unnecessary.

## 🛠️ Machine Learning Pipeline & Hyperparameters
* **Data Cleaning:** Removed `id` and empty `Unnamed: 32` columns to ensure data integrity.
* **Hyperparameter Tuning:** The `max_depth` parameter was constrained to `4`. Decision Trees are highly prone to **Overfitting** (memorizing the training data). Limiting the depth forces the model to learn generalized patterns rather than noise.
* **Model:** `DecisionTreeClassifier(criterion='gini')`.

## 📈 Visualizations & Interpretability
The strongest advantage of a Decision Tree is its interpretability (White-Box model). This project includes a large-scale, plotted visualization of the actual trained Decision Tree using `sklearn.tree.plot_tree`. 
This visualization allows healthcare professionals to trace the exact logical path (e.g., Node 1 checks concave points, Node 2 checks texture) the AI takes to classify a tumor as Benign or Malignant.

## ⚙️ How to Run
1. Ensure the `Cancer_Data (1).csv` dataset is present.
2. Open the `Breast_Cancer_Decision_Tree.ipynb` notebook.
3. Run all cells to evaluate the model and generate the visual Decision Tree plot.