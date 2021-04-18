#include <stdio.h>

int main(void)
{
	int dan, i=9;
	printf("몇 단을 출력하겠습니까?: ");
	scanf("%d", &dan);

	while (i != 0)
	{
		printf("%d x %d = %d\n", dan, i, dan*i);
		i--;
	}
	return 0;
}
