#include <stdio.h>

void Binary(int num)
{
	long long bin=0;
	long long i=0, ten=1;
	while(num > 1)
	{
		bin += (num%2)*(ten);
		ten *= 10;
		num = num/2;
	}
	i=ten + bin;
	printf("%lld\n", i);
}
int main(void)
{
	int num, i=1;
	
	printf("10진수 정수 입력: ");
	scanf("%d", &num);

	Binary(num);
	return 0;
}
