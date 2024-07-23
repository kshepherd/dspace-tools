import json5
import sys
from typing import Set

def escape_newlines(s: str) -> str:
    return s.replace('\n', '\\n')

def extract_data(file_path: str) -> Set[str]:
    with open(file_path, 'r') as file:
        # Read the file content and remove comments and blank lines
        content = '\n'.join(line.strip() for line in file if line.strip() and not line.strip().startswith('//'))
    return json5.loads(content)

def compare_keys(file1: str, file2: str):
    data1 = extract_data(file1)
    data2 = extract_data(file2)
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())

    # Sets support union with |, intersection with &, difference with -, symmetric difference with ^
    # Here we want differences in both directions, but not really symmetric since I want to report them separately
    # to make it easy to copy into the new file
    only_in_file1 = keys1 - keys2
    only_in_file2 = keys2 - keys1

    print(f"Keys only in {file1} (printed with existing value, as comment, for reference):\n==")
    for key in sorted(only_in_file1):
        print(f'//"{key}": "{data1[key]}"')

    print(f"\n\nKeys only in {file2} (printed with existing value, as comment, for reference):\n==")
    for key in sorted(only_in_file2):
        print(f'//"{key}": "{data2[key]}"')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1.json5> <file2.json5>")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    compare_keys(file1, file2)
