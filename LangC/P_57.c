#include <stdio.h>

int main(void)
{
	int num1 = 9, num2=2;
	printf("%d+%d=%d\n", num1, num2, num1+num2);
	printf("%d-%d=%d\n", num1, num2, num1-num2);
	printf("%d*%d=%d\n", num1, num2, num1*num2);
	printf("%d/%d의 몫=%d (변수가 int로 선언돼서 소숫점 저장 못함)\n" , num1, num2, num1/num2);
	printf("%d/%d의 나머지=%d\n", num1, num2, num1%num2);
	return 0;
}
