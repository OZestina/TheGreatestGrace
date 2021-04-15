//LiteralSize.c

//문자 'A'의 크기는 4이지만, 문자 'A'를 대입한 char 변수 ch의 크기는 1이다.

#include <stdio.h>

int main()
{
	char ch = 'A';
	printf("literal int size: %d\n", sizeof(7));        //4
	printf("literal double size: %d\n", sizeof(7.14));  //8
	printf("literal char size: %d\n", sizeof('A'));     //4
	printf("char variable size: %d\n", sizeof(ch));     //1
	return 0;
}
