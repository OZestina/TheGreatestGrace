#include <stdio.h>

int main()
{
	int num1, num2;
	printf("정수 두개를 입력하세요: ");
	scanf("%d %d", &num1, &num2);
	printf("%d를 %d로 나눈 몫은 %d, 나머지는 %d입니다.\n", num1, num2, num1/num2, num1%num2);
	return 0;
}
