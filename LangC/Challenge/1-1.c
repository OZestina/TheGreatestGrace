#include <stdio.h>

int main(void)
{
	int num;

	printf("10진수 정수를 입력하세요: ");
	scanf("%d", &num);

	printf("10진수 정수 %d는 16진수로 %x입니다\n", num, num);
	return 0;
}
