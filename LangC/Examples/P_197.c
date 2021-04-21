//AdvanEnglishSchool.c

#include <stdio.h>

int main(void)
{
	char sel;
	printf("M 오전, A 오후, E 저녁\n");
	printf("입력: ");
	scanf("%c", &sel);

	switch(sel)
	{
	case 'M': case 'm': //이렇게 한 줄에도 표시 가능(case 레이블이 묶여있는 것처럼 하려면)
		printf("Morning\n");
		break;
	case 'A':
	case 'a':
		printf("Afternoon\n");
		break;
	case 'E':
	case 'e':
		printf("Evening\n");
		break;
	default:
		printf("I don't know!\n");
	}

	return 0;
}
