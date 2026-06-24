import os
import re
import pdfplumber
import pandas as pd

CONTRACT_FOLDER = "data/raw/contracts"

all_clauses = []

for filename in os.listdir(CONTRACT_FOLDER):

    if not filename.endswith(".pdf"):
        continue

    pdf_path = os.path.join(
        CONTRACT_FOLDER,
        filename
    )

    print(f"Processing: {filename}")

    try:

        full_text = ""

        with pdfplumber.open(pdf_path) as pdf:

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
                "label": title.strip(),
                "text": section_text.strip()
            })

    except Exception as e:

        print(
            f"Error in {filename}: {e}"
        )

df = pd.DataFrame(all_clauses)

print("\nTotal Clauses:")
print(len(df))

print("\nUnique Labels:")
print(df["label"].nunique())

os.makedirs(
    "data/processed",
    exist_ok=True
)

df.to_csv(
    "data/processed/cuad_training.csv",
    index=False
)

print(
    "\nDataset Saved Successfully!"
)