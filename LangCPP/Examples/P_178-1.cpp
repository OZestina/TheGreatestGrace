//Rectangle.cpp

#include <iostream>
#include "Rectangle.h"
using namespace std;


Rectangle::Rectangle(const int &x1, const int &y1, const int &x2, const int &y2):upLeft(x1, y1), lowRight(x2, y2)
{
	//empty
}

void Rectangle::ShowRecInfo() const
{
	cout<<"upper left: ["<<upLeft.GetX()<<", ";
	cout<<upLeft.GetY()<<"]"<<endl;
	cout<<"lower right: ["<<lowRight.GetX()<<", ";
	cout<<lowRight.GetY()<<"]"<<endl<<endl;
}
