#include <iostream>
using namespace std;

class Point
{
private:
	int xpos, ypos;
public:
	void Init(int x, int y)
	{
		xpos = x;
		ypos = y;
	}
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
	void Init(int x, int y, int r)
	{
		pos.Init(x, y);
		rad = r;
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
	void Init(int x1, int y1, int r1, int x2, int y2, int r2)
	{
		c1.Init(x1, y1, r1);
		c2.Init(x2, y2, r2);
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
	Ring ring;
	ring.Init(1,1,4,2,2,9);
	ring.ShowRingInfo();

	return 0;
}
