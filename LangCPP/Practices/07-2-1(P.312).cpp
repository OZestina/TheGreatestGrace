#include <iostream>
using namespace std;

class Rectangle
{
private:
	int width;	//가로
	int depth;	//세로
public:
	Rectangle(int w, int d): width(w), depth(d)
	{}
	void ShowAreaInfo() const
	{
		cout<<"면적: "<<width*depth<<endl;
	}
};

class Square: public Rectangle
{
public:
	Square(int w): Rectangle(w, w)
	{}	
};

int main(void)
{
	Rectangle rec(4,3);
	rec.ShowAreaInfo();

	Square sqr(7);
	sqr.ShowAreaInfo();
	return 0;
}
