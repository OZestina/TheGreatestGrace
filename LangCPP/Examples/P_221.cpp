//ShallowCopyError.cpp

#include <iostream>
#include <cstring>
using namespace std;

class Person
{
private:
	char *name;
	int age;
public:
	Person (char *myname, int myage)
	{
		name = new char[strlen(myname)+1];
		strcpy(name, myname);
		age = myage;
	}
	void ShowPersonInfo() const
	{
		cout<<"Name: "<<name<<endl;
		cout<<"Age: "<<age<<endl;
	}
	~Person()
	{
		delete []name;
		cout<<"called destructor!"<<endl;
	}
};

int main(void)
{
	Person man1("LDW", 20);
	Person man2 = man1;
	man1.ShowPersonInfo();
	man2.ShowPersonInfo();
	return 0;
}
