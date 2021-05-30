//RectangleFaultFind.cpp

#include <iostream>
#include "Point.h"
#include "Rectangle.h"
using namespace std;

int main(void)
{
	Point pos1;
	if (!pos1.InitMembers(-2, 4))
		cout<<"Initiate failed"<<endl;
	if (!pos1.InitMembers(2, 4))
		cout<<"Initiate failed"<<endl;

	Point pos2;
	if (!pos2.InitMembers(5, 9))
		cout<<"Initiate failed"<<endl;
	
	Rectangle rec;
	if(!rec.InitMembers(pos2, pos1))
		cout<<"Rectangle initiate failed"<<endl;
	if(!rec.InitMembers(pos1, pos2))
		cout<<"Rectangle initiate failed"<<endl;

	rec.ShowRecInfo();

	return 0;
}
