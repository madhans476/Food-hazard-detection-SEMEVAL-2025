# Food Hazard Detection - SemEval 2025 Task 9  

## 📌 Project Overview  
This repository contains our solution for **SemEval-2025 Task 9: The Food Hazard Detection Challenge**, which aims to **automate food hazard classification and extraction** from recall notifications.  

The project consists of **two subtasks**:  
1. **Task 1 (Classification)**: Predicts the **hazard category** (e.g., Biological, Chemical) and **product category** (e.g., Dairy, Meat).  
2. **Task 2 (Detection)**: Extracts the **exact hazard reason** and **product name** from recall text.  

We employ **machine learning, fine-tuned LLMs (GPT-2, LLaMA, Flan-T5-XL), and ensemble learning** to solve these challenges.  

## Project Structure
```plaintext
Food-Hazard-Detection-SemEval-2025/ 
│── Datasets/                     # Dataset storage (train, validation, test) 
│   │── train.csv                 # Preprocessed training data 
│   │── validation.csv            # Raw validation dataset 
│   │── test.csv                  # Raw test dataset 
│   │── README.md                 # Dataset details and preprocessing steps 
│── Task 1/                       # Task 1: Hazard & Product Category Classification 
│   │── TF-IDF_XGBoost.ipynb      # Train and evaluate TF-IDF + XGBoost model 
│   │── peft_GPT2.ipynb           # Fine-tune GPT-2 Large using PEFT 
│   │── peft_llama.ipynb          # Fine-tune LLaMA 3.1 1B using PEFT 
│   │── ensemble.py               # Combine models using a voting ensemble 
│   │── README.md                 # Task 1 details 
│── Task 2/                       # Task 2: Hazard & Product Extraction 
│   │── prompt_based_peft.ipynb   # Fine-tune Flan-T5-XL for extraction 
│   │── README.md                 # Task 2 details 
│── LICENSE                       # License information 
│── README.md                     # Main project documentation 
│── requirements.txt              # Python dependencies 
│── .gitignore                    # Ignore unnecessary files
```

## 📂 Dataset Details  
- **Source**: The dataset contains food recall notifications scraped from regulatory sources.  
- **Language**: English.  
- **Size**: ~7,546 recall notices.  
- **Labels**:  
  - **Hazard Categories**: 10 classes (e.g., Biological, Chemical, Physical).  
  - **Product Categories**: 22 classes (e.g., Beverages, Dairy, Meat).  

📌 **More details**: See [`Datasets/README.md`](Datasets/readme.md).  


## ⚙️ Methodology  

### **🛠 Task 1: Hazard & Product Category Classification**  
🔹 **Goal**: Assign a recall notice to a **hazard category** & **product category**.  
🔹 **Models Used**:  
✅ **TF-IDF + XGBoost** (Baseline).  
✅ **Fine-Tuned GPT-2 & LLaMA (LoRA-PEFT)**.  
✅ **Ensemble Learning (Voting Classifier)** for hazard classification.  

📌 **More details**: See [`Task 1/README.md`](https://github.com/madhans476/Food-hazard-detection-SEMEVAL-2025/blob/fda1f55214af673a48ef485a72c563ee9135e17d/Task%201/readme.md).  


### **🔍 Task 2: Hazard & Product Extraction**  
🔹 **Goal**: Extract the **exact hazard reason** and **product name** from recall text.  
🔹 **Model Used**:  
✅ **Flan-T5-XL** (Fine-tuned with PEFT & LoRA).  
✅ **Prompt Engineering** for improved extraction.  

📌 **More details**: See [`Task 2/README.md`](https://github.com/madhans476/Food-hazard-detection-SEMEVAL-2025/blob/fda1f55214af673a48ef485a72c563ee9135e17d/Task%202/readme.md).  


## 🚀 Installation & Setup  

### **1️⃣ Install Dependencies**  
Ensure you have **Python 3.8+** installed. Then, run:  
```bash
pip install -r requirements.txt
```
### 2️⃣ Pre-Run Checklist
- Ensure dataset file path.
- Set up Hugging Face API token (for loading models).
- Set up WandB API key (if using experiment tracking).
- Verify fine-tuned model paths before execution.


## Acknowledgment

We acknowledge the authors for providing the dataset:

**Dataset Citation:**

Randl, Korbinian; Karvounis, Manos; Marinos, George; Pavlopoulos, John; Lindgren, Tony; Henriksson, Aron.  
*Food Recall Incidents*.  
Publisher: Zenodo, March 2024.  
DOI: [10.5281/zenodo.10891602](https://doi.org/10.5281/zenodo.10891602)

