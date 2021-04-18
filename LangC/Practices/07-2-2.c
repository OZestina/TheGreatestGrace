#include <stdio.h>

int main(void)
{
	int row=0, circle;

	while (row<5)
	{
		circle = row;
		while(circle>0)
		{
			printf("o");
			circle--;
		}
		
		printf("*\n");
		row++;
	}
	return 0;
}
