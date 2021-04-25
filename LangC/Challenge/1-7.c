//재귀함수 방법

#include <stdio.h>

int Squared(int n)
{
	if(n==1)
		return 2;
	else
		return 2*Squared(n-1);
}

int main(void)
{
	int n, k, i=1;
	printf("2^k<=n. n의 값(상수)을 입력하면 k의 최댓값을 계산해드립니다.\n");
	printf("n의 값: ");
	scanf("%d", &n);

	if(n==0)
	{
		printf("k에 어떤 수를 넣어도 2^k가 0이 될 수 없습니다.\n");
		return 0;
	}
	else if(n==1)
		k = 0;
	else
		while(1)
		{
			if (Squared(i) < n)
				i++;
			else if (Squared(i) == n)
			{
				k = i; 
				break;
			}
			else
			{
				k = i-1; 
				break;
			}
		}

	printf("공식을 만족하는 k의 최대값은 %d입니다.\n", k);
	return 0;
}

//재귀함수 없이 방법
#include <stdio.h>

int main(void)
{
	int n, k, s=2, i=1;
	printf("2^k<=n. n의 값(상수)을 입력하면 k의 최댓값을 계산해드립니다.\n");
	printf("n의 값: ");
	scanf("%d", &n);

	if(n==0)
	{
		printf("k에 어떤 수를 넣어도 2^k가 0이 될 수 없습니다.\n");
		return 0;
	}
	else if(n==1)
		k = 0;
	else
		while(1)
		{
			if (s == n)
			{
				k=i;
				break;
			}
			else if (s<n)
			{
				i++;
				s = s*2;
			}
			else
			{
				k = i-1; 
				break;
			}
		}

	printf("공식을 만족하는 k의 최대값은 %d입니다.\n", k);
	return 0;
}
