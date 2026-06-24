from datasets import load_dataset
import pdfplumber
import pandas as pd
import re
import os

print("Loading CUAD Dataset...")

dataset = load_dataset(
    "theatticusproject/cuad",
    verification_mode="no_checks"
)

train_data = dataset["train"]

all_clauses = []

# Skip document 0 (datasheet)
for idx in range(1, 21):

    print(f"Processing Contract {idx}")

    try:

        pdf = train_data[idx]["pdf"]

        full_text = ""

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

        pattern = r"\n(\d+\.\s+[^\n]+)"

        matches = list(
            re.finditer(
                pattern,
                full_text
            )
        )

        for i in range(len(matches)):

            start = matches[i].start()

            title = matches[i].group(1)

            if i < len(matches) - 1:
                end = matches[i + 1].start()
            else:
                end = len(full_text)

            section_text = full_text[start:end]

            title = re.sub(
                r"^\d+\.\s*",
                "",
                title
            )

            all_clauses.append({
                "contract_id": idx,
                "label": title.strip(),
                "text": section_text.strip()
            })

    except Exception as e:

        print(
            f"Error in contract {idx}: {e}"
        )

df = pd.DataFrame(all_clauses)

print("\nTotal Clauses:", len(df))
print("Unique Labels:", df["label"].nunique())

os.makedirs(
    "data/processed",
    exist_ok=True
)

df.to_csv(
    "data/processed/cuad_20_contracts.csv",
    index=False
)

print("\nDataset Saved Successfully!")