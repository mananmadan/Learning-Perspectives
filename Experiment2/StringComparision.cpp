#include<bits/stdc++.h>
#include<iostream>
#include<map>
#include<fstream>
#include<algorithm>
#define ll long long int
using namespace std;
map<string,int> m;
set<string> student_notes;
vector<string> teacher_notes;
set<string> teacher_notes_set;
int main()
{
//Read the strings from the index file and put into hashmap
ifstream fin;
fin.open("Results(Mam)(Noun).txt");
string line;
cout<<"Outside the while loop"<<endl;
int count =0;

getline(fin,line);
cout<<line<<endl;

cout<<"Breaking the line into different string and then puttiing them into hash maps"<<endl;
int i =0;
while(i<line.length())
{
 string temp;
while(line[i]!=',')
{
temp = temp + line[i];
i++;
}
count++;

//cout<<"made string "<<count<<endl;
cout<<"Putting into hashmap"<<endl;
cout<<temp<<endl;
transform(temp.begin(), temp.end(), temp.begin(), ::tolower);

m[temp]=1;

teacher_notes.push_back(temp);
teacher_notes_set.insert(temp);
i++;
}

cout<<"------------------------------------Hash Map Created-----------------------------"<<endl;
int count_lematized=0;
fin.close();
//ifstream fin;
fin.open("Results(Lematized).txt");
string line4;
cout<<"Outside the while loop"<<endl;
count =0;

getline(fin,line4);
cout<<line4<<endl;

cout<<"Breaking the line into different string and then puttiing them into hash maps"<<endl;
i =0;
while(i<line4.length())
{
 string temp;
while(line4[i]!=',')
{
temp = temp + line4[i];
i++;
}
count++;

//cout<<"made string "<<count<<endl;
cout<<"Putting into hashmap"<<endl;
cout<<temp<<endl;
transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
count_lematized++;
m[temp]=1;
teacher_notes.push_back(temp);
i++;
}

cout<<"------------------------------------Hash Map Created-----------------------------"<<endl;
int count_stemmed=0;
fin.close();

//ifstream fin;
fin.open("Results(Stemmed).txt");
string line3;
cout<<"Outside the while loop"<<endl;
 count =0;

getline(fin,line3);
cout<<line3<<endl;

cout<<"Breaking the line into different string and then puttiing them into hash maps"<<endl;
 i =0;
while(i<line3.length())
{
 string temp;
while(line3[i]!=',')
{
temp = temp + line3[i];
i++;
}
count++;

//cout<<"made string "<<count<<endl;
cout<<"Putting into hashmap"<<endl;
cout<<temp<<endl;
transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
m[temp]=1;
teacher_notes.push_back(temp);
count_stemmed++;
i++;
}

cout<<"------------------------------------Hash Map Created-----------------------------"<<endl;
fin.close();



cout<<"Closed index file"<<endl;
cout<<"Opening the Notes file"<<endl;
ifstream fin2;
fin2.open("Results(Manan)(Noun).txt");
string line2;
getline(fin2,line2);
cout<<line2<<endl;
cout<<"Breaking the line into different string and searching"<<endl;
cout<<line2[0]<<endl;
int j=0;
int count2 =0;
int match =0;
set<string> result;
set<string> matches_found;
while(j<line2.length())
{
string temp2;
while(line2[j]!=',')
{

temp2 = temp2 + line2[j];
j++;
}
cout<<temp2<<endl;
transform(temp2.begin(), temp2.end(), temp2.begin(), ::tolower);
student_notes.insert(temp2);
count2++;

if(m[temp2]!=0){
cout<<"Found"<<endl;
match++;
matches_found.insert(temp2);
}else{
cout<<"Not Found"<<endl;
result.insert(temp2);
}
j++;
}

cout<<"Total String for Index file found"<<" "<<count<<endl;
//cout<<count_stemmed<<" "<<count_lematized<<"\n";
cout<<"Total topic from teacher"<<" "<<teacher_notes_set.size()<<"\n";
cout<<"Total String for Notes File found"<<" "<<count2<<endl;
cout<<"Total topics from student"<<" "<<student_notes.size()<<"\n";
cout<<"Matches Found"<<" "<<matches_found.size()<<endl;
//cout<<"different topics Found"<<" "<<result.size()<<" "<<endl;
std::set<std::string>::iterator it= teacher_notes_set.begin();
int temp_f=0;

// Iterate till the end of set
set<string> finalresult;
int count_temp=0;
while (it != teacher_notes_set.end())
{
	// Print the element
count_temp++;

	//Increment the iterator
  temp_f=0;
std::set<std::string>::iterator it2= matches_found.begin();

  while (it2 != matches_found.end())
  {
    if(*it2 == *it)
    temp_f=1;

    it2++;
  }
   if(temp_f!=1)
  { finalresult.insert(*it);
   //cout<<*it<<":::";
  }
  it++;
}

cout<<"Different topics found"<<finalresult.size()<<" "<<count_temp<<"\n";
std::set<std::string>::iterator it3= finalresult.begin();
while(it3!=finalresult.end())
{cout<<(*it3)<<" ";
it3++;
}
cout<<"\n";
//write the words to the file teacher set
std::set<std::string>::iterator it_t= teacher_notes_set.begin();
ofstream outfile;
outfile.open("teacher_notes_set.txt");
while(it_t != teacher_notes_set.end())
{
  outfile<<*it_t<<" ";it_t++;
}
// write to word to the file gaurav set
ofstream outfile2;
outfile2.open("manan_notes_set.txt");
std::set<std::string>::iterator it_f= student_notes.begin();
while(it_f != student_notes.end())
{
  outfile2<<*it_f<<" ";it_f++;
}

}
