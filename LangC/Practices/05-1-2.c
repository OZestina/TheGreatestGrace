#include <stdio.h>

int main()
{
	double num1, num2;
	printf("두 개의 실수를 입력하세요: ");
	scanf("%lf %lf", &num1, &num2);

	printf("%f + %f = %f\n", num1, num2, num1+num2);
	printf("%f - %f = %f\n", num1, num2, num1-num2);
	printf("%f * %f = %f\n", num1, num2, num1*num2);
	printf("%f / %f = %f\n", num1, num2, num1/num2);
	printf("%d\n", sizeof(num1+num2));
	return 0;
}
