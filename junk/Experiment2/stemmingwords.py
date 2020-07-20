#!/usr/bin/python
import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
opentext = open("Results(Mam)(Noun).txt")
readtext = opentext.read()
lines = readtext
openfile = open("Results(Stemmed).txt","w")
tokenized = nltk.word_tokenize(lines)
print tokenized

for i in tokenized:
 print(i)
 word = ps.stem(i)
 openfile.write(word)
 #openfile.write(",")
openfile.close()
