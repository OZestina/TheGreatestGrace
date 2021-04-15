//RealNumOutput.c

#include <stdio.h>

int main()
{
	double num1 = 0.1234, num2 = 0.12345678;
	long double num = 0.12345678;
	printf("f: %f\n", num1);
	printf("e: %e\n", num1);
	printf("E: %E\n", num1);
	
	printf("f: %f\n", num2);
	printf("e: %e\n", num2);
	printf("E: %E\n", num2);

	printf("lf: %lf\n", num);
	printf("Lf: %Lf\n", num);
	return 0;
}
