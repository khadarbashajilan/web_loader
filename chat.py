import os

from dotenv import load_dotenv

from langchain_core.messages import AIMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_openrouter import ChatOpenRouter

from config import MODEL_NAME

load_dotenv()


def ask_question(
    question: str,
    summary: str,
    history: list,
) -> AIMessage:

    llm = ChatOpenRouter(
        model=MODEL_NAME,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a study assistant. "
                "Use ONLY the provided summary.\n\n"
                "Summary:\n{summary}",
            ),
            MessagesPlaceholder(
                variable_name="history"
            ),
            ("human", "{question}"),
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "summary": summary,
            "history": history,
            "question": question,
        }
    )

    return AIMessage(content=response.content)
