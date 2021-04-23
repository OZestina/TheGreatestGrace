//LocalValHideVal.c

#include <stdio.h>

int main(void)
{
	int num=1;

	if(num==1)
	{
		int num=7;
		num+=10;
		printf("if문 내 지역번수 num: %d\n", num);
	}
	printf("main함수 내 지역변수 num: %d\n", num);
	return 0;
}
