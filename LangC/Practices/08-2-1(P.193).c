//문제를 보고 직관적으로 떠올린^^;; continue와 break를 쓰지 "않는" 방법

#include <stdio.h>

int main(void)
{
	int dan, num;
	for(dan=2; dan<9; dan+=2)
	{
		for(num=1; num<=dan; num++)
			printf("%d x %d = %d\n", dan, num, dan*num);
		printf("\n");
	}
	return 0;
}

//2nd try with continue & break

#include <stdio.h>

int main(void)
{
	int dan=2, num=1;
	
	while (1)
	{
		if (dan%2!=0)
		{
			dan++;
			continue;
		}
		if (dan>9)
			break;
		for(num=1; num<=dan; num++)
			printf("%d x %d = %d\n", dan, num, dan*num);
		printf("\n");
		dan++;
	}
	return 0;
}


//답지

#include <stdio.h>

int main(void)
{
	int i, j;
	for(i=1; i<10; i++)
	{
		if(i%2!=0)
			continue;
		
		for(j=1; j<10; j++)
		{
			if(i<j)
				break;
			printf("%d x %d = %d\n", i, j, i*j);
		}
		printf("\n");
	}
	return 0;
}
