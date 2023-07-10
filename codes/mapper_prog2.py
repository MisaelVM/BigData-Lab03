#!/usr/bin/python3

import sys

search_term = str(sys.argv[1])
original_search_term = str(sys.argv[2])

# Read input from standard input
for line in sys.stdin:
    # Remove leading/trailing whitespaces and split the line
    line = line.strip()
    data = line.split(':')

    # Extract the password hash and associated metadata
    password_hash = data[0]
    metadata = data[1]

    # Check if the password hash matches the search term
    if password_hash == search_term:
        # Emit the password hash as the key and metadata as the value
        print("%s\t%s" % (original_search_term, metadata))
        sys.exit(0)
print("%s\t%s" % (password_hash, 0))
