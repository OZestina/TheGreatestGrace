//ReferenceAttribute.cpp

#include <iostream>
using namespace std;

class First
{
public:
	void FirstFunc() { cout<<"FirstFunc()"<<endl; }
	virtual void SimpleFunc() { cout<<"First's SimpleFunc()"<<endl; }
};

class Second: public First
{
public:
	void SecondtFunc() { cout<<"2ndFunc()"<<endl; }
	virtual void SimpleFunc() { cout<<"Second's SimpleFunc()"<<endl; }
};

class Third: public Second
{
public:
	void ThirdFunc() { cout<<"3rdFunc()"<<endl; }
	virtual void SimpleFunc() { cout<<"3rd's SimpleFunc()"<<endl; }
};

int main(void)
{
	Third obj;
	obj.FirstFunc();
	obj.SecondtFunc();
	obj.ThirdFunc();
	obj.SimpleFunc();

	Second & sref = obj;
	sref.FirstFunc();
	sref.SecondtFunc();
	sref.SimpleFunc();

	First & fref = obj;
	fref.FirstFunc();
	fref.SimpleFunc();

	return 0;
}
