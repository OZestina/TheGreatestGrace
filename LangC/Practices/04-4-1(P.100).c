#include <stdio.h>

int main(void)
{
	int num1, num2;
	printf("정수를 입력하세요: ");
	scanf("%d", &num1);

	num2=~num1+1;
	printf("입력받은 정수의 부호를 바꾸면 %d입니다.\n", num2);

	return 0;
}
