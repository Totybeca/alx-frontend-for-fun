#!/usr/bin/python3
import sys
import os
import markdown


def convert_markdown_to_html(markdown_file, output_file):
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the contents of the Markdown file
    with open(markdown_file, "r") as f:
        markdown_text = f.read()

    # Convert Markdown to HTML
    html_text = markdown.markdown(markdown_text)

    # Write the HTML output to a file
    with open(output_file, "w") as f:
        f.write(html_text)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Get the Markdown file and output file names from the command line arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML and write to the output file
    convert_markdown_to_html(markdown_file, output_file)

    # Print nothing and exit successfully
    sys.exit(0)
    
    def convert_markdown_to_html(markdown_file, output_file):
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the contents of the Markdown file
    with open(markdown_file, "r") as f:
        markdown_text = f.read()

    # Convert Markdown to HTML
    html_text = markdown.markdown(markdown_text)

    # Parse headings and replace with HTML
    html_text = html_text.replace("<p># ", "<h1>").replace(" #</p>", "</h1>")
    html_text = html_text.replace("<p>## ", "<h2>").replace(" ##</p>", "</h2>")
    html_text = html_text.replace("<p>### ", "<h3>").replace(" ###</p>", "</h3>")
    html_text = html_text.replace("<p>#### ", "<h4>").replace(" ####</p>", "</h4>")
    html_text = html_text.replace("<p>##### ", "<h5>").replace(" #####</p>", "</h5>")
    html_text = html_text.replace("<p>###### ", "<h6>").replace(" ######</p>", "</h6>")

    # Write the HTML output to a file
    with open(output_file, "w") as f:
        f.write(html_text)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Get the Markdown file and output file names from the command line arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML and write to the output file
    convert_markdown_to_html(markdown_file, output_file)

    # Print nothing and exit successfully
    sys.exit(0)

def convert_markdown_to_html(markdown_file, output_file):
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the contents of the Markdown file
    with open(markdown_file, "r") as f:
        markdown_text = f.read()

    # Convert Markdown to HTML
    html_text = markdown.markdown(markdown_text)

    # Parse headings and replace with HTML
    html_text = html_text.replace("<p># ", "<h1>").replace(" #</p>", "</h1>")
    html_text = html_text.replace("<p>## ", "<h2>").replace(" ##</p>", "</h2>")
    html_text = html_text.replace("<p>### ", "<h3>").replace(" ###</p>", "</h3>")
    html_text = html_text.replace("<p>#### ", "<h4>").replace(" ####</p>", "</h4>")
    html_text = html_text.replace("<p>##### ", "<h5>").replace(" #####</p>", "</h5>")
    html_text = html_text.replace("<p>###### ", "<h6>").replace(" ######</p>", "</h6>")

    # Parse unordered lists and replace with HTML
    html_text = html_text.replace("<ul>\n", "<ul>")
    html_text = html_text.replace("</ul>\n", "</ul>")
    html_text = html_text.replace("<li>", "<li>")
    html_text = html_text.replace("</li>\n", "</li>")

    # Write the HTML output to a file
    with open(output_file, "w") as f:
        f.write(html_text)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Get the Markdown file and output file names from the command line arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML and write to the output file
    convert_markdown_to_html(markdown_file, output_file)

    # Print nothing and exit successfully
    sys.exit(0)

def convert_markdown_to_html(markdown_file, output_file):
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the contents of the Markdown file
    with open(markdown_file, "r") as f:
        markdown_text = f.read()

    # Convert Markdown to HTML
    html_text = markdown.markdown(markdown_text)

    # Parse headings and replace with HTML
    html_text = html_text.replace("<p># ", "<h1>").replace(" #</p>", "</h1>")
    html_text = html_text.replace("<p>## ", "<h2>").replace(" ##</p>", "</h2>")
    html_text = html_text.replace("<p>### ", "<h3>").replace(" ###</p>", "</h3>")
    html_text = html_text.replace("<p>#### ", "<h4>").replace(" ####</p>", "</h4>")
    html_text = html_text.replace("<p>##### ", "<h5>").replace(" #####</p>", "</h5>")
    html_text = html_text.replace("<p>###### ", "<h6>").replace(" ######</p>", "</h6>")

    # Parse unordered lists and replace with HTML
    html_text = html_text.replace("<ul>\n", "<ul>")
    html_text = html_text.replace("</ul>\n", "</ul>")
    html_text = html_text.replace("<li>", "<li>")
    html_text = html_text.replace("</li>\n", "</li>")

    # Parse ordered lists and replace with HTML
    html_text = html_text.replace("<ol>\n", "<ol>")
    html_text = html_text.replace("</ol>\n", "</ol>")
    html_text = html_text.replace("<li>", "<li>")
    html_text = html_text.replace("</li>\n", "</li>")

    # Write the HTML output to a file
    with open(output_file, "w") as f:
        f.write(html_text)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Get the Markdown file and output file names from the command line arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML and write to the output file
    convert_markdown_to_html(markdown_file, output_file)

    # Print nothing and exit successfully
    sys.exit(0)

