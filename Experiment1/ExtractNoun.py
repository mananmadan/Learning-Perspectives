#!/usr/bin/python
import nltk
import textblob
import sys
import io
reload(sys)
sys.setdefaultencoding('utf-8')

#opentext = open("Networking_Student1.txt")
opentext = io.open("Index.txt", "r", encoding='utf-8') 
readtext = opentext.read()
blob = textblob.TextBlob(readtext)
#open file for writing
openfile = io.open("Results(Index).txt","w",encoding='utf-8')
for i in blob.noun_phrases:
 openfile.write(i)
 openfile.write(((" ").decode('utf-8')))
 openfile.write(((",").decode('utf-8')))

openfile.close()

print(blob.noun_phrases)
