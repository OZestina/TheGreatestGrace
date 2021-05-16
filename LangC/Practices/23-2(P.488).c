#include <stdio.h>

typedef struct point
{
	int xpos;
	int ypos;
} Point;

typedef struct rectangle
{
	Point pos1;
	Point pos2;
} Rectangle;

void Area (Rectangle ra)
{
	printf("직사각형의 넓이: %d \n", (ra.pos2.xpos-ra.pos1.xpos)*(ra.pos2.ypos-ra.pos1.ypos));
}

void PrintPoints (Rectangle ra)
{
	printf("점 1: [%3d, %3d]\n", ra.pos1.xpos, ra.pos1.ypos);
	printf("점 2: [%3d, %3d]\n", ra.pos1.xpos, ra.pos2.ypos);
	printf("점 3: [%3d, %3d]\n", ra.pos2.xpos, ra.pos2.ypos);
	printf("점 4: [%3d, %3d]\n", ra.pos2.xpos, ra.pos1.ypos);
}

int main(void)
{
	Rectangle ra1 = {{0,0}, {100,100}};
	Rectangle ra2 = {{1,1}, {4,4}};
	Rectangle ra3 = {{0,7}, {7,5}};

	Area(ra1);
	PrintPoints(ra1);
	Area(ra2);
	PrintPoints(ra2);
	Area(ra3);
	PrintPoints(ra3);
	return 0;
}
