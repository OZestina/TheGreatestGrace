#include <stdio.h>

void Dan(int n)
{
	int num;
	for(num=1; num<=9; num++)
		printf("%d x %d = %d\n", n, num, n*num);
	printf("\n");
}

int main(void)
{
	int n1, n2, i;
	printf("구구단을 출력하고 싶은 단 2개를 입력하세요: ");
	scanf("%d %d", &n1, &n2);

	if(n1<n2)
		for(i=n1; i<=n2; i++)
			Dan(i);
	else
		for(i=n2; i<=n1; i++)
			Dan(i);

	return 0;
}
