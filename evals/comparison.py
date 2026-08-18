TOLERANCE = 0.01


def compare_to_expected(expected: float, actual: float | None) -> tuple[str, str]:
    if actual is None:
        return "FAIL", "no number extracted"

    if abs(actual - expected) <= TOLERANCE:
        return "PASS", f"{actual} matches expected {expected}"

    return "FAIL", f"expected {expected}, got {actual}"
