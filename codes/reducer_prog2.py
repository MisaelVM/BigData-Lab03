#!/usr/bin/python3

import sys

# Read input from standard input
for line in sys.stdin:
    # Remove leading/trailing whitespaces and split the line
    line = line.strip()
    original_pw, metadata = line.split('\t')

    # Process the search result as desired
    print("%s\t%s" % (original_pw, metadata))
