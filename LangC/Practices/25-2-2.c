//더 많은 문제를 보고 더 많이 흡수합시당

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int arrlen=5;
	int idx=0, j;
	int* arr = (int*)malloc(sizeof(int)*arrlen);

	while(1)
	{
		printf("정수를 입력하세요: ");
		scanf("%d", &arr[idx]);
		if(arr[idx]==-1)
			break;

		if(arrlen==idx+1)
		{
			arrlen += 3;
			arr = (int*)realloc(arr, sizeof(int)*arrlen);
		}
		
		idx++;
	}
		
	for(j=0; j<idx; j++)
	{
		printf("%d ", arr[j]);
	}
	free(arr);
	return 0;
}
