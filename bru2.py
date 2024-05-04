from transformers import AutoTokenizer

model_name = "google/vit-base-patch16-224"
tokenizer = AutoTokenizer.from_pretrained(model_name)

