//문제 이해를 잘 하지 못하여 다시 풀었고, 맞았음!

#include <stdio.h>

void MaxAndMin (int arr[], int len, int**max, int**min)
{
	int i;
	*max = &arr[0];
	*min = &arr[0];
	for (i=1; i<len; i++)
	{
		if(**max < arr[i])
		{
			*max = &arr[i];
		}
		if(**min > arr[i])
		{
			*min = &arr[i];
		}
	}
}

int main(void)
{
	int *maxPtr;
	int *minPtr;
	int arr[5] = {3,2,5,1,4};

	MaxAndMin (arr, sizeof(arr)/sizeof(int), &maxPtr, &minPtr);

	printf("max: %d, min: %d\n", *maxPtr, *minPtr);

	printf("max: %p, min: %p\n", &arr[2], &arr[3]);
	printf("max: %p, min: %p\n", maxPtr, minPtr);

	return 0;
}
