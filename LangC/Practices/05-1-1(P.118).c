#include <stdio.h>

int main()
{
	int num1, num2, num3, num4;
	int area;
	printf("좌 하단의 x, y 좌표: ");
	scanf("%d %d", &num1, &num2);
	printf("우 상단의 x, y 좌표: ");
	scanf("%d %d", &num3, &num4);

	area = (num3-num1)*(num4-num2);
	printf("두 점이 이루는 직사각형의 넓이는 %d입니다.\n", area);

	return 0;
}
