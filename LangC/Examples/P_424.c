//WriteString.c

#include <stdio.h>

int main(void)
{
	char*str="Simple String";

	printf("1. puts test ------ \n");
	puts(str);
	puts("So Simple string");

	printf("2. fputs test ----- \n");
	fputs(str, stdout); printf("\n");
	fputs("So Simple string", stdout); printf("\n");

	printf("3. end of main ----\n");

	return 0;
}
