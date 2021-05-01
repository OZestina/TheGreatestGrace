#include <stdio.h>

int SquareByValue(int num)
{
	return num*num;
}

void SquareByReference(int* ptr)
{
	*ptr = (*ptr)*(*ptr);
}

int main(void)
{
	int num=2;
	printf("%d\n", SquareByValue(num));

	SquareByReference(&num);
	printf("%d\n", num);

	return 0;
}
