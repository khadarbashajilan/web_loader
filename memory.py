import json

from langchain_core.messages import (
    AIMessage,
    HumanMessage,
)

from config import MEMORY_FILE


def ensure_memory_file():
    MEMORY_FILE.parent.mkdir(exist_ok=True)
    if not MEMORY_FILE.exists():
        MEMORY_FILE.write_text(json.dumps(None))


def load_memory():
    ensure_memory_file()
    with open(MEMORY_FILE) as f:
        return json.load(f)


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def serialize_messages(messages):
    return [
        {"type": m.type, "content": m.content}
        for m in messages
    ]


def deserialize_messages(data):
    if not data:
        return []
    return [
        HumanMessage(content=m["content"])
        if m["type"] == "human"
        else AIMessage(content=m["content"])
        for m in data
    ]


def get_session():
    data = load_memory()
    if data is None:
        return None
    return {
        "url": data["url"],
        "summary": data["summary"],
        "messages": deserialize_messages(
            data.get("messages", [])
        ),
    }


def set_session(session):
    data = {
        "url": session["url"],
        "summary": session["summary"],
        "messages": serialize_messages(
            session.get("messages", [])
        ),
    }
    save_memory(data)


def clear_session():
    save_memory(None)
