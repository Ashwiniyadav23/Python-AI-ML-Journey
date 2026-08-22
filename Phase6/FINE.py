# Fine-Tuning — Adapting a Pretrained Model to YOUR Task


# Step 1: Load a pretrained model and tokenizer

# pyrefly: ignore [missing-import]
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)   # e.g., 3 classes (positive/neutral/negative)    



# Step 2: Prepare your own labeled dataset


data = [("I love this product!", "positive"),
        ("This is not good.", "negative"),
        ("It’s okay, not great.", "neutral"),
        ("Excellent! I recommend it.", "positive")]

        
# pyrefly: ignore [missing-import]
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./my_finetuned_bert",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    logging_dir="./logs",
)

# pyrefly: ignore [missing-import]
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=data,  # your prepared dataset
    tokenizer=tokenizer,
)
    