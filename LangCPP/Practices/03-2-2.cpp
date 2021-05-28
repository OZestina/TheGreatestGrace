#include <iostream>
#include <cstring>
using namespace std;

const int STR_LEN = 20;

class Printer
{
private:
	char memory[STR_LEN];

public:
	void SetString(char* str);
	void ShowString();
};

void Printer::SetString(char* str)
{
	strcpy(memory, str);
}

void Printer::ShowString()
{
	cout<<memory<<endl;
}

int main(void)
{
	Printer pnt;
	pnt.SetString("Hello world!");
	pnt.ShowString();

	pnt.SetString("I love C++");
	pnt.ShowString();

	return 0;
}
