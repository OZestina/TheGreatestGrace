//PrintOutput.c
//line10~12의 printf는 일단 프린트함 (ㅋㅋ)
//line13의 num1, num2의 값은 printf로 반환되는 문자열의 길이(\n 포함)를 반환한다.

#include <stdio.h>

int main(void)
{
	int num1, num2, num3;
	num1=printf("12345\n");
	num2=printf("I love myself\n");
	num3=printf("어디 이게 나오는 지 보자\n");
	printf("%d %d \n", num1, num2);
	return 0;
}
