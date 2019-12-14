#include<bits/stdc++.h>
#include<iostream>
#include<map>
#include<fstream>
#define ll long long int
using namespace std;
map<string,int> m;
set<string> s;


int main()
{
//Read the strings from the index file and put into hashmap
ifstream fin; 
fin.open("Results(Index).txt");
string line;
cout<<"Outside the while loop"<<endl;
getline(fin,line);
cout<<line<<endl;
cout<<"Breaking the line into different string and then puttiing them into hash maps"<<endl;
int i =0;
int count =0;
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
m[temp]=1;
i++;
}

cout<<"------------------------------------Hash Map Created-----------------------------"<<endl;
fin.close();
cout<<"Closed index file"<<endl;
cout<<"Opening the Notes file"<<endl;
ifstream fin2;
fin2.open("Results(Networking_NCERT).txt");
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
count2++;

if(m[temp2]!=0){
cout<<"Found"<<endl;
match++;
s.insert(temp2);
}else
cout<<"Not Found"<<endl;
j++;
}
cout<<"Total String for Index file found"<<" "<<count<<endl;
cout<<"Total String for Notes File found"<<" "<<count2<<endl;
cout<<"Matches Found"<<" "<<match<<endl;
cout<<"Distinct Matches Found"<<" "<<s.size()<<" "<<endl;


}
