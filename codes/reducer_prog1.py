#!/usr/bin/python3
"""reducer.py"""

import sys
import bisect
bigrames_list = []

for line in sys.stdin:
    line = line.strip()
    bisect.insort(bigrames_list, line)

documents_occurence = {}
last_word1, last_word2, last_doc_id = bigrames_list[0].split()
documents_occurence[last_doc_id] = 1

word1, word2, doc_id = None, None, None

for bigrame_str in bigrames_list[1:]:
    word1, word2, doc_id = bigrame_str.split()

    if word1 == last_word1 and word2 == last_word2:
        if doc_id in documents_occurence:
            documents_occurence[doc_id] += 1
        else:
            documents_occurence[doc_id] = 1
    else:
        if last_word1:
            occurences = [
                "%s:%s" % (doc, count) for doc, count in documents_occurence.items()
            ]
            result = " ".join(occurences)
            print("%s %s %s" % (last_word1, last_word2, result))
        last_word1 = word1
        last_word2 = word2
        las_doc_id = doc_id
        documents_occurence = {}
        documents_occurence[las_doc_id] = 1

if word1 == last_word1 and word2 == last_word2:
    occurences = [
        "%s:%s" % (doc, count) for doc, count in documents_occurence.items()
    ]
    result = " ".join(occurences)
    print("%s %s %s" % (last_word1, last_word2, result))
