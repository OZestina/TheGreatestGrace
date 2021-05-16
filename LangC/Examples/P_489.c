//UnionMemAlloc.c

#include <stdio.h>

typedef struct sbox
{
	int mem1;
	int mem2;
	double mem3;
} Sbox;

typedef union ubox
{
	int mem1;
	int mem2;
	double mem3;
} Ubox;

int main(void)
{
	Sbox sbx;
	Ubox ubx;
	printf("%p %p %p \n", &sbx.mem1, &sbx.mem2, &sbx.mem3);
	printf("%p %p %p \n", &ubx.mem1, &ubx.mem2, &ubx.mem3);
	printf("%d %d \n", sizeof(Sbox), sizeof(Ubox));
	return 0;
}
