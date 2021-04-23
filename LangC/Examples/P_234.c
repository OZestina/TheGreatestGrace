//StaticLocalVariale.c

#include <stdio.h>

void SimpleFunc(void)
{
	static int num1=0;
	int num2=0;
	num1++, num2++;
	printf("static: %d, local: %d\n", num1, num2);
}

void Simple2(void)
{
	static int num1=1;
	num1 *= 5;
	printf("Simple2 static: %d\n", num1);
}
int main(void)
{
	int i;
	for(i=0; i<3; i++)
	{
		SimpleFunc(); 
		Simple2();
	}
		
	return 0;
}
