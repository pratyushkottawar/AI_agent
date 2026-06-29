# 🤖 AI Agent — Python × Gemini

> A sandboxed AI agent built in Python that uses Google's Gemini API to reason, plan, and interact with a local codebase — safely.

![AI Agent Banner](hhttps://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fbernardmarr.com%2Fhow-ai-agents-will-revolutionize-your-day-to-day-lif%2F&ved=0CBYQjRxqFwoTCKiqkZfsrJUDFQAAAAAdAAAAABA4&opi=89978449)

---

## 📌 Overview

This project is a hands-on implementation of an AI agent from scratch, built as part of the [Boot.dev](https://www.boot.dev) backend development curriculum.

The agent uses **Google Gemini 2.5 Flash** as its brain and is given a set of tools it can call to interact with a local working directory — reading files, understanding code structure, and more. All tool calls are sandboxed to a permitted working directory to prevent the agent from running amok on your machine.

---

## ✨ Features

- 🧠 **Powered by Gemini 2.5 Flash** — fast, capable LLM reasoning
- 📁 **File system tools** — agent can list and inspect files within a sandboxed directory
- 🔒 **Security-first** — all file operations are restricted to a permitted working directory
- 🛠️ **Extensible tool system** — easily add new tools for the agent to call
- 🐍 **Pure Python** — minimal dependencies, clean architecture

---

## 🗂️ Project Structure

```
aiagent/
├── main.py                   # Entry point — runs the agent
├── functions/
│   └── get_files_info.py     # Tool: list files in a directory
├── calculator/               # Sample working directory for the agent
│   ├── main.py
│   ├── tests.py
│   └── pkg/
│       ├── calculator.py
│       └── render.py
├── test_get_files_info.py    # Manual test script
├── pyproject.toml            # Project dependencies
└── .env                      # API keys (never committed)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

```bash
# Clone the repo
git clone https://github.com/pratyushkottawar/ProductService_3rdPartyAPI.git
cd aiagent

# Install dependencies
uv sync
```

### Configuration

Create a `.env` file in the root of the project:

```env
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file. It is already included in `.gitignore`.

### Run the Agent

```bash
uv run main.py
```

### Run Tests

```bash
uv run test_get_files_info.py
```

---

## 🔧 How It Works

### The Agent Loop

1. A prompt is sent to **Gemini 2.5 Flash**
2. Gemini decides whether to call a tool or respond directly
3. If a tool is called, the result is fed back to Gemini
4. The loop continues until Gemini produces a final answer

### Tools Available

| Tool             | Description                                   |
| ---------------- | --------------------------------------------- |
| `get_files_info` | Lists files and metadata in a given directory |

### Security Model

Every tool that touches the file system validates that the target path falls within the permitted `working_directory`:

```python
target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
```

This prevents directory traversal attacks like `../../etc/passwd`.

---

## 📦 Dependencies

| Package         | Purpose                                |
| --------------- | -------------------------------------- |
| `google-genai`  | Gemini API client                      |
| `python-dotenv` | Load environment variables from `.env` |

---

## 📚 Built With

- [Boot.dev AI Agent Course](https://www.boot.dev)
- [Google Gemini API](https://ai.google.dev/)
- [uv — Python package manager](https://github.com/astral-sh/uv)

---

## 👤 Author

**Pratyush Kottawar**

- GitHub: [@pratyushkottawar](https://github.com/pratyushkottawar)

---

## 📄 License

This project is for educational purposes as part of the Boot.dev curriculum.
