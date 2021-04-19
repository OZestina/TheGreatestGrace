#include <stdio.h>

int main(void)
{
	int num;
	for (num=1; num<100; num++)
		if (num%7 ==0 || num%9 ==0)
			printf("%d \n", num);

	return 0;
}


//또 다른 방법 (line 7 변형)
// !연산자는 참 <-> 거짓 변경. 나머지로 0이 반환될 때 if문의 조건이 참이 되게 하는 방법.

#include <stdio.h>

int main(void)
{
	int num;
	for (num=1; num<100; num++)
		if ( !(num%7) || !(num%9) )
			printf("%d \n", num);

	return 0;
}
