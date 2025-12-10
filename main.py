from datasets import load_dataset

# Exemple avec Alpaca FR
dataset = load_dataset("croissantllm/croissant_dataset", split="train")

# Sauvegarder en JSON
dataset.to_json("data/data-one.json")
