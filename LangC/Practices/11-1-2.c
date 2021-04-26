#include <stdio.h>

int main(void)
{
	char sen[] = {"Good time"};
	int i;

	for(i=0; i<sizeof(sen); i++)
		printf("%c", sen[i]);
	printf("\n");
	return 0;
}
