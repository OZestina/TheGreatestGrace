//TriplePointer.c

#include <stdio.h>

int main(void)
{
	int num=100;
	int *ptr=&num;
	int **dptr=&ptr;
	int ***tptr=&dptr;

	printf("%d %d %d %d \n", num, *ptr, **dptr, ***tptr);
	return 0;
}
