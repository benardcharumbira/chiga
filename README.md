---

# **Hybrid Metric Selection for Software Defect Prediction**
📌 **Repository for implementing and evaluating Software Defect Prediction models**  

This repository contains implementations of various **software defect prediction (SDP) models** using different **algorithm and dataset combinations**. The goal is to compare feature selection techniques, and analyze their effectiveness in improving defect prediction accuracy.

---

## **📊 Implemented Algorithms**
This repository includes various **feature selection techniques** for software defect prediction, ranging from **filter methods** (statistical-based) to **wrapper methods** (optimization-based).  

| **Algorithm** | **Type** | **Description** |
|--------------|--------------------------|----------------|
| **CHIGA (Chi-square Genetic Algorithm)** | Hybrid | A **hybrid metric selection technique** that combines a **filter method (Chi-square ranking)** with a **wrapper method (Genetic Algorithm)** for metric subset selection. CHIGA balances **statistical rigor** with **evolutionary optimization** to improve model generalizability. |
| **Chi-square (CS)** | Filter | Uses the **Chi-square statistic** to compute the independence between features and the target variable. Higher Chi-square values indicate stronger relationships, making the metric more important for defect prediction. |
| **Information Gain (IG)** | Filter | Evaluates the **entropy reduction** of each metric, determining how much information a feature provides about the target class. Higher values indicate **more informative metrics**. |
| **Genetic Algorithm for Subset Selection (GAS)** | Wrapper | Uses **Genetic Algorithms (GA)** to find an **optimal subset of features** by simulating natural selection through **selection, crossover, and mutation operators**. The fitness function evaluates the quality of each subset. |
| **Genetic Algorithm for Ranking (GAR)** | Wrapper | Similar to GAS but generates a **ranked list of metrics** instead of selecting a subset. It provides an ordered importance ranking of features based on evolutionary optimization. |
| **Particle Swarm Optimization (PSO)** | Wrapper | Inspired by **bird flocking and fish schooling behavior**, PSO finds an optimal metric subset by simulating a **swarm of candidate solutions** that iteratively improve through shared knowledge. It is **faster than GA** in high-dimensional feature spaces. |
| **Ant Colony Optimization (ACO)** | Wrapper | Models the **foraging behavior of ants**, where metrics are nodes in a graph, and pheromones help guide the search for optimal feature subsets. ACO is useful for balancing **exploration and exploitation** in feature selection. |
| **Heuristic Search (HS)** | Heuristic | Uses **forward selection, backward elimination, or stepwise selection** to iteratively **add or remove features** based on a predefined heuristic. Computationally more efficient than wrapper methods but may not always find the best subset. |
| **Exhaustive Search (ES)** | Exhaustive | Evaluates **all possible feature subsets** to find the optimal combination. **Guarantees optimal solutions** but is computationally **very expensive**, making it impractical for large datasets. |

---

## **📊 How these methods improve software defect prediction**
- **Filter methods** (CS, IG) are computationally **fast** and effective for **removing irrelevant features**.
- **Wrapper methods** (GAS, GAR, PSO, ACO) adaptively **search for the best feature subset**, improving model **performance but at a higher computational cost**.
- **Heuristic and exhaustive search** provide different trade-offs between **efficiency and accuracy**.

🚀 These techniques help **reduce dataset dimensionality** and improve **defect prediction accuracy**.

## **📊 Datasets**
The repository includes **benchmark datasets** commonly used in **Software Defect Prediction (SDP)**:

| Dataset | Source | Instances | Metrics |
|---------|--------|----------|---------|
| **CM1** | NASA | 498 | 21 |
| **JM1** | NASA | 10,885 | 21 |
| **KC1** | NASA | 2,109 | 21 |
| **Eclipse** | Open-source | 997 | 198 |
| **Equinox** | Open-source | 324 | 198 |

All datasets are stored in **CSV format**

---

## **📈 Evaluation Metrics**
All models are evaluated using the following performance metrics:
- **AUC (Area Under Curve)** – Measures classification performance.
- **Precision, Recall, and F1-Score** – Evaluate prediction accuracy.
- **ANOVA Significance Testing** – Measures statistical differences.

---

### **Running Jupyter Notebooks**
For interactive analysis, run:

```sh
jupyter notebook
```
Then open the notebooks in the **`notebooks/`** folder.

---

## **💡 Acknowledgments**
This repository is inspired by research in **software defect prediction** and leverages **NASA datasets and open-source software quality metrics**.

---
