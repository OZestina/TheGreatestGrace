#include <stdio.h>

int main(void)
{
	int arr[5];
	int i, max, min, sum=0;

	printf("다섯 개의 정수 입력: ");
	scanf("%d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4]);
	
	max=arr[0];
	min=arr[0];
	sum=arr[0];

	for(i=1; i<5; i++)
	{
		if (max < arr[i])
			max = arr[i];

		if (min > arr[i])
			min = arr[i];
		
		sum += arr[i];
	}

	printf("입럭한 정수 중 최댓값은 %d입니다.\n", max);
	printf("입럭한 정수 중 최솟값은 %d입니다.\n", min);
	printf("입럭한 정수의 합은 %d입니다.\n", sum);

	return 0;
}
