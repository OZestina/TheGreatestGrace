//SimpleAddFour.c
//scanf 함수 인자로 "주소값!!!!!"을 넣는거 잊지 않긔^^... &붙이자!

#include <stdio.h>

int main(void)
{
	int result;
	int num1, num2, num3;

	printf("세 개의 정수 입력: ");
	scanf("%d %d %d",&num1, &num2, &num3);

	result = num1+num2+num3;
	printf("%d+%d+%d=%d\n", num1, num2, num3, result);
	return 0;
}
