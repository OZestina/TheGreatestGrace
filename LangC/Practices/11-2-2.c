#include <stdio.h>

int main(void)
{
	char str[15];
	int i=0, j;
	char cha;
	printf("영어 단어를 입력하세요: ");
	scanf("%s", str);

	while(str[i]!='\0')
		i++;

	for(j=0; j <= (i-1)/2; j++)
	{
		cha = str[j];
		str[j] = str[i-j-1];
		str[i-j-1] = cha;
	}

	printf("%s\n", str);
	return 0;
}
	
