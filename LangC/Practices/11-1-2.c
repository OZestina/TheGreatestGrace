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

//답지

#include <stdio.h>

int main(void)
{
	char sen[] = {'G','o','o','d',' ','t','i','m','e'};
	int senLen = sizeof(sen) / sizeof(char);
	int i;

	for(i=0; i<senLen; i++)
		printf("%c", sen[i]);
	printf("\n");
	printf("%d", sizeof(sen));
	return 0;
}
