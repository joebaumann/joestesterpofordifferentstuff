import json, subprocess, sys
from openai import OpenAI

client = OpenAI()
MODEL = "gpt-4o"

TOOLS = [
    {"type": "function", "function": {
        "name": "execute_python",
        "description": "Execute Python code and return stdout/stderr",
        "parameters": {"type": "object", "properties": {
            "code": {"type": "string", "description": "Python code to execute"}
        }, "required": ["code"]},
    }},
    {"type": "function", "function": {
        "name": "write_file",
        "description": "Write content to a file",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"},
            "content": {"type": "string"},
        }, "required": ["path", "content"]},
    }},
    {"type": "function", "function": {
        "name": "read_file",
        "description": "Read content from a file",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"},
        }, "required": ["path"]},
    }},
]


def execute_python(code: str) -> str:
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=30)
    return r.stdout + (f"\nSTDERR: {r.stderr}" if r.stderr else "")

def write_file(path: str, content: str) -> str:
    open(path, "w").write(content)
    return f"Written {len(content)} bytes to {path}"

def read_file(path: str) -> str:
    return open(path).read()

TOOL_HANDLERS = {
    "execute_python": lambda a: execute_python(**a),
    "write_file": lambda a: write_file(**a),
    "read_file": lambda a: read_file(**a),
}


def run_coding_task(task: str, max_iterations: int = 10) -> str:
    messages = [
        {"role": "system", "content": "You are a coding agent. Use tools to complete coding tasks."},
        {"role": "user", "content": task},
    ]
    for _ in range(max_iterations):
        response = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
        msg = response.choices[0].message
        messages.append(msg)
        if response.choices[0].finish_reason == "stop":
            return msg.content or ""
        for tc in msg.tool_calls or []:
            args = json.loads(tc.function.arguments)
            print(f"[tool] {tc.function.name}({args})")
            result = TOOL_HANDLERS[tc.function.name](args)
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})
    return "Max iterations reached"


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "Write a Python function to compute fibonacci numbers and test it"
    print(run_coding_task(task))
