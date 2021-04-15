//UsingPS.c

#include <stdio.h>

int main(void)
{
	char ch1 = 'A', ch2 = 'AZ';
	printf("%s %s %s \n","AAA", "BBB", "CCC");
	printf("%c, %d\n", ch1, ch1);			//됨
	printf("%s, %c, %d\n", ch1, ch1, ch1);	//안됨
	printf("%c, %d\n", ch2, ch2);			//안됨
	printf("%s, %c, %d\n", ch2, ch2, ch2);	//안됨
	return 0;
}
