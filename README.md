# Coding Agent

A simple AI coding agent powered by GPT-4o that can execute Python code, read, and write files to complete coding tasks.

## Installation

```bash
pip install openai
```

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

Or add it to your shell profile (e.g., `~/.zshrc` or `~/.bashrc`) for persistence.

## Usage

```bash
python coding_agent.py "your coding task here"
```

**Examples:**

```bash
# Sort a list
python coding_agent.py "Write a Python function to sort a list and test it"

# Create a file
python coding_agent.py "Create a hello.py file that prints 'Hello, World!'"

# Analyze code
python coding_agent.py "Read coding_agent.py and explain what it does"
```

If no task is provided, it defaults to computing fibonacci numbers.

## Tools

The agent has access to three tools:

| Tool | Description |
|------|-------------|
| `execute_python` | Runs Python code and returns stdout/stderr |
| `write_file` | Writes content to a file |
| `read_file` | Reads content from a file |

## How It Works

1. The agent receives a coding task from the user
2. It uses GPT-4o to reason about the task and decide which tools to use
3. It executes the chosen tools and observes the results
4. This process repeats until the task is complete (up to 10 iterations)

## Configuration

You can customize the agent by modifying `coding_agent.py`:

- `MODEL` - Change the OpenAI model (default: `gpt-4o`)
- `max_iterations` - Adjust max tool-use iterations (default: 10)
