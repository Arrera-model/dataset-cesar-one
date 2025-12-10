from datasets import load_dataset

# Pre-entrainement
first_train_one = load_dataset("croissantllm/croissant_dataset",split="train")
first_train_two = load_dataset("oscar-corpus/OSCAR-2301", split="train")

first_train_one.to_json("first-train/data-one.json")
first_train_two.to_json("first-train/data-tow.json")