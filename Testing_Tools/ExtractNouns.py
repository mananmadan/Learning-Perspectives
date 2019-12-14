#!/usr/bin/python
import nltk
import textblob

opentext = open("Sample.txt")
readtext = opentext.read()
blob = textblob.TextBlob(readtext)
print(blob.noun_phrases)
