//ReinterpretCasting.cpp

#include <iostream>
using namespace std;

int main(void)
{
	int num=0x010203;
	cout<<num<<endl;
	char * ptr = reinterpret_cast<char*>(&num);

	for(int i=0; i<sizeof(num); i++)
		cout<< static_cast<int>(*(ptr+i)) <<endl;

	cout<<num<<endl;

	return 0;
}
