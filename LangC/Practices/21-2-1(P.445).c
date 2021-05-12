#include <stdio.h>
#include <string.h>

int Convo(char c)
{
	static int diff = 1-'1';
	return c+diff;
}

int main(void)
{
	char str[20];
	int i, n, sum=0;
	printf("문자열 입력: ");
	scanf("%s", str);

	n=strlen(str);

	for(i=0; i<n; i++)
	{
		if('1' <= str[i] && str[i] <= '9')
			sum += Convo(str[i]);
	}
	
	printf("%d \n", sum);

	return 0;
}
