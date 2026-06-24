import pandas as pd
import re

df = pd.read_csv(
    "data/processed/cuad_20_contracts.csv"
)

def clean_label(label):

    label = str(label)

    # take only first sentence
    label = label.split(".")[0]

    # remove extra spaces
    label = label.strip()

    # uppercase headings become cleaner
    return label

df["clean_label"] = df["label"].apply(
    clean_label
)

print(
    df["clean_label"].value_counts().head(50)
)

df.to_csv(
    "data/processed/cuad_20_contracts_cleaned.csv",
    index=False
)

print("Saved")