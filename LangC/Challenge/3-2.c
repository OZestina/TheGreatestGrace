//달팽이 배열

#include <stdio.h>

int main(void)
{
	int i, j;
	int k=1, sum=1;
	int size;
	int x=0, y=0;

	int arr[15][15] = {0, }; //0을 하나라도 넣어두면 빈 칸은 자동으로 0으로 채워진다

	printf("출력하고 싶은 달팽이 배열의 크기를 입력하세요: ");
	scanf("%d", &size);

	for(i=0; i<size; i++)
	{
		arr[x][y] = sum++;
		y += k;
	}

	y -= k;	//arr[0][5] -> arr[0][4]
	
	for(i=0; i<size-1; i++)
	{
		for(j=0; j<(size-1-i); j++)
		{
			x=x+k;
			arr[x][y] = sum++;
		}

		k *= -1;

		for(j=0; j<(size-1-i); j++)
		{
			y=y+k;
			arr[x][y] = sum++;
		}
	}

	for(i=0; i<size; i++)
	{
		for(j=0; j<size; j++)
			printf("%2d ", arr[i][j]);
		printf("\n");
	}

	return 0;
}
