#include <stdio.h>

int main(void)
{
	int num1, num2, num3;
	int result;
	printf("정수 세 개를 입력하세요: ");
	scanf("%d %d %d", &num1, &num2, &num3);
	result=(num1-num2)*(num2+num3)*(num3%num1);
	printf("(%d-%d)*(%d+%d)*(%d %% %d)의 값은 %d입니다.\n",num1, num2, num2, num3, num3, num1, result);
	return 0;
}
