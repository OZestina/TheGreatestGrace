//StringIO.cpp

#include <iostream>

int main(void)
{
	char name[100];
	char lang[200];

	std::cout<<"What is your name? ";
	std::cin>>name;

	std::cout<<"What is your favorite programming language? ";
	std::cin>>lang;

	std::cout<<"My name is "<<name<<".\n";
	std::cout<<"My favorite programming language is "<<lang<<"."<<std::endl;
	return 0;
}
