#!/usr/bin/env python3

import sys
import os
import re
import hashlib


def parse_heading(line):
    # Regex to match the heading syntax and extract the level and title
    match = re.match(r'^(#+)\s(.*)$', line)
    if match:
        level = len(match.group(1))
        title = match.group(2)
        return f'<h{level}>{title}</h{level}>'
    else:
        return line


def parse_unordered_list(lines):
    # Wrap each item in an <li> tag
    list_items = [f'<li>{line[2:].strip()}</li>' for line in lines if line.startswith('- ')]
    # Join the items with line breaks and wrap them in a <ul> tag
    return '<ul>\n{}\n</ul>'.format('\n'.join(list_items))


def parse_ordered_list(lines):
    # Wrap each item in an <li> tag
    list_items = [f'<li>{line[2:].strip()}</li>' for line in lines if line.startswith('* ')]
    # Join the items with line breaks and wrap them in an <ol> tag
    return '<ol>\n{}\n</ol>'.format('\n'.join(list_items))


def parse_paragraph(lines):
    # Join the lines with line breaks, wrap them in a <p> tag, and replace newlines with <br> tags
    return '<p>\n{}\n</p>'.format('\n'.join(lines).replace('\n', '<br />\n'))


def parse_bold(line):
    # Replace **text** and __text__ with <b>text</b> and <em>text</em>, respectively
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)
    return line


def parse_md5(line):
    # Replace [[text]] with the MD5 hash of the lowercase text
    match = re.match(r'^\[\[(.*)\]\]$', line)
    if match:
        text = match.group(1).lower().encode('utf-8')
        return hashlib.md5(text).hexdigest()
    else:
        return line


def parse_remove_c(line):
    # Replace ((text)) with the text with all instances of 'c' (case-insensitive) removed
    match = re.match(r'^\(\((.*)\)\)$', line)
    if match:
        text = match.group(1).replace('c', '').replace('C', '')
        return text
    else:
        return line


def parse_markdown(filename):
    with open(filename) as f:
        lines = f.readlines()

    # Split the lines into blocks separated by empty lines
    blocks = [[]]
    for line in lines:
        if line.strip():
            blocks[-1].append(line)
        else:
            blocks.append([])

    # Parse each block based on its syntax
    output = []
    for block in blocks:
        if block[0].startswith('#'):
            # Heading syntax
            output.append(parse_heading(block[0]))
        elif any(line.startswith('- ') for line in block):
            # Unordered list syntax
            output.append(parse_unordered_list(block))
        elif any(line.startswith('* ') for line in block):
            # Ordered list syntax
            output.append(parse_ordered_list(block))
        elif any(line.startswith(('**', '__')) for line in block):
            # Bold syntax
            output.append(parse
