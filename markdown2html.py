#!/usr/bin/python3
"""
This module provide a functionfor converting
a Markdown file to HTML.
"""

import sys
import markdown

def markdown2html(input_file: str, output_file: str):
    """
    Convert the input Markdown file to HTML and save
    it to the output file.

    :param input_file: path to the Markdown file
    :param out_file: path to the HTML file
    """
    try:
        with open(input_file, 'r') as md_file:
            html = markdown.markdown(mk_file.read())
            with open(output_file, 'w') as html_file:
                html_file.write(html)
    except FileNotFoundError:
        print(f"Missing (input_file)", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input_file> <out_file>", file=sys.stderr)
        sys.exit(1)
    markdown2html(sys.argv[1], sys.argv[2])