#include <stdio.h>

void DesSort(int arr[], int len)
{
	int i,j, temp;

	for (j=0; j<len-1; j++)
	{
		for (i=0; i<len-1-j; i++)
		{
			if (arr[i] < arr[i+1])
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
	int arr[7];
	int i;
	
	for(i=0; i<7; i++)
	{
		printf("입력: ");
		scanf("%d", &arr[i]);
	}
	
	DesSort(arr,sizeof(arr)/sizeof(int));

	for (i=0; i<7; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
