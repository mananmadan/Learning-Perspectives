# Learning-Perspectives


Project to analyse the Notes of different students in Class and figure out different Perspectives of Learning of Students.
# Main Idea:
First Extract Nouns from the notes of students using NLP and then compare them to the index formed using teachers note or book 
# Implementation Progress
1. Done- extracting all the noun - phrases from a sample text to check working of ntlk.(available in testing_tools folder)
2. Done -To write the Extracted Nouns to a text file to apply further algorithms on the file.(results.txt file also in testing_tools folders)
3. Done - Finding a book to compare 
4. Done - Extracting NOUNS out of the Networking Notes.
# Ultimate Process
1>I calculated the Nouns from the NCERT Text using nltk.

2>Then stored them into a text file (Result file in Experiment1 Folder).

3>Then I repeated the same process for Index file which is basically index of the book sumitra arora

4>Now after that we stored all the Nouns of Index File into a Hash Map

5>Now for every term in the Notes file we checked if there exixts a word in the Hash Map .

6>If such a word exists then we increase the count of match variable and store that value into a set

7>Now the set of size is basically the distinct topics which are a part of Notes and the Index of the book,
which means that it is covered by both of them

8>Using this Example we found that The Book Sumitra Arora Has 30 More topics covered as compared to NCERT.

We get the result in the form

Total String for Index file found 91

Total String for Notes File found 2059

Matches Found 324

Distinct Matches Found 61

Here the Matched found indicate that this many values matched , but out of them 61 topics were same in both Index and Notes.


