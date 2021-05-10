//1st try

#include <stdio.h>

int main(void)
{
	int ch1, ch2;
	printf("문자를 입력하세요:");
	ch1=getchar();

	if (64<ch1 && ch1<91)
	{
		ch2=ch1+32;
		putchar(ch2);
	}
	else if (96<ch1 && ch1<123)
	{
		ch2=ch1-32;
		putchar(ch2);
	}
	else
		printf("알파벳으로만 입력해주세요.");

	return 0;
}

//2nd try - 답지
#include <stdio.h>

int ConCase(int ch)
{
	int diff = 'a'-'A';
	
	if ('A'<=ch && ch<='Z')
		return ch+diff;
	else if ('a'<=ch && ch<='z')
		return ch-diff;
	else
		return -1;
}

int main(void)
{
	int ch;
	printf("문자를 입력하세요:");
	ch=getchar();

	ch=ConCase(ch);

	if(ch==-1)
	{
		printf("알파벳으로만 입력해주세요.");
		return -1;
	}

	putchar(ch);
	return 0;
}
