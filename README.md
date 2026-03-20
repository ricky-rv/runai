# runai

> Write instructions. Run them.

`runai` is a new kind of runtime. Instead of writing code, you write what you want in plain English — and `runai` executes it.

```bash
runai helloworld.runai
```

---

## Install

```bash
pip install openai
git clone https://github.com/yourusername/runai.git
cd runai
pip install -e .
```

Set your OpenAI API key:

```bash
export OPENAI_API_KEY=your_key_here
```

Add that line to your `~/.zshrc` or `~/.bashrc` to make it permanent.

---

## Usage

Create a `.runai` file with natural language instructions:

**helloworld.runai**

```
# Print hello world
```

**countries.runai**

```
# Print all countries in the world sorted alphabetically
```

**fibonacci.runai**

```
# Print the first 20 fibonacci numbers
```

Then run it:

```bash
runai countries.runai
```

---

## How it works

1. `runai` reads your `.runai` file
2. Sends the instructions to GPT-4o
3. GPT-4o returns a Python script
4. `runai` executes it instantly and cleans up

---

## License

MIT
