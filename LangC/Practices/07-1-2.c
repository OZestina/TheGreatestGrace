#include <stdio.h>

int main(void)
{
	int i=0, num;
	printf("양의 정수를 입력하세요: ");
	scanf("%d", &num);

	while(i<num)
	{
		printf("%d ", (i+1)*3);
		i++;
	}
	printf("\n");

	return 0;
}
