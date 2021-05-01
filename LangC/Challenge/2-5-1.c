#include <stdio.h>

void BubbleSort(int arr[], int len)
{
	int i,j, temp;

	for (j=0; j<len-1; j++)
	{
		for (i=0; i<len-1-j; i++)
		{
			if (arr[i] > arr[i+1])
			{
				temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
				
			}
		}
	}
}

int main(void)
{
	int arr[4] = {3,2,4,1};
	int i;
	
	BubbleSort(arr,sizeof(arr)/sizeof(int));

	for (i=0; i<4; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
