import sys

from evals.source_of_truth import get_record
from evals.llm_client import ask_about_record
from evals.number_extraction import extract_number
from evals.comparison import compare_to_expected

CAMPAIGN_ID = "camp_002"
FIELD = "roas"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    record = get_record(CAMPAIGN_ID)
    question = f"What was the {FIELD} for campaign {CAMPAIGN_ID}?"

    print(f"Record passed to Claude: {record}")
    print(f"Question: {question}")

    answer = ask_about_record(record, question)
    print(f"Claude's answer: {answer}")

    actual = extract_number(answer)

    result, reason = compare_to_expected(record[FIELD], actual)
    print(f"{result}: {reason}")


if __name__ == "__main__":
    main()
