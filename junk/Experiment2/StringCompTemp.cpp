#include<bits/stdc++.h>
#include<iostream>
#include<fstream>
using namespace std;
map<string,int> temp;
int main()
{
  ifstream fin;
  fin.open("Results(Mam)(Noun).txt");
  string line;
if(fin.is_open())
  while(getline(fin,line))
  cout<<line<<endl;
else
cout<<"Unable to open file";
}
