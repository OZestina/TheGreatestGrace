//ReThrow.cpp

#include <iostream>
using namespace std;

void Divide(int num1, int num2)
{
	try
	{
		if(num2==0)
			throw 0;
		cout<<"몫: "<<num1/num2<<endl;
		cout<<"나머지: "<<num1%num2<<endl;
	}
	catch(int expn)
	{
		cout<<"first catch"<<endl;
		throw;	//예외를 다시 던진다
	}
}

int main(void)
{
	try
	{
		Divide (9,2);
		Divide (4,0);
	}
	catch(int expn)
	{
		cout<<"Second catch"<<endl;
	}
	return 0;
}
