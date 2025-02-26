# Task 1: Hazard and Product Category Classification  

## 📌 Task Overview  
Task 1 focuses on classifying food recall notices into **hazard categories** and **product categories** based on textual descriptions. The dataset contains structured recall information, including product descriptions and reasons for recall.  

We experimented with multiple models and techniques, including **TF-IDF + XGBoost**, **Parameter-Efficient Fine-Tuning (PEFT) of LLMs([GPT-2 large](https://huggingface.co/openai-community/gpt2-large), [Llama 3.1 1B](https://huggingface.co/meta-llama/Llama-3.2-1B) )**, and an **Ensemble Model** for improved performance.  

---

## 📊 Features Used  
We used the following features for classification:  

- **Text Vectorization**  
  - `text`: The recall notice text.  
  - `title`: The summary of recall notice text.  
  - Combined (`text + title`).  

- **Target Labels**
  - **Hazard Category (h-c)**: One of 10 categories. 
  - **Product Category (p-c)**: One of 22 categories.   

---

## ⚙️ Approach & Models Used  
We followed a **progressive approach** to improve classification performance:  

### **1️⃣ TF-IDF + XGBoost**    
- Convert text into **TF-IDF vectors** (n-grams up to bigrams).
- Train a **multi-class XGBoost classifier** separately for product and hazard categories.

### **2️⃣ PEFT (Fine-Tuning LLMs with Adapter Layers)**  
- Fine-tuned **GPT-2 Large & LLaMA 3.1 1B** using **PEFT** (Parameter-Efficient Fine-Tuning).  
- Used **LoRA (Low-Rank Adaptation)** to fine-tune a smaller subset of LLM parameters.  

### **3️⃣ Ensemble Model (Voting Classifier)**  
- Combined **TF-IDF + XGBoost, GPT-2, and LLaMA** predictions.  
- Used **hard voting** (majority rule) to determine final labels.   

---

## 🚀 How to Use the Code?  
### **1️⃣ Install Dependencies**  
Make sure you have all required libraries installed. Run:  

```bash
pip install -r requirements.txt
```

### **2️⃣ Dataset Placement** 
Ensure the dataset path is correctly mentioned.

### **3️⃣ Running the Models**  
Each notebook performs a specific function:
| Notebook                  | Purpose                                        |
|---------------------------|------------------------------------------------|
| `TF-IDF_XGBoost.ipynb`    | Train and evaluate TF-IDF + XGBoost model      |
| `peft.ipynb`              | Fine-tune GPT-2 / LLaMA using PEFT             |
| `ensemble.ipynb`          | Combine models using voting ensemble           |

- Run TF-IDF_XGBoost.ipynb first to generate baseline results.
- Then, execute peft.ipynb for LLM fine-tuning.
    - First fine-tune [GPT-2 large](https://huggingface.co/openai-community/gpt2-large) with peft.ipynb and then generate results on test.csv.
    - Next fine-tune [Llama 3.1 1B](https://huggingface.co/meta-llama/Llama-3.2-1B) with peft.ipynb and then generate results on test.csv.
- Finally, run ensemble.ipynb to make final predictions.








