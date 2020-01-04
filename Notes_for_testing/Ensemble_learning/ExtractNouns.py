#!/usr/bin/python
import nltk
import textblob

opentext = open("Notes.txt")
readtext = opentext.read()
lines = readtext
is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

print nouns

openfile = open("Results(Keldec)(Noun).txt","w")
for i in nouns:
    openfile.write(i)
    openfile.write(",")
print("Done")
blob = textblob.TextBlob(readtext)
#open file for writing
openfile = open("Results.txt","w")
for i in blob.noun_phrases:
 openfile.write(i)
 openfile.write(" ")
 openfile.write(",")

openfile.close()

print(blob.noun_phrases)
