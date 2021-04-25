#include <stdio.h>

int Sq(int n)
{
	if (n==1)
		return 2;
	else
		return 2*Sq(n-1);
}

int main(void)
{
	int n;
	printf("정수 입력: ");
	scanf("%d", &n);

	printf("2의 %d승은 %d\n", n, Sq(n));
	return 0;
}
