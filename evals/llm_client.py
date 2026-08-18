import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-opus-5"


def ask_about_record(record: dict, question: str) -> str:
    api_key = os.environ["ANTHROPIC_API_KEY"]
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"Here is a campaign record:\n{record}\n\nQuestion: {question}"

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    return next(block.text for block in response.content if block.type == "text")
