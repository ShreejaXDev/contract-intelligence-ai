import pdfplumber


def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    except Exception as e:
        print(f"Error: {e}")
        return ""


if __name__ == "__main__":

    pdf_path = "data/raw/contracts/sample_contract.pdf"

    extracted_text = extract_text_from_pdf(pdf_path)

    print(extracted_text[:3000])