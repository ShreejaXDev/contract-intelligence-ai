import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from datasets import Dataset

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    TrainingArguments,
    Trainer
)

# =====================================================
# LOAD DATASET
# =====================================================

print("Loading Dataset...")

df = pd.read_csv(
    "data/processed/final_training_dataset.csv"
)

df = df[["text", "category"]]

df = df.dropna()

print("Dataset Shape:", df.shape)

# =====================================================
# LABEL ENCODING
# =====================================================

label_encoder = LabelEncoder()

df["label"] = label_encoder.fit_transform(
    df["category"]
)

print("\nClasses:")
print(label_encoder.classes_)

# save label encoder

with open(
    "label_encoder.pkl",
    "wb"
) as f:

    pickle.dump(
        label_encoder,
        f
    )

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

print("\nTrain:", train_df.shape)
print("Test:", test_df.shape)

# =====================================================
# HUGGINGFACE DATASET
# =====================================================

train_dataset = Dataset.from_pandas(
    train_df
)

test_dataset = Dataset.from_pandas(
    test_df
)

# =====================================================
# TOKENIZER
# =====================================================

print("\nLoading Tokenizer...")

tokenizer = DistilBertTokenizerFast.from_pretrained(
    "distilbert-base-uncased"
)

def tokenize(batch):

    return tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=256
    )

train_dataset = train_dataset.map(
    tokenize,
    batched=True
)

test_dataset = test_dataset.map(
    tokenize,
    batched=True
)

# =====================================================
# FORMAT DATASET
# =====================================================

train_dataset = train_dataset.rename_column(
    "label",
    "labels"
)

test_dataset = test_dataset.rename_column(
    "label",
    "labels"
)

train_dataset.set_format(
    "torch",
    columns=[
        "input_ids",
        "attention_mask",
        "labels"
    ]
)

test_dataset.set_format(
    "torch",
    columns=[
        "input_ids",
        "attention_mask",
        "labels"
    ]
)

# =====================================================
# MODEL
# =====================================================

print("\nLoading DistilBERT...")

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=len(
        label_encoder.classes_
    )
)

# =====================================================
# TRAINING ARGUMENTS
# =====================================================

training_args = TrainingArguments(
    output_dir="./results",

    num_train_epochs=2,

    per_device_train_batch_size=4,

    per_device_eval_batch_size=4,

    logging_steps=25,

    save_strategy="epoch",

    report_to="none"
)

# =====================================================
# TRAINER
# =====================================================

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

# =====================================================
# TRAIN
# =====================================================

print("\nStarting Training...\n")

trainer.train()

# =====================================================
# SAVE MODEL
# =====================================================

print("\nSaving Model...")

model.save_pretrained(
    "saved_model"
)

tokenizer.save_pretrained(
    "saved_model"
)

print("\nTraining Complete!")
print("Model saved in: saved_model/")