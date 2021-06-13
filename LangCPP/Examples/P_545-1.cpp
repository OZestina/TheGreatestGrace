//PointMain.cpp

#include <iostream>
#include "PointTemplate.h"
using namespace std;

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
