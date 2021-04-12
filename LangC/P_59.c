//OperatorTwo.c
//복합 대입 연산자-추가로 더 해봄!

#include <stdio.h>

int main(void)
{
	int num1=2, num2=4, num3=6, num4 = 8, num5=9;
	num1 += 3;
	num2 -= 2;
	num3 *=4;
	num5 /=2;
	num4 %=5;
	printf("%d %d %d %d %d\n", num1, num2,num3,num4,num5);
	return 0;
}
