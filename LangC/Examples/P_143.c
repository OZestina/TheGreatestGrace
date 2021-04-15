//FieldWidth.c

#include <stdio.h>

int main(void)
{
	printf("%-8s %14s %5s \n", "이  름", "전공학과", "학년");
	printf("%-8s %14s %5d \n", "홍길동", "전자공학", 3);
	printf("%-8s %14s %5d \n", "이을수", "컴퓨터공학", 2);
	printf("%-8s %14s %5d \n", "김예빈", "건축학", 4);
	return 0;
}
