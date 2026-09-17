import os
from typing import Optional

from openai import OpenAI


def get_client() -> Optional[OpenAI]:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return None

    return OpenAI(api_key=api_key)


def ask_ai(message: str) -> str:
    client = get_client()

    if client is None:
        return (
            "Akash AI backend is connected, but the AI API key "
            "has not been configured yet."
        )

    response = client.responses.create(
        model="gpt-5",
        input=message
    )

    return response.output_text
