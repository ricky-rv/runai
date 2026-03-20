<p align="center">
  <img src="https://raw.githubusercontent.com/ricky-rv/runai/refs/heads/main/runai.png" alt="runai" width="120" />
</p>

<h1 align="center">runai</h1>

<p align="center">
  <strong>Write English. Run it.</strong>
</p>

<p align="center">
  <a href="https://github.com/ricky-rv/runai/releases"><img src="https://img.shields.io/github/v/release/ricky-rv/runai?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
  <a href="https://pypi.org/project/openai/"><img src="https://img.shields.io/badge/requires-openai-blue?style=for-the-badge" alt="Requires OpenAI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-purple.svg?style=for-the-badge" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/python-3.8+-cyan?style=for-the-badge" alt="Python 3.8+">
</p>

---

**runai** is a new kind of runtime. Instead of writing code, you write what you want in plain English — and `runai` executes it.

No IDE. No syntax. Just intent.

```bash
runai countries.runai
```

```
Afghanistan
Albania
Algeria
...
```

---

## Install

```bash
pip install openai
git clone https://github.com/ricky-rv/runai.git
cd runai
pip install -e .
```

Set your OpenAI API key:

```bash
export OPENAI_API_KEY=your_key_here
```

Add to your `~/.zshrc` or `~/.bashrc` to make it permanent.

---

## Usage

Create a `.runai` file with plain English:

**countries.runai**

```
# Print all countries in the world sorted alphabetically
```

**fibonacci.runai**

```
# Print the first 20 fibonacci numbers
```

**calendar.runai**

```
# Print today's date, day of the week, and a countdown to New Year's Day
```

Then run it:

```bash
runai countries.runai
```

That's it.

---

## How it works

```
your_file.runai
      │
      ▼
┌─────────────────────┐
│        runai        │
│   (reads english)   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       GPT-4o        │
│  (generates code)   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Python runtime    │
│   (executes it)     │
└─────────────────────┘
           │
           ▼
        output
```

1. `runai` reads your `.runai` file
2. Sends the natural language to GPT-4o
3. GPT-4o returns a Python script
4. `runai` executes it instantly and cleans up

---

## More examples

```
# Fetch the top 10 most spoken languages and print them with speaker counts
```

```
# Generate a random strong password of 20 characters and print it
```

```
# Print a calendar for the current month
```

```
# Print a multiplication table for numbers 1 through 12
```

---

## Project structure

```
runai/
├── runai/
│   ├── __init__.py
│   ├── core.py       ← engine
│   └── cli.py        ← entry point
├── pyproject.toml
└── README.md
```

---

## Requirements

- Python 3.8+
- `openai>=1.0.0`
- `OPENAI_API_KEY` environment variable

---

## License

MIT — build whatever you want with it.

---

<p align="center">
  Built with 🚀 by <a href="https://github.com/ricky-rv">Ricky Raval</a>
</p>
