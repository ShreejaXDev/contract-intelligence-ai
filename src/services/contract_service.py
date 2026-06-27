from src.ingestion.pdf_parser import extract_text_from_pdf
from src.preprocessing.clause_splitter import split_into_clauses
from src.classification.predict_clause import predict_clause
from src.risk.risk_analyzer import analyze_risk
from src.ner.entity_extractor import extract_entities


def analyze_contract(pdf_path):
    """
    Complete Contract Analysis Pipeline

    Steps:
    1. Extract text from PDF
    2. Split into clauses
    3. Predict clause category using DistilBERT
    4. Get prediction confidence
    5. Get Top-3 predictions
    6. Analyze risk
    7. Extract named entities
    8. Return structured JSON
    """

    print("=" * 60)
    print("Starting Contract Analysis...")
    print("=" * 60)

    # --------------------------------------------------
    # STEP 1 : Extract Text
    # --------------------------------------------------

    text = extract_text_from_pdf(pdf_path)

    if not text:
        return {
            "status": "error",
            "message": "No text could be extracted from the PDF."
        }

    print("✓ Text Extracted Successfully")

    # --------------------------------------------------
    # STEP 2 : Split into Clauses
    # --------------------------------------------------

    clauses = split_into_clauses(text)

    print(f"✓ {len(clauses)} Clauses Found")

    predictions = []

    high = 0
    medium = 0
    low = 0

    # --------------------------------------------------
    # STEP 3 : Analyze Every Clause
    # --------------------------------------------------

    for i, clause in enumerate(clauses):

        # DistilBERT Prediction
        prediction = predict_clause(clause)

        category = prediction["category"]
        confidence = prediction["confidence"]
        top_predictions = prediction["top_predictions"]

        # Risk Analysis
        risk = analyze_risk(category)

        # Named Entity Recognition
        entities = extract_entities(clause)

        # Count Risk Levels
        if risk["risk"] == "High":
            high += 1

        elif risk["risk"] == "Medium":
            medium += 1

        else:
            low += 1

        # Store Prediction
        predictions.append({

            "clause_number": i + 1,

            "category": category,

            "confidence": confidence,

            "top_predictions": top_predictions,

            "risk_level": risk["risk"],

            "reason": risk["reason"],

            "entities": entities,

            "text": clause

        })

    print("✓ Contract Analysis Completed Successfully")

    # --------------------------------------------------
    # FINAL RESPONSE
    # --------------------------------------------------

    return {

        "status": "success",

        "total_clauses": len(predictions),

        "risk_summary": {

            "High": high,

            "Medium": medium,

            "Low": low

        },

        "predictions": predictions

    }