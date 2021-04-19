#include <stdio.h>

int main(void)
{
	int num1, num2, abs;
	printf("정수 두 개를 입력하세요: ");
	scanf("%d %d", &num1, &num2);

	abs = num1>num2? num1-num2 : num2-num1;
	printf("두 수의 차는 %d입니다.\n", abs);
	
	return 0;
}
