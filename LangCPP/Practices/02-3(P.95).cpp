//주석처리된 부분에서 선언된 sum은 delete가 안돼서 (cmd 창에서 에러메시지) 일단 제외...

#include <iostream>

typedef struct __Point
{
	int xpos;
	int ypos;
}Point;

Point& PntAdder(const Point &p1, const Point &p2)
{
	Point *ptr = new Point;
	(*ptr).xpos = p1.xpos + p2.xpos;
	ptr->ypos = p1.ypos + p2.ypos;
	return *ptr;
}

int main(void)
{
	Point * d1 = new Point;
	d1->xpos = 10;
	d1->ypos = 3;
	Point * d2 = new Point;
	d2->xpos = 7;
	d2->ypos = 13;
	
	/*Point sum = PntAdder(*d1, *d2);
	std::cout<<"["<<sum.xpos<<", "<<sum.ypos<<"]"<<std::endl;*/

	Point &pref = PntAdder(*d1, *d2);
	std::cout<<"["<<pref.xpos<<", "<<pref.ypos<<"]"<<std::endl;
	
	delete d1;
	delete d2;
	delete &pref;
	/*delete &sum;*/
	
	return 0;
}
