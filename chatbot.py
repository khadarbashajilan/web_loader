from langchain_core.messages import HumanMessage

from chat import ask_question
from cli import (
    console,
    show_ai_message,
    show_error,
    show_info,
    show_summary,
)
from memory import (
    clear_session,
    get_session,
    set_session,
)
from summarizer import summarize_url


def handle_command(user_input: str):

    if user_input.startswith("/url "):

        url = user_input.replace(
            "/url ", "", 1
        ).strip()

        try:
            with console.status(
                "[bold green]Reading webpage..."
            ):
                result = summarize_url(url)
        except Exception as e:
            show_error(f"Failed: {e}")
            return True

        session = {
            "url": result["url"],
            "summary": result["summary"],
            "messages": [],
        }
        set_session(session)
        show_summary(result["summary"])
        return True

    if user_input == "/help":

        show_info(
            "/url <url>   Summarize a webpage\n"
            "/help         Show this help\n"
            "/exit         Clear memory and exit\n\n"
            "Anything else will be sent as "
            "a chat message."
        )
        return True

    if user_input == "/exit":
        clear_session()
        return False

    session = get_session()

    if not session:
        show_error(
            "No webpage loaded. Use /url <url> first."
        )
        return True

    with console.status(
        "[bold cyan]Thinking..."
    ):

        answer = ask_question(
            user_input,
            session["summary"],
            session["messages"],
        )

    session["messages"].append(
        HumanMessage(content=user_input)
    )
    session["messages"].append(answer)
    set_session(session)

    show_ai_message(answer.content)
    return True
