//MacroOpToString.c

#include <stdio.h>
#define STR(A, B)	#A"의 직업은 "#B"입니다."

int main(void)
{
	printf("%s \n", STR(이동춘, 나무꾼));
	printf("%s \n", STR(김갑을,장사꾼));
	return 0;
}
