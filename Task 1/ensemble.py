import pandas as pd

file1 = pd.read_csv("file1.csv")  # TF-IDF predictions
file2 = pd.read_csv("file2.csv")  # LLaMA predictions
file3 = pd.read_csv("file3.csv")  # GPT-2 predictions

hazard_tfidf = file1["predicted_hazard_category"]
hazard_llama = file2["predicted_hazard_category"]
hazard_gpt2 = file3["predicted_hazard_category"]
product_llama = file2["predicted_product_category"] # LLaMA's product category

# Hard Voting
final_hazard_category = []
for i in range(len(hazard_llama)):
    votes = [hazard_tfidf[i], hazard_llama[i], hazard_gpt2[i]]
    most_common = max(set(votes), key=votes.count)
    final_hazard_category.append(most_common if votes.count(most_common) >= 2 else hazard_llama[i])


final_df = pd.DataFrame({
    "hazard-category": final_hazard_category,
    "product-category": product_llama
})

# Save to CSV
final_df.to_csv("final_predictions.csv", index=False)
print("Final ensemble predictions saved to final_predictions.csv")
