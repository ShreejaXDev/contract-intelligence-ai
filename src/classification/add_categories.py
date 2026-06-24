import pandas as pd

df = pd.read_csv(
    "data/processed/cuad_100_contracts.csv"
)

def assign_category(label):

    label = str(label).lower()

    if any(x in label for x in [
        "payment",
        "compensation",
        "fee",
        "escrow",
        "purchase",
        "wage",
        "salary",
        "remuneration"
    ]):
        return "Payment"

    elif any(x in label for x in [
        "confidential",
        "non disclosure"
    ]):
        return "Confidentiality"

    elif any(x in label for x in [
        "employment",
        "employee",
        "leave",
        "harassment",
        "accommodation",
        "maternity",
        "sick"
    ]):
        return "Employment"

    elif any(x in label for x in [
        "termination",
        "default"
    ]):
        return "Termination"

    elif any(x in label for x in [
        "warranty",
        "indemnification",
        "liability",
        "damages"
    ]):
        return "Liability"

    elif any(x in label for x in [
        "property",
        "premises",
        "deed"
    ]):
        return "Property"

    elif any(x in label for x in [
        "copyright",
        "trademark",
        "license",
        "work product"
    ]):
        return "Intellectual_Property"

    elif any(x in label for x in [
        "law",
        "dispute",
        "agreement",
        "jurisdiction"
    ]):
        return "Legal"

    elif any(x in label for x in [
        "performance",
        "duties",
        "reports"
    ]):
        return "Performance"

    else:
        return "General"

df["category"] = df["label"].apply(
    assign_category
)

print(
    df["category"].value_counts()
)

df.to_csv(
    "data/processed/cuad_100_categorized.csv",
    index=False
)

print("Saved Successfully")