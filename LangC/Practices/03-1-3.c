#include <stdio.h>

int main(void)
{
	int num;
	printf("제곱값을 원하는 정수를 입력하세요: ");
	scanf("%d", &num);
	printf("%d의 제곱은 %d입니다.\n", num, num*num);
	return 0;
}
