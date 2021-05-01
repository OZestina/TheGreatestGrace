#include <stdio.h>

int main(void)
{
	int arr[10];
	int i=0, temp;
	int j=0, k=9;

	printf("총 10개의 숫자 입력: \n");

	for(i=0; i<10; i++)
	{
		printf("입력 %d: ", i+1);
		scanf("%d", &temp);
		if (temp%2 == 1)
		{
			arr[j] = temp;
			j++;
		}
		else
		{
			arr[k] = temp;
			k--;
		}
	}

	printf("배열 요소의 출력: ");
	for (i=0; i<10; i++)
	{
		printf("%d ", arr[i]);
	}
	printf("\n");

	return 0;
}
