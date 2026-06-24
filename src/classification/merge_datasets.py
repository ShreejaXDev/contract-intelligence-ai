import pandas as pd

# CUAD 100 contracts
cuad_df = pd.read_csv(
    "data/processed/cuad_100_categorized.csv"
)

# Your local PDFs dataset
local_df = pd.read_csv(
    "data/processed/cuad_training.csv"
)

# Keep only required columns
cuad_df = cuad_df[
    ["text", "category"]
]

local_df = local_df[
    ["text", "category"]
]

# Merge
final_df = pd.concat(
    [cuad_df, local_df],
    ignore_index=True
)

print("\nTotal Samples:")
print(len(final_df))

print("\nCategory Distribution:")
print(
    final_df["category"].value_counts()
)

final_df.to_csv(
    "data/processed/final_training_dataset.csv",
    index=False
)

print("\nFinal Dataset Saved Successfully!")