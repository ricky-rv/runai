import sys
import os
from . core import parse_file, generate_code, run_code

def main():
    if len(sys.argv) < 2:
        print("Usage: runai <file.runai>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    if not filepath.endswith(".runai"):
        print("Warning: Expected a .runai file.")

    instructions = parse_file(filepath)

    if not instructions:
        print("Error: No instructions found in file.")
        sys.exit(1)

    code = generate_code(instructions)
    run_code(code)

if __name__ == "__main__":
    main()