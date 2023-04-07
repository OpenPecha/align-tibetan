from transformers import AutoModelForSequenceClassification, AutoTokenizer
model_path = "model"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
# push model and tokenizer to huggingface hub
model.push_to_hub("buddhist-nlp/bod-eng-similarity")
tokenizer.push_to_hub("buddhist-nlp/bod-eng-similarity")