#include <stdio.h>

int GCD(int n1, int n2)
{
	int i;
	if(n1>n2)
	{
		for(i=n2; i>0; i--)
			if (n1%i==0 && n2%i==0)
				return i;
	}
	else
		for(i=n1; i>0; i--)
			if (n1%i==0 && n2%i==0)
				return i;
}
int main(void)
{
	int n1, n2;
	printf("두 개의 정수를 입력하세요: ");
	scanf("%d %d", &n1, &n2);

	printf("%d와 %d의 최대공약수는 %d입니다.\n", n1, n2, GCD(n1, n2));
	return 0;
}
