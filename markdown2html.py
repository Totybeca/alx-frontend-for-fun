#!/usr/bin/python3
import sys
import markdown

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "r") as f:
        markdown_text = f.read()
except FileNotFoundError:
    sys.stderr.write(f"Missing {input_file}\n")
    sys.exit(1)

html_text = markdown.markdown(markdown_text)

with open(output_file, "w") as f:
    f.write(html_text)

sys.exit(0)