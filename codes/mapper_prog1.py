#!/usr/bin/python3
"""mapper.py"""

import sys
for line in sys.stdin:
    line = line.strip()
    document = line.split()
    document_id = document[0]
    for i in range(1, len(document) - 1):
        print("%s %s %s" % (document[i], document[i+1], document_id))
