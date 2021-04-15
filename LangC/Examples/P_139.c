//OctHex.c

#include <stdio.h>

int main()
{
	int num1=7, num2=13;
	printf("%o %#o \n", num1, num1);
	printf("%O %#O \n", num1, num1); // 대문자로 하면 안된다^^
	printf("%x %#x \n", num2, num2);
	printf("%X %#X \n", num2, num2);
	return 0;
}
