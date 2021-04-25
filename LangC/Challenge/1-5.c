#include <stdio.h>

int Prime(int n)
{
	int i=(n/2);
	if (n==2)
		return 2;
	else if (n==3)
		return 3;
	else
		while(i>1)
		{
			if (n%i == 0)
				return 1;
			else
				i--;
		}
	
	return n;
}

int main (void)
{
	int i=0, num=2;
	
	while (i<10)
	{
		if(Prime(num)==num)
		{
			printf("%d \n", num);
			num++;
			i++;
		}
		else
			num++;
	}

	printf("\n");

	return 0;
}
