import os
from datetime import datetime

import requests

from bs4 import BeautifulSoup

from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

from config import (
    MODEL_NAME,
    MAX_CONTENT_LENGTH,
    USER_AGENT,
)

load_dotenv()

os.environ["USER_AGENT"] = USER_AGENT


def fetch_webpage(url: str) -> str:
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        timeout=30,
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    for tag in soup(
        ["script", "style", "noscript"]
    ):
        tag.decompose()

    text = soup.get_text("\n")

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n".join(lines)


def summarize_url(url: str):

    content = fetch_webpage(url)

    content = content[:MAX_CONTENT_LENGTH]

    llm = ChatMistralAI(
        model=MODEL_NAME,
        api_key=os.getenv(
            "MISTRAL_API_KEY"
        ),
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_template(
        """
Summarize the following web content in a clean, readable format.

Structure:
- One short paragraph explaining what this page is about
- Key points as bullet points
- One-sentence bottom line at the end

Keep it concise. Use Markdown.

Content:

{content}
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {"content": content}
    )

    return {
        "url": url,
        "summary": response.content,
        "timestamp": datetime.now().isoformat(),
    }
