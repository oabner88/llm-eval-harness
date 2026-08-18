import re

NUMBER_PATTERN = re.compile(r"(?<![\w.])\$?\d[\d,]*(?:\.\d+)?")


def extract_number(text: str) -> float | None:
    match = NUMBER_PATTERN.search(text)
    if not match:
        return None

    number_str = match.group().lstrip("$").replace(",", "")
    return float(number_str)
