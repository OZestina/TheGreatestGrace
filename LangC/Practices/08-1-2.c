#include <stdio.h>

int main(void)
{
	int num1, num2;
	printf("정수 두 개를 입력하세요: ");
	scanf("%d %d", &num1, &num2);

	if(num1>num2)
		printf("두 수의 차는 %d입니다.\n", num1-num2);
	else
		printf("두 수의 차는 %d입니다.\n", num2-num1);

	return 0;
}
