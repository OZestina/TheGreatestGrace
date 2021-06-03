#include <iostream>
using namespace std;

class Point
{
private:
	int xpos, ypos;
public:
	Point (int x, int y): xpos(x), ypos(y) {}
	void ShowPointInfo() const
	{
		cout<<"["<<xpos<<", "<<ypos<<"]"<<endl;
	}
};

class Circle
{
private:
	Point pos;
	int rad;
public:
	Circle (int x, int y, int r): pos(x,y), rad(r)
	{
		//empty
	}
	void ShowCircleInfo() const
	{
		cout<<"원의 중심: ";
		pos.ShowPointInfo();
		cout<<"원의 반지름: "<<rad<<endl;
	}
};

class Ring
{
private:
	Circle c1;
	Circle c2;
public:
	Ring(int x1, int y1, int r1, int x2, int y2, int r2): c1(x1, y1, r1), c2(x2, y2, r2)
	{
		//empty
	}
	void ShowRingInfo() const
	{
		cout<<"[ First Circle ]"<<endl;
		c1.ShowCircleInfo();
		cout<<"[ Second Circle ]"<<endl;
		c2.ShowCircleInfo();
	}
};

int main(void)
{
	Ring ring(1,1,4,2,2,9);
	ring.ShowRingInfo();

	return 0;
}
