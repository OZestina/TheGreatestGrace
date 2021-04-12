#include <stdio.h>

int main(void)
{
	int num1, num2;
	int minus, multi;

	printf("두 개의 정수를 입력하세요: ");
	scanf("%d %d", &num1, &num2);
	minus=num1-num2;
	multi=num1*num2;

	printf("%d-%d=%d\n",num1,num2,minus);
	printf("%d*%d=%d\n",num1,num2,multi);
	return 0;
}
