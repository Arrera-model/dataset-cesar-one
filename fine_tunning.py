from datasets import load_dataset


second_train_one = load_dataset("jpacifico/French-Alpaca-dataset-Instruct-55K",split="train")
second_train_two = load_dataset("OpenAssistant/oasst1",split="train")
second_train_theer = load_dataset("PhilSad/Instruct-fr-merged",split="train")

second_train_one.to_json("second-train/data-one.json")
second_train_two.to_json("second-train/data-two.json")
second_train_theer.to_json("second-train/data-theer.json")