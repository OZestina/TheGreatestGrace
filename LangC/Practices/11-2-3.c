#include <stdio.h>

int main(void)
{
	char str[50];
	int i=0, j, max;

	printf("enter word: ");
	scanf("%s", str);
	while(str[i]!='\0')
		i++;

	max=str[0];
	for (j=1; j<i; j++)
		if (str[j]>max)
			max = str[j];
	
	printf("biggest ASCII code: %c\n", max);
	return 0;
}
