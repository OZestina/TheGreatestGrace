//ObjPtrArr.cpp


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
	Person * parr[3];
	char namestr[100];
	int age;
	
	for (int i=0; i<3; i++)
	{
		cout<<"Name: ";
		cin>>namestr;
		cout<<"Age: ";
		cin>>age;
	/*	len = strlen(namestr)+1;
		strptr = new char[len];
		strcpy(strptr, namestr);*/
		parr[i] = new Person(namestr, age);
	}

	parr[0]->ShowPersonInfo();
	parr[1]->ShowPersonInfo();
	parr[2]->ShowPersonInfo();
	delete parr[0];
	delete parr[1];
	delete parr[2];
	return 0;
}
