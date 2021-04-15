//OperatorSeven.c
// !(NOT) 논리 연산자 낯설다...

#include <stdio.h>

int main(void)
{
	int num1=10;
	int num2=12;
	int num3=0;
	int result1, result2, result3, result4, result5;

	result1=(num1==10 && num2==12);
	result4=(num1==11 && num2==12);
	result2=(num1<12 || num2 >12);
	result3=(!num1);
	result5=(!num3);

	printf("result1: %d\n", result1);
	printf("result4: %d\n", result4);
	printf("result2: %d\n", result2);
	printf("result3: %d\n", result3);
	printf("result5: %d\n", result5);
	return 0;

}
