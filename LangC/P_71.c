//SimpleAddThree.c
//포인터를 써야하는 scanf! 

/*
입력되는 서식문자에는 왜 쌍따옴표가 필요하고, 왜 저장하는 변수는 주소값으로 써야 할까? 
언젠간 이해할 수 있을까...
후... 포인터 너란 녀석...
*/

#include <stdio.h>
int main(void)
{
	int result;
	int num1, num2;

	printf("정수 one: ");
	scanf("%d", &num1);
	printf("정수 two: ");
	scanf("%d", &num2);

	result = num1+num2;
	printf("%d + %d = %d\n", num1, num2, result);
	return 0;
}
