from datasets import load_dataset

# Exemple avec Alpaca FR
dataset = load_dataset("baconnier/alpaca-fr", split="train")

# Sauvegarder en JSON
dataset.to_json("mon_dataset_entrainement.json")
