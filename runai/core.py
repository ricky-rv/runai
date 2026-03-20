import os
import subprocess
import sys
import tempfile
from openai import OpenAI

SYSTEM_PROMPT = """You are a code generator. The user will give you natural language instructions.
Your job is to convert those instructions into a single, complete, runnable Python script.

Rules:
- Output ONLY raw Python code. No markdown, no backticks, no explanation whatsoever.
- Do NOT wrap the output in any code fences or backticks.
- Do NOT add any notes, comments, or explanations outside of the code.
- Use only the Python standard library unless the user explicitly mentions a package.
- If the instructions are ambiguous, make your best guess and produce working code.
- The script should print its output to stdout.
"""

def get_client():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Run: export OPENAI_API_KEY=your_key_here")
        sys.exit(1)
    return OpenAI(api_key=api_key)

def parse_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    instructions = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("//"):
            continue
        if stripped.startswith("#"):
            stripped = stripped[1:].strip()
        if stripped:
            instructions.append(stripped)
    return "\n".join(instructions)

def strip_fences(code):
    lines = code.splitlines()
    lines = [line for line in lines if not line.strip().startswith("```")]
    # Also strip any trailing lines that don't look like Python
    while lines and not lines[-1].strip().startswith((" ", "\t", "def ", "class ", "import ", "from ", "if ", "for ", "while ", "print", "return")) and "=" not in lines[-1] and not lines[-1].strip().startswith("#"):
        last = lines[-1].strip()
        if last and not any(c in last for c in ["(", ")", "[", "]", ":", '"', "'"]):
            lines.pop()
        else:
            break
    return "\n".join(lines).strip()

def generate_code(instructions):
    client = get_client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": instructions}
        ],
        temperature=0.2,
    )
    code = response.choices[0].message.content.strip()
    return strip_fences(code)

def run_code(code):
    with tempfile.NamedTemporaryFile(suffix=".py", mode="w", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name
    try:
        result = subprocess.run([sys.executable, tmp_path], capture_output=False)
        if result.returncode != 0:
            sys.exit(result.returncode)
    finally:
        os.unlink(tmp_path)