def convert_markdown_to_html(markdown_file, output_file):
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the contents of the Markdown file
    with open(markdown_file, "r") as f:
        markdown_text = f.read()

    # Convert Markdown to HTML
    html_text = markdown.markdown(markdown_text)

    # Parse headings and replace with HTML
    html_text = html_text.replace("<p># ", "<h1>").replace(" #</p>", "</h1>")
    html_text = html_text.replace("<p>## ", "<h2>").replace(" ##</p>", "</h2>")
    html_text = html_text.replace("<p>### ", "<h3>").replace(" ###</p>", "</h3>")
    html_text = html_text.replace("<p>#### ", "<h4>").replace(" ####</p>", "</h4>")
    html_text = html_text.replace("<p>##### ", "<h5>").replace(" #####</p>", "</h5>")
    html_text = html_text.replace("<p>###### ", "<h6>").replace(" ######</p>", "</h6>")

    # Parse unordered lists and replace with HTML
    html_text = html_text.replace("<ul>\n", "<ul>")
    html_text = html_text.replace("</ul>\n", "</ul>")
    html_text = html_text.replace("<li>", "<li>")
    html_text = html_text.replace("</li>\n", "</li>")

    # Parse ordered lists and replace with HTML
    html_text = html_text.replace("<ol>\n", "<ol>")
    html_text = html_text.replace("</ol>\n", "</ol>")
    html_text = html_text.replace("<li>", "<li>")
    html_text = html_text.replace("</li>\n", "</li>")

    # Parse paragraphs and replace with HTML
    html_text = "<p>" + html_text.replace("\n\n", "</p>\n\n<p>") + "</p>"
    html_text = html_text.replace("<p></p>", "")

    # Write the HTML output to a file
    with open(output_file, "w") as f:
        f.write(html_text)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Get the Markdown file and output file names from the command line arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML and write to the output file
    convert_markdown_to_html(markdown_file, output_file)

    # Print nothing and exit successfully
    sys.exit(0)
    
!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

try:
    with open(markdown_file, "r") as f:
        markdown_text = f.read()
except FileNotFoundError:
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Parse Headings
markdown_text = re.sub(r'^(#+)\s+(.+)$', lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>', markdown_text, flags=re.MULTILINE)

# Parse Unordered Lists
markdown_text = re.sub(r'^\*\s+(.+)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
markdown_text = re.sub(r'^([^\n]*)(\n\*)+', r'<ul>\n\0</ul>\n', markdown_text, flags=re.MULTILINE)

# Parse Ordered Lists
markdown_text = re.sub(r'^\d+\.\s+(.+)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
markdown_text = re.sub(r'^([^\n]*)(\n\d+\.)+', r'<ol>\n\0</ol>\n', markdown_text, flags=re.MULTILINE)

# Parse Paragraphs
markdown_text = re.sub(r'^([^\n]+)\n{2,}', r'<p>\1</p>\n', markdown_text, flags=re.MULTILINE)
markdown_text = re.sub(r'__(.+?)__', r'<em>\1</em>', markdown_text, flags=re.MULTILINE)
markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown_text, flags=re.MULTILINE)

try:
    with open(html_file, "w") as f:
        f.write(markdown_text)
except:
    print(f"Error writing to {html_file}", file=sys.stderr)
    sys.exit(1)

sys.exit(0)

#!/usr/bin/env python3

import sys
import re
import hashlib

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

try:
    with open(markdown_file, "r") as f:
        markdown_text = f.read()
except FileNotFoundError:
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Parse Headings
markdown_text = re.sub(r'^(#+)\s+(.+)$', lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>', markdown_text, flags=re.MULTILINE)

# Parse Unordered Lists
markdown_text = re.sub(r'^\*\s+(.+)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
markdown_text = re.sub(r'^([^\n]*)(\n\*)+', r'<ul>\n\0</ul>\n', markdown_text, flags=re.MULTILINE)

# Parse Ordered Lists
markdown_text = re.sub(r'^\d+\.\s+(.+)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
markdown_text = re.sub(r'^([^\n]*)(\n\d+\.)+', r'<ol>\n\0</ol>\n', markdown_text, flags=re.MULTILINE)

# Parse Paragraphs
markdown_text = re.sub(r'^([^\n]+)\n{2,}', r'<p>\1</p>\n', markdown_text, flags=re.MULTILINE)

# Parse Bold
markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown_text, flags=re.MULTILINE)

# Parse MD5
markdown_text = re.sub(r'\[\[(.+?)\]\]', lambda m: hashlib.md5(m.group(1).encode('utf-8')).hexdigest(), markdown_text)

# Parse Remove C
markdown_text = re.sub(r'\(\((.+?)\)\)', lambda m: m.group(1).replace('c', '').replace('C', ''), markdown_text)

try:
    with open(html_file, "w") as f:
        f.write(markdown_text)
except:
    print(f"Error writing to {html_file}", file=sys.stderr)
    sys.exit(1)

sys.exit(0)