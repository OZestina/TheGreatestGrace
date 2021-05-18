//UnivStdNum.c

#include <stdio.h>
//#define STNUM(Y,S,P)	YSP
//#define STNUM(Y,S,P)	Y S P
#define STNUM(Y,S,P)	((Y)*100000+(S)*1000+(P))

int main(void)
{
	printf("학번: %d \n", STNUM(10, 65, 175));
	printf("학번: %d \n", STNUM(10, 65, 077));	//0이 앞에 붙는 숫자는 8진수의 표현을 의미
	return 0;
}
