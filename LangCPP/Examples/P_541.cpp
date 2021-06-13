//PointClassTemplate.cpp

#include <iostream>
using namespace std;

template <typename T>
class Point
{
private:
	T xpos, ypos;
public:
	Point(T x=0, T y=0): xpos(x), ypos(y) {}
	void ShowPotision() const
	{
		cout<<'['<<xpos<<", "<<ypos<<']'<<endl;
	}
};

int main(void)
{
	Point<int> pos1(3,4);
	pos1.ShowPotision();

	Point<double> pos2(2.4, 3.6);
	pos2.ShowPotision();

	Point<char> pos3('P', 'F');
	pos3.ShowPotision();
	return 0;
}
