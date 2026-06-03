from pathlib import Path

BASE_DIR = Path(__file__).parent

MEMORY_FILE = BASE_DIR / "data" / "memory.json"

MODEL_NAME = "mistral-small-latest"

MAX_CONTENT_LENGTH = 20000

USER_AGENT = "web-summarizer/1.0"
