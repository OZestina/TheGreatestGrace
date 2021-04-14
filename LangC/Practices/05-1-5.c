#include <stdio.h>

int main(void)
{
	char num1;
	printf("알파벳 문자를 입력하세요: ");
	scanf("%c", &num1);
	printf("입력한 %c의 아스키 코드 값은 %d입니다.\n",num1, num1);
	return 0;
}
