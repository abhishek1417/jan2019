#!/usr/bim/python3

import nltk
from nltk import word_tokenize
sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print (tokens)

