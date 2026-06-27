import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import pickle
import torch

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

print("Loading trained model...")

MODEL_PATH = "saved_model"

tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)

model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

print("Model Loaded Successfully!")

# -----------------------------------------------------
# Load Label Encoder
# -----------------------------------------------------

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

print("Label Encoder Loaded!")

# -----------------------------------------------------
# Prediction Function
# -----------------------------------------------------


def predict_clause(clause):

    inputs = tokenizer(
        clause,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():

        outputs = model(**inputs)

    logits = outputs.logits

    probabilities = torch.softmax(logits, dim=1)

    confidence, prediction = torch.max(
        probabilities,
        dim=1
    )

    category = label_encoder.inverse_transform(
        [prediction.item()]
    )[0]

    confidence = round(
        confidence.item() * 100,
        2
    )

    # -----------------------------
    # Top 3 Predictions
    # -----------------------------

    top_probs, top_indices = torch.topk(
        probabilities,
        k=3
    )

    top_predictions = []

    for prob, idx in zip(
        top_probs[0],
        top_indices[0]
    ):

        label = label_encoder.inverse_transform(
            [idx.item()]
        )[0]

        top_predictions.append({

            "category": label,

            "confidence": round(
                prob.item() * 100,
                2
            )

        })

    return {

        "category": category,

        "confidence": confidence,

        "top_predictions": top_predictions

    }


# -----------------------------------------------------
# Testing
# -----------------------------------------------------

if __name__ == "__main__":

    clause = """
    Payment shall be made within thirty days
    of invoice.
    """

    result = predict_clause(clause)

    print(result)