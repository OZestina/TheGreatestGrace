//MacroFunction.c

#include <stdio.h>

#define SQUARE(x)	x*x

int main(void)
{
	int num=20;

	printf("Square of num: %d \n", SQUARE(num));
	printf("Square of -5: %d \n", SQUARE(-5));
	printf("Square of 2.5: %g \n", SQUARE(2.5));
	printf("Square of 3+2: %d \n", SQUARE(3+2));

	return 0;
}
