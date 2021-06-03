//ObjArr.cpp

#include <iostream>
#include <cstring>
using namespace std;

class Person
{
private:
	char * name;
	int age;
public:
	Person(char *myname, int myage)
	{
		name = new char(strlen(myname)+1);
		strcpy(name, myname);
		age=myage;
	}
	Person()
	{
		name=NULL;
		age = 0;
		cout<<"Called Person()"<<endl;
	}
	void SetPersonInfo(char *myname, int myage)
	{
		name=myname;
		age = myage;
	}
	void ShowPersonInfo() const
	{
		cout<<"Name: "<<name<<", ";
		cout<<"Age: "<<age<<endl;
	}
	~Person()
	{
		delete []name;
		cout<<"Called destructor!"<<endl;
	}
};

int main(void)
{
	Person parr[3];
	char namestr[100];
	char * strptr;
	int age;
	int len;

	for (int i=0; i<3; i++)
	{
		cout<<"Name: ";
		cin>>namestr;
		cout<<"Age: ";
		cin>>age;
		len = strlen(namestr)+1;
		strptr = new char[len];
		strcpy(strptr, namestr);
		parr[i].SetPersonInfo(strptr, age);
	}

	parr[0].ShowPersonInfo();
	parr[1].ShowPersonInfo();
	parr[2].ShowPersonInfo();
	return 0;
}
