#!/usr/bin/python
import nltk
import re
import textblob

opentext = open("Notes.txt")
readtext = opentext.read()
#print(readtext)

lines = readtext
#print(type(lines))

print(lines)

is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff

tokenized = nltk.word_tokenize(lines)

print(tokenized)
#tokens_without_punct_python = [t for t in tokenized if t not in string.punctuation]
#print(tokens_without_punct_python)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

print nouns

openfile = open("Results(Encryption)(Noun).txt","w")
for i in nouns:
    openfile.write(i)
    openfile.write(",")
print("Done")
blob = textblob.TextBlob(readtext)
#open file for writing
list=[]
openfile = open("Results(Encryption)(noun_phrases).txt","w")
for i in blob.noun_phrases:
 #openfile.write(" " ")
 openfile.write(i.decode('utf-8'))
 list.append(i.decode('utf-8'))
 openfile.write(" ")
 openfile.write(",")

openfile.close()

print(list)
