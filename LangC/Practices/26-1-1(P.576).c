#include <stdio.h>
#define ADD(x,y,z)		((x)+(y)+(z))
#define MULTI(x,y,z)	((x)*(y)*(z))

int main(void)
{
	int num1, num2, num3;
	printf("Enter 3 numbers: ");
	scanf("%d %d %d", &num1, &num2, &num3);

	printf("%d + %d + %d = %d \n", num1, num2, num3, ADD(num1,num2,num3));
	printf("%d * %d * %d = %d \n", num1, num2, num3, MULTI(num1,num2,num3));
	return 0;
}
