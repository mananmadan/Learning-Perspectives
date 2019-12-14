#!/usr/bin/python
import nltk
import textblob

opentext = open("Sample.txt")
readtext = opentext.read()
blob = textblob.TextBlob(readtext)
#open file for writing
openfile = open("Results.txt","w")
for i in blob.noun_phrases:
 openfile.write(i)
 openfile.write(" ")
 openfile.write(",")

openfile.close()

print(blob.noun_phrases)
