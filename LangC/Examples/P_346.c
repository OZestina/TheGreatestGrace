//TwoDimArrayInit.c

#include <stdio.h>

int main(void)
{
	int i, j;

	int arr1[3][3] = {
		{1,2,3},
		{4,5,6},
		{7,8,9}
	};

	int arr2[3][3] = {
		{1},
		{4,5},
		{7,8,9}
	};

	int arr[3][3]={1,2,3,4,5,6,7};

	for(i=0; i<3; i++)
	{
		for(j=0; j<3; j++)
			printf("%d ", arr1[i][j]);
		printf("\n");
	}

	for(i=0; i<3; i++)
	{
		for(j=0; j<3; j++)
			printf("%d ", arr2[i][j]);
		printf("\n");
	}

	for(i=0; i<3; i++)
	{
		for(j=0; j<3; j++)
			printf("%d ", arr[i][j]);
		printf("\n");
	}

	return 0;
}
