//SimpleWhile.c

#include <stdio.h>

int main(void)
{
	int num=0;

	while(num<5)
	{
		printf("Hello world! %d \n", num);
		num++;
	}
	return 0;
}

//반복의 대상이 한 줄일 경우 중괄호 생략 가능
//num++은 라인 이후에 +1되는거니까 이렇게도 쓸 수 있구나!

#include <stdio.h>

int main(void)
{
	int num=0;

	while(num<5)
		printf("Hello world! %d \n", num++);
	
	return 0;
}
