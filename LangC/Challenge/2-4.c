#include <stdio.h>

void Palindrome(char * ptr, int len)
{
	int i=0, j=len-1;
	
	for( ; i<len/2; )
	{
		if(ptr[i] != ptr[j])
		{
			printf("회문이 아닙니다.\n");
			return;
		}
		else
			i++; j--;
	}
	printf("회문 입니다.\n");
}

int main(void)
{
	char str[50];
	int i=0;
	printf("문자열 입력; ");
	scanf("%s", str);

	while(str[i] != '\0')
	{
		i++;
	}

	Palindrome(str, i);

	return 0;
}
