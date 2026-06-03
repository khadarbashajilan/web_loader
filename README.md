# Web Research Assistant

A terminal-based AI research assistant built with Python, LangChain, OpenRouter, and Rich.

It can:

* Summarize webpages into study notes
* Chat with your saved notes via session memory
* Run entirely from the terminal

---

## Features

### Web Summarization

Load any webpage:

```bash
/url https://docs.langchain.com/
```

The assistant:

1. Downloads the webpage
2. Extracts readable text
3. Generates concise study notes
4. Loads the notes into the current session

---

### Chat With Notes

After loading a webpage:

```text
> what is langchain?

> explain tools

> compare chains and agents
```

The assistant answers using the summarized notes as context.

---

### Session Memory

Memory stores only the current session (URL, summary, and message history).  
Starting a new URL overwrites the previous session. Exiting wipes all memory.

---

### Exit Behavior

When exiting:

```bash
/exit
```

Memory is wiped immediately and the assistant exits.

---

## Installation

### Clone

```bash
git clone <your-repo-url>
cd web-loader
```

### Install Dependencies

Using UV:

```bash
uv sync
```

Or manually:

```bash
uv add \
    langchain \
    langchain-openrouter \
    beautifulsoup4 \
    requests \
    python-dotenv \
    rich
```

---

## Configuration

Create your environment file:

```bash
cp .env.example .env
```

Add your OpenRouter API key:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## Running

Start the assistant:

```bash
uv run main.py
```

You should see:

```text
Web Research Assistant

Type /help
```

---

## Commands

### Summarize a webpage

```bash
/url https://overthewire.org/wargames/bandit/
```

### Help

```bash
/help
```

### Exit (wipes memory)

```bash
/exit
```

---

## Project Structure

```text
web-loader/
│
├── main.py
├── chatbot.py
├── chat.py
├── summarizer.py
├── memory.py
├── config.py
├── cli.py
│
├── data/
│   └── memory.json
│
├── .env.example
├── README.md
├── pyproject.toml
└── .gitignore
```

---

## Example Workflow

```text
> /url https://overthewire.org/wargames/bandit/

(summary displayed in green panel)

> what does bandit teach?

(Answer displayed in cyan panel)

> /exit

Goodbye!
```

---

## Future Improvements

* PDF support
* YouTube transcript summarization
* Multi-document chat
* Vector database retrieval
* Local embeddings
* Streaming responses
* Export notes to Markdown
* Export notes to PDF
* Conversation history
* Multi-model support
* Source citations
