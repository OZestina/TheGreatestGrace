#include <iostream>

int main(void)
{
	const int num=12;
	const int * ptr = &num;
	const int *(&ref) = ptr;

	std::cout<<*ptr<<std::endl;
	std::cout<<*ref<<std::endl;

	
	return 0;
}
