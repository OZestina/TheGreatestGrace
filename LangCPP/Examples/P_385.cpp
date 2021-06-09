//MultiInheri2.cpp

#include <iostream>
using namespace std;

class BaseOne
{
public:
	void SimpleFunc() { cout<<"BaseOne"<<endl; }
};

class BaseTwo
{
public:
	void SimpleFunc() { cout<<"BaseTwo"<<endl; }
};

class MultiDerived: public BaseOne, protected BaseTwo
{
public:
	void Complex()
	{
		BaseOne::SimpleFunc();
		BaseTwo::SimpleFunc();
	}
};

int main(void)
{
	MultiDerived mdr;
	mdr.Complex();
	return 0;
}
