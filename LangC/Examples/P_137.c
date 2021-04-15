//FormPrintf.c

#include <stdio.h>

int main()
{
	int age;
	printf("당신의 나이를 입력하세요: ");
	scanf("%d", &age);
	printf("당신의 나이는 10진수로 %d살, 16진수로 %X살입니다.\n", age, age);
	printf("당신의 나이는 10진수로 %d살, 16진수로 %x살입니다.\n", age, age);
	return 0;
}
