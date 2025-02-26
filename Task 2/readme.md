# 🏆 Task 2: Food Hazard & Product Extraction  

## 📌 Task Overview  
Task 2 focuses on **extracting the exact hazard and product mentions** from food recall notices. Unlike Task 1 (which classifies categories), this task aims for **fine-grained entity extraction**, identifying the precise **hazard reason** and **product name** in text.  

To achieve this, we employ:  
- **Prompt-based Extraction**: Uses **instruction-tuned LLMs** for precise text span retrieval.  
- **Fine-Tuned Flan-T5-XL**: A language model adapted for text generation tasks.  

---

## 📊 Features Used  

- **Text Fields**  
  - `title`: Summary of the recall notice.  
  - `text`: Full recall notice description.  

- **Target Outputs**  
  - `product` → The exact food product name in the recall notice.  
  - `hazard` → The exact hazard reason in the recall notice.  

---

## ⚙️ Approach & Model Used  

### **1️⃣ Prompt-Based Fine-Tuning with Flan-T5-XL**  
- We fine-tuned **[Google's Flan-T5-XL](https://huggingface.co/google/flan-t5-xl)** to generate structured outputs.  
- **LoRA-based PEFT** was used to train efficiently with limited resources.  

### **2️⃣ Task-Specific Prompt Engineering**  
To guide the model, we designed structured prompts:  

#### **Product Extraction Prompt**  
> *"Extract only the recall food product from the following food recall text: {text}"*  

#### **Hazard Extraction Prompt**  
> *"Extract the exact reason for the food recall from the given text. Provide only the specific recall reason, without including any other information, from the following recall text: {text}"*  


## 🚀 How to Use the Code?  

### **1️⃣ Install Dependencies**  
Run the following command to install required libraries:  

```bash
pip install -r requirements.txt
```

### 2️⃣ Thinks to check!!!
1. Dataset paths
2. Hugging face token
3. Wandb API key
4. Fine tuned model path

### 3️⃣ Running the Model
|Notebook	                |Purpose                                            |
|-------------------------|---------------------------------------------------|
|`prompt_based_peft.ipynb`|	Fine-tune Flan-T5-XL for hazard/product extraction|

- Run prompt_based_peft.ipynb to generate results.
