# 📂 Dataset Overview  

This directory contains the datasets used for the **SemEval-2025 Task 9: Food Hazard Detection Challenge**. The dataset consists of **food recall notifications**, which include structured and unstructured text fields. The goal is to classify food hazards and extract exact hazard/product mentions.



## 📌 Dataset Files  

| File Name         | Description |
|------------------|-------------|
| `train.csv`      | **Preprocessed training dataset** used for model training. |
| `validation.csv` | **Validation dataset** (not preprocessed). |
| `test.csv`       | **Test dataset** (not preprocessed, used for final evaluation). |



## 📝 Data Format  

Each CSV file contains the following columns:

| Column Name  | Description |
|-------------|-------------|
| `title`     | Title of the food recall notification. |
| `text`      | Full description of the recall, including the product name, reason for recall, and manufacturer details. |
| `product-category` | Category of the food product (e.g., Dairy, Meat, Beverages). *(Used in ST1 - Classification)* |
| `hazard-category`  | Type of hazard detected (e.g., Biological, Chemical, Physical). *(Used in ST1 - Classification)* |
| `product`   | Extracted product name as a structured vector. *(Used in ST2 - Extraction)* |
| `hazard`    | Extracted hazard reason as a structured vector. *(Used in ST2 - Extraction)* |



## 🔄 Data Preprocessing  

### **Preprocessed (train.csv)**  
The `train.csv` file has undergone **cleaning and normalization**, including:
- **HTML tag removal** from scraped web data.
- **Whitespace standardization** to ensure proper formatting.
- **Newline character removal** for continuous text flow.
- **Concatenation of `title` and `text` fields** to capture complete context.

### **Raw (validation.csv & test.csv)**  
- These files **have not been preprocessed** and contain raw text with potential noise.
- Apply the preprocessing steps from `train.csv` before using them for model evaluation.

## 🔗 References
- [SemEval-2025 Task 9: Food Hazard Detection Challenge](https://food-hazard-detection-semeval-2025.github.io/)
- Dataset derived from [CICLe: Conformal In-Context Learning for Largescale Multi-Class Food Risk Classification](https://aclanthology.org/2024.findings-acl.459/) (Randl et al., Findings 2024)
---

