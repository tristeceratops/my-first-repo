#!/usr/bin/python3
import sys
import urllib.request

try:
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
except Exception:
    print("Request failed")