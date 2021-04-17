
#include <stdio.h>

int main(void)
{
	int i=0, num;
	printf("양의 정수 하나를 입력하세요: ");
	scanf("%d", &num);

	while(i<num)
		printf("Hello world!\n"), i++;

	return 0;
}
