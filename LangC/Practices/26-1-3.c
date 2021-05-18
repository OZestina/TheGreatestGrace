#include <stdio.h>
#define MAX(x,y)	((x)>(y)? (x) : (y))

int main(void)
{
	int num1, num2;
	printf("Enter 2 numbers: ");
	scanf("%d %d", &num1, &num2);

	printf("%d와 %d 중 더 큰 수는 %d입니다.\n", num1, num2, MAX(num1, num2));
	
	return 0;
}
