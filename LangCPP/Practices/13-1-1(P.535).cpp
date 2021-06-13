#include <iostream>
using namespace std;


class Point
{
private:
	int xpos, ypos;
public:
	Point(int x=0, int y=0): xpos(x), ypos(y) { }
	void ShowPosition()
	{
		cout<<'['<<xpos<<", "<<ypos<<']'<<endl;
	}
};

template <class T>
void SwapData(T& data1, T& data2)
{
	T temp= data1;
	data1=data2;
	data2=temp;
}

int main(void)
{
	Point pos1(3,5);
	Point pos2(2,4);
	SwapData(pos1, pos2);

	pos1.ShowPosition();
	pos2.ShowPosition();
	return 0;
}
