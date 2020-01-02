#!/usr/bin/python
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
student = []
teacher = []
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
opentext = open("teacher_notes_set.txt")
opentext2 = open("manan_notes_set.txt")
#print(opentext)
readtext = opentext.read()
#print(readtext)
readtext2 = opentext2.read()
tokenized_teacher = nltk.word_tokenize(readtext)
tokenized_student = nltk.word_tokenize(readtext2)
#print(tokenized_teacher)
#print(tokenized_student)
flag = 0
#print(type(tokenized_student[0]))
result = []
mismatch = []
for i in tokenized_teacher:
    for j in tokenized_student:
       if i == j or ps.stem(i) == j.decode('utf-8') or lemmatizer.lemmatize(i) == j.decode('utf-8') :
         flag = 1
    if flag == 0:
     mismatch.append(i)
    if flag == 1:
     flag = 0
     result.append(i)
print(len(tokenized_teacher))
print(len(tokenized_student))

print(len(mismatch))
print(mismatch)
print(len(result))
