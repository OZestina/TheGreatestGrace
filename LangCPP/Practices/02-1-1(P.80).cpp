#include <iostream>
using namespace std;

void Increase1(int &ref)
{
	ref += 1;
}

void SignChange(int &ref)
{
	ref *= -1;
}

int main(void)
{
	int num = 10;
	cout<<num<<endl;
	Increase1(num);
	cout<<num<<endl;
	Increase1(num);
	cout<<num<<endl;
	SignChange(num);
	cout<<num<<endl;
	return 0;
}
