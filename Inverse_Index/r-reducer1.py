#!/usr/bin/env python

import sys

current_word=None
url_count=[]
word = None

for line in sys.stdin:
    line = line.strip()
    try:
		word,url=line.split('\t',1)
    except ValueError:
		continue
    if current_word == word:
        url_count.append(url)
    else:
        if current_word:
            print '%s\t%s' % (current_word, list(set(url_count)))
        url_count=[]
        url_count.append(url)
        current_word = word

if current_word == word:
    print '%s\t%s' % (current_word, list(set(url_count)))
