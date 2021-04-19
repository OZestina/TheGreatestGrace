#include <stdio.h>

int main(void)
{
	int num1, num2;
	int i, total=0;
	
	printf("두 개의 정수를 입력하세요: ");
	scanf("%d %d", &num1, &num2);

	for (i=num1; i<num2+1; i++)
	{
		total += i;
	}

	printf("%d와 %d 사이의 정수의 합은 %d입니다. \n", num1, num2, total);
	return 0;
}
