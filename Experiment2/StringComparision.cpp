#include<bits/stdc++.h>
#include<iostream>
#include<map>
#include<fstream>
#include<algorithm>
#define ll long long int
using namespace std;
map<string,int> m;
set<string> student_notes;
set<string> teacher_notes;

int main()
{
//Read the strings from the index file and put into hashmap
ifstream fin;
fin.open("Result(Mam).txt");
string line;
cout<<"Outside the while loop"<<endl;
int count =0;

while(getline(fin,line))
{
cout<<line<<endl;
cout<<"Breaking the line into different string and then puttiing them into hash maps"<<endl;
int i =0;
while(i<line.length())
{
 string temp;
while(line[i]!=' ')
{
temp = temp + line[i];
i++;
}
count++;

//cout<<"made string "<<count<<endl;
cout<<"Putting into hashmap"<<endl;
cout<<temp<<endl;
m[temp]=1;
teacher_notes.insert(temp);
string another_temp;
another_temp = temp;
int add = 26 + temp[0];
another_temp = (string)add+ another_temp;
i++;
}
}
cout<<"------------------------------------Hash Map Created-----------------------------"<<endl;
fin.close();
cout<<"Closed index file"<<endl;
cout<<"Opening the Notes file"<<endl;
ifstream fin2;
fin2.open("Results(Aditya).txt");
string line2;
getline(fin2,line2);
cout<<line2<<endl;
cout<<"Breaking the line into different string and searching"<<endl;
cout<<line2[0]<<endl;
int j=0;
int count2 =0;
int match =0;
while(j<line2.length())
{
string temp2;
while(line2[j]!=',')
{

temp2 = temp2 + line2[j];
j++;
}
cout<<temp2<<endl;
student_notes.insert(temp2);
count2++;

if(m[temp2]!=0){
cout<<"Found"<<endl;
match++;
//s.insert(temp2);
}else
cout<<"Not Found"<<endl;
j++;
}
cout<<"Total String for Index file found"<<" "<<count<<endl;
cout<<"Total String for Notes File found"<<" "<<count2<<endl;
cout<<"Matches Found"<<" "<<match<<endl;
//cout<<"Distinct Matches Found"<<" "<<s.size()<<" "<<endl;
cout<<endl;
//std::set<std::string>::iterator it= s.begin();

// Iterate till the end of set
/*while (it != s.end())
{
	// Print the element
	std::cout << (*it) << " , ";
	//Increment the iterator
	it++;
}
*/
cout<<"Finding the difference between the sets"<<endl;

set<string> result;
set_difference(teacher_notes.begin(),teacher_notes.end(),student_notes.begin(),student_notes.end(),std::insert_iterator<set<string> >(result, result.end()));
std::set<std::string>::iterator it= result.begin();
cout<<"Total topics in Teachers-Student Notes ----------------"<<result.size()<<"\n";
while(it!=result.end())
{
  cout<<(*it)<<" , ";
  it++;
}
}
