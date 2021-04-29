#include <stdio.h>

int main(void)
{
	char str[15];
	int i=0;
	printf("영어 단어를 입력하세요: ");
	scanf("%s", str);

	while(str[i]!='\0')
		i++;

	printf("입력한 영어 단어의 길이는 %d입니다.\n", i);
	return 0;
}
	
