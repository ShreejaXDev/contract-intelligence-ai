import re


def remove_extra_spaces(text):
    return re.sub(r"\s+", " ", text)


def remove_empty_lines(text):
    lines = text.splitlines()

    cleaned_lines = [line.strip() for line in lines if line.strip()]

    return "\n".join(cleaned_lines)


def normalize_text(text):

    text = remove_empty_lines(text)

    text = remove_extra_spaces(text)

    return text.strip()


if __name__ == "__main__":

    sample_text = """

    Hello      World


    This     is a     contract.

    """

    print(normalize_text(sample_text))