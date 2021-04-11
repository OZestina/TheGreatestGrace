#include <stdio.h>

int main(void)
{
	int num1, num2;
	int num3=30, num4 = 40;

	printf("num1: %d, num2: %d \n", num1, num2); //변수를 선언만 하고 초기화하지 않으면 아무 의미가 없는 쓰레기값이 저장된다.
	num1 = 10;
	num2 = 20;

	printf("num1: %d, num2: %d \n", num1, num2);
	printf("num3: %d, num3: %d \n", num3, num4);
	return 0;
}
