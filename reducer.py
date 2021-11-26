#!/usr/bin/env python3
# -*-coding:utf-8 -*
from operator import itemgetter
import sys
word = None
word2count={}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
        word2count[word]=word2count.get(word,0)+count
    except ValueError:
        pass   
for word,count in word2count.items():
    print ('{0}\t{1}'.format(word,count))
