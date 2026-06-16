from src.ner.entity_extractor import extract_entities

sample_text = """
This agreement is between ABC Corporation and XYZ Ltd.
Payment of $50000 shall be made before January 1, 2027.
"""

entities = extract_entities(sample_text)

for entity in entities:
    print(entity)