# Using Transformers — the Basic Pattern

# Example 1 — Using BERT for sentiment classification (no training needed, just using it)


# pyrefly: ignore [missing-import]
from transformers import pipeline


classifier = pipeline("sentiment-analysis")

result = classifier("I absolutely loved this movie!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9998}]


# Example 2 — Using GPT-2 for text generation


# pyrefly: ignore [missing-import]
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

result = generator("The future of AI is", max_length=30, num_return_sequences=1)
print(result[0]["generated_text"])
# "The future of AI is going to be shaped by how we choose to..."



# Step 1: Load a pretrained model and tokenizer

# pyrefly: ignore [missing-import]
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")


# Step 2: Prepare your own labeled dataset


# pyrefly: ignore [missing-import]
from datasets import dataset

data ={
    "text" :["I love this product", "This is terrible ","Amazing qality", "Very disappointing"],
    "label" : [1,0,1,0] #1 = postive, 0 = negative
}
dataset = Dataset.from_dict(data)

def tokenizer_function(examples):
    return tokenizer(examples["text"], truncation= True)
tokenized_dataset = dataset.map(tokenizer_function, batched=True)
print(tokenized_dataset)    

# Step 3: Train the model on your data
# pyrefly: ignore [missing-import]
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="/tmp/test-trainer",
    evaluation_strategy="epoch",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    logging_dir="/tmp/logs",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()
