#include <stdio.h>

void SD(const int * ptr)
{
	int * rptr = ptr;
	printf("%d\n", *rptr);
	*rptr = 20;
}
int main(void)
{
	int num = 10;
	int * ptr = &num;
	SD(ptr);
	printf("%d\n", num);
	return 0;
}
