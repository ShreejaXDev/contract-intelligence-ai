import spacy

print("Loading SpaCy Model...")

nlp = spacy.load("en_core_web_sm")

print("SpaCy Model Loaded Successfully!")


def extract_entities(text):
    """
    Extract named entities from contract text.
    """

    doc = nlp(text)

    entities = {
        "Organizations": [],
        "People": [],
        "Dates": [],
        "Money": [],
        "Locations": [],
        "Others": []
    }

    for ent in doc.ents:

        if ent.label_ == "ORG":
            entities["Organizations"].append(ent.text)

        elif ent.label_ == "PERSON":
            entities["People"].append(ent.text)

        elif ent.label_ == "DATE":
            entities["Dates"].append(ent.text)

        elif ent.label_ == "MONEY":
            entities["Money"].append(ent.text)

        elif ent.label_ in ["GPE", "LOC"]:
            entities["Locations"].append(ent.text)

        else:
            entities["Others"].append(ent.text)

    # Remove duplicates
    for key in entities:
        entities[key] = list(set(entities[key]))

    return entities


if __name__ == "__main__":

    sample = """
    ABC Technologies shall pay $5000 before 31 December 2026.
    John Smith signed this agreement in New York.
    """

    print(extract_entities(sample))