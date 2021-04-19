#include <stdio.h>

int main(void)
{
	int num;
	int i, total=1;
	
	printf("팩토리얼 값을 계산할 정수를 입력하세요: ");
	scanf("%d", &num);

	for (i=num; i>0; i--)
	{
		total *= i;
	}

	printf("%d의 팩토리얼 값은 %d입니다. \n", num, total);
	return 0;
}


//2nd try
//변수 2개만 가지고 해봄

#include <stdio.h>

int main(void)
{
	int num;
	int total=1;
	
	printf("팩토리얼 값을 계산할 정수를 입력하세요: ");
	scanf("%d", &num);

	for (; num>0; num--)
	{
		total *= num;
	}

	printf("팩토리얼 값은 %d입니다. \n", total);
	return 0;
}
