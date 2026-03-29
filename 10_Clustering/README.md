# 🎯 Customer Segmentation (Unsupervised Learning)

## 📌 Project Overview
This final project transitions from supervised predictive modeling to **Unsupervised Learning**. The objective is to perform Customer Segmentation on retail data, grouping customers into distinct marketing personas based on their purchasing habits (Annual Income and Spending Score) without any pre-labeled target variable.

## 🛠️ Algorithms Used
1. **K-Means Clustering:** A partition-based algorithm that divides the dataset into $K$ distinct, non-overlapping clusters.
2. **Agglomerative Hierarchical Clustering:** A bottom-up approach that recursively merges pairs of clusters to build a hierarchy.

## ⚙️ Engineering Decisions & Best Practices
* **Feature Selection:** Filtered the dataset to focus purely on continuous behavioral metrics (`Annual Income` and `Spending Score`), dropping IDs and categorical noise to ensure clear multidimensional distance calculations.
* **Feature Scaling:** Since clustering relies heavily on Euclidean distance, `StandardScaler` was applied. Without this, the `Annual Income` (in tens of thousands) would completely dominate the `Spending Score` (1-100), leading to biased and incorrect clusters.
* **Optimal 'K' Selection:** Implemented the **Elbow Method** (plotting WCSS/Inertia against $K$ values) to mathematically justify the selection of $K=5$ clusters.

## 📈 Visualizations & Business Value
The notebook includes detailed scatter plots visually separating the 5 customer segments (e.g., High Income/High Spend, Low Income/Low Spend, Target Customers). These exact visualizations are used by marketing teams to tailor ad campaigns and optimize customer retention strategies.

## 🚀 How to Run
1. Ensure `Customers (1).csv` is in the same directory.
2. Open `Customer_Segmentation_Clustering.ipynb`.
3. Run all cells to view the Elbow Curve and the final plotted Customer Segments.