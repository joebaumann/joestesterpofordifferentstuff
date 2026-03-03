# Contributing

> **Note:** This repository was generated solely for debugging purposes and is not intended for active development or production use.

## Overview

This project is a minimal AI coding agent (~73 lines of Python) powered by GPT-4o. It accepts a natural-language task, iteratively calls tools (execute Python, read file, write file), and returns the result. Contributions should maintain this simplicity.

## Project Structure

```
.
├── coding_agent.py   # Core agent logic
└── README.md         # Usage documentation
```

## How to Contribute

### Reporting Issues

Open an issue describing:
- What you expected to happen
- What actually happened
- Steps to reproduce (including the task string you passed)
- Python version and OS

### Submitting Changes

1. Fork the repository and create a branch from `main`.
2. Make your changes, keeping the code minimal and focused.
3. Test your changes manually:
   ```bash
   python coding_agent.py "Write a Python function to sort a list and test it"
   ```
4. Open a pull request with a clear description of the change and why it is needed.

### Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Keep functions short and single-purpose.
- Avoid adding dependencies beyond `openai` unless strictly necessary.
- Do not add error handling for scenarios that cannot realistically occur.

## Architecture Notes

The agent loop (`run_coding_task`) works as follows:

1. A system prompt and the user task are placed into `messages`.
2. GPT-4o is called with the three available tools.
3. If the model returns `finish_reason == "stop"`, the loop exits and the final message is returned.
4. Otherwise, each tool call is dispatched to `TOOL_HANDLERS`, the result is appended to `messages`, and the loop continues.
5. After `max_iterations` (default 10) the agent exits with a timeout message.

Any contribution that alters this loop should preserve this basic contract.

## Configuration

Two constants in `coding_agent.py` can be changed without breaking anything else:

| Constant | Default | Purpose |
|---|---|---|
| `MODEL` | `"gpt-4o"` | OpenAI model to use |
| `max_iterations` | `10` | Maximum tool-use iterations per task |

## Adding a New Tool

1. Add a function definition to the `TOOLS` list (OpenAI function-calling schema).
2. Implement the handler function.
3. Register it in `TOOL_HANDLERS`.

No other changes to the agent loop are required.

## License

This project has no explicit license. Contact the repository owner before reusing or distributing the code.
