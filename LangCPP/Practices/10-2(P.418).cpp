#include <iostream>
using namespace std;

class Point
{
private:
	int xpos, ypos;
public:
	Point(int x=0, int y=0): xpos(x), ypos(y)
	{ }
	void ShowPosition() const
	{
		cout<<"["<<xpos<<", "<<ypos<<"]"<<endl;
	}
	Point& operator++()
	{
		xpos += 1;
		ypos += 1;
		return *this;
	}
	Point& operator-()
	{
		xpos *= -1;
		ypos *= -1;
		return *this;

		//Point pos(-xpos, -ypos);
		//return pos;
	}
	friend Point& operator--(Point &ref);
	friend Point& operator~(Point &);
};

Point& operator--(Point &ref)
{
	ref.xpos -= 1;
	ref.ypos -= 1;
	return ref;
}

Point& operator~ (Point &ref)
{
	int temp = ref.xpos;
	ref.xpos = ref.ypos;
	ref.ypos = temp;
	return ref;

	//Point pos(ref.ypos, ref.xpos);
	//return pos;
}

int main(void)
{
	Point pos(1,2);
	pos.ShowPosition();
	
	Point pos2 = -pos;
	pos2.ShowPosition();

	(~pos2).ShowPosition();
	pos2.ShowPosition();

	return 0;
}
