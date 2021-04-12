#include <stdio.h>

int main(void)
{
	int num1 = 9, num2=2;
	printf("%d+%d=%d\n", num1, num2, num1+num2);
	printf("%d-%d=%d\n", num1, num2, num1-num2);
	printf("%d*%d=%d\n", num1, num2, num1*num2);
	printf("%d/%d의 몫=%d (%d가 10진수의 정수를 출력하는 서식문자여서 소숫점 생략)\n" , num1, num2, num1/num2);
	printf("%d/%d의 나머지=%d\n", num1, num2, num1%num2);
	return 0;
}
