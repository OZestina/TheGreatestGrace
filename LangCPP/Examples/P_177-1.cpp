//Pointer.cpp

#include <iostream>
#include "Point.h"
using namespace std;

Point::Point (const int &xpos, const int &ypos)
{
	if(xpos<0 || ypos<0)
	{
		cout<<"error: point out of range"<<endl;
		return;
	}
	x=xpos;
	y=ypos;
}

int Point::GetX() const
{
	return x;
}

int Point::GetY() const
{
	return y;
}

bool Point::SetX(int xpos)
{
	if(0>xpos || xpos>100)
	{
		cout<<"error: point out of range"<<endl;
		return false;
	}
	x=xpos;
	return true;
}

bool Point::SetY(int ypos)
{
	if(0>ypos || ypos>100)
	{
		cout<<"error: point out of range"<<endl;
		return false;
	}
	y=ypos;
	return true;
}
