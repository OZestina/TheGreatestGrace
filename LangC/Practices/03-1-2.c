#include <stdio.h>

int main(void)
{
	int num1, num2, num3;
	
	printf("세 개의 정수를 입력하세요: ");
	scanf("%d %d %d", &num1, &num2, &num3);
	printf("%dx%d+%d=%d\n",num1, num2, num3, num1*num2+num3);
	return 0;
}
