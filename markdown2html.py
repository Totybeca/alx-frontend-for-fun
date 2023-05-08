#!/usr/bin/python3
'''
This script codes the markdown to HTML
'''
import sys
import os
import re

if __name__ == '__main__':

    # Test if the number of arguments passed is 2
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    # Store the arguments into variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check that the markdown file exist and it is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    ulvli = ''
    olvli = ''    

    readfile = open(inputvfile, 'r')
    writefile = open(outputvfile, 'w')
    Lines = readfile.readlines()

    for line in Lines:
        ct = line.count('#')
        if ct:
            line = line.replace('#', '')
            line = line.strip()
            writefile.write(f'<h{ct}>{line}</h{ct}>\n')

        if(line.find('v') >= 0):
            line = line.replace('v', '')
            line = line.strip()
            ulvli += f'<li>{line}</li>\n'
        
        if(line.find('*') >= 0):
            line = line.replace('*', '')
            line = line.strip()
            olvli += f'<li>{line}</li>\n'

    if ulvli:
         writefile.write(f'<ul>\n{ulvli}</ul>')

    if olvli:
         writefile.write(f'<ol>\n{olvli}</ol>')

    readfile.close()
    writefile.close()
