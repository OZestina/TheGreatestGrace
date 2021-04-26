//ScanfConvOne.c

#include <stdio.h>

int main(void)
{
	int num1, num2, num3;
	printf("세 개의 정수 입력: ");
	scanf("%d %o %x", &num1, &num2, &num3);

	printf("입력된 정수 10진수 출력: %d %d %d \n", num1, num2, num3);

	printf("num1의 10, 8, 16진수 출력: %d %o %x\n", num1, num1, num1);
	return 0;
}
