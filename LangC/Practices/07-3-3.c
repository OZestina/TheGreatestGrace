//출력 시 서식 지정도 해봄!

#include <stdio.h>
int main(void)
{
	int dan=2, num;

	do
	{
		num=1;
		do
		{
			printf("%d x %d = %2d\n", dan, num, dan*num);
			num++;
		}while(num<10);
		dan++;
		printf("\n");

	}while(dan<10);

	return 0;
}
