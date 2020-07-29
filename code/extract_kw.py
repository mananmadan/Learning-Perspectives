#!/usr/bin/python
import nltk
import textblob

def extract_keywords(readfile,writefile):
 opentext = open(readfile)
 readtext = opentext.read()
 lines = readtext
 is_noun = lambda pos: pos[:2] == 'NNPS'
 tokenized = nltk.word_tokenize(lines)
 nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
 openfile = open(writefile,"w")
 blob = textblob.TextBlob(readtext)
 count = 0
 for i in blob.noun_phrases:
  count = count + 1
  openfile.write(i)
  openfile.write(" ")
  openfile.write(",")

 openfile.close()
 return count
 print("total keywords found",count)


