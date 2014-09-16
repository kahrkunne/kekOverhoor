#!/usr/bin/python2
import argparse, re

def parse(filename):
   """Parse a word list file. Returns a dictionary"""

    # Get the data from the file
    with open(filename, 'r') as file:
        unstrippedData = file.read()
    
    # Remove blank lines from unstrippedData, put them in data
    data = ''
    for line in unstrippedData.split('\n'):
        if line.strip() != '':
            data += line.replace("\r","") + '\n'
    
    # Define the regular expression for parsing the files
    parseRegex = re.compile(r"^FIB\t([^\t\n]+)\t([^\t\n]+)$")
    
    # Parse the word list, and turn it into a dictionary
    words = {}
    for line in data.split('\n'):
        match = parseRegex.match(line)
        if match:
            words[match.group(1)] = match.group(2)
    
    return words

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='filename parser')
    parser.add_argument('filename', help="File to parse")
    args = parser.parse_args()
    print parse(args.filename)
