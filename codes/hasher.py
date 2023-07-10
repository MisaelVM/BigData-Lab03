#!/usr/bin/python3

import sys
import hashlib

text = sys.argv[1]
hash_object = hashlib.sha1(text.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig.upper())
