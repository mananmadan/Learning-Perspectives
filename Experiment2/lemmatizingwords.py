#!/usr/bin/python
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
opentext = open("Results(Mam)(Noun).txt")
readtext = opentext.read()
lines = readtext
openfile = open("Results(Lematized).txt","w")
tokenized = nltk.word_tokenize(lines)
print tokenized

for i in tokenized:
 print(i)
 word = lemmatizer.lemmatize(i)
 openfile.write(word)
 #openfile.write(",")
openfile.close()
