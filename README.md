# Coding Agent

A simple AI coding agent powered by GPT-4o that can execute Python code, read, and write files to complete coding tasks.

## Usage

```bash
python coding_agent.py "your coding task here"
```

**Example:**
```bash
python coding_agent.py "Write a Python function to sort a list and test it"
```

If no task is provided, it defaults to computing fibonacci numbers.

## Requirements

- Python 3.x
- `openai` package
- `OPENAI_API_KEY` environment variable set

## Tools

The agent has access to three tools:

- `execute_python` — runs Python code and returns output
- `write_file` — writes content to a file
- `read_file` — reads content from a file
