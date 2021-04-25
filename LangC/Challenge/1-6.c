#include <stdio.h>

int main(void)
{
	int seconds;
	int h, m,s;
	printf("초(second) 입력: ");
	scanf("%d", &seconds);

	h=seconds/3600;
	m=(seconds-3600*h)/60;
	s=seconds-3600*h-60*m;

	printf("[h:%d, m:%d, s:%d]", h, m, s);
	return 0;
}
