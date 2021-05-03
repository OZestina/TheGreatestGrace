#include <stdio.h>

int main(void)
{
	int i,j;
	int Dan[3][9] = {
		{2,4,6,8,10,12,14,16,18},
		{3,6,8,12,15,18,21,24,27},
		{4,8,12,16,20,24,28,32,36}
	};

	for(i=0; i<3; i++)
	{
		for(j=0; j<9;j++)
		{
			printf("%d x %d = %d\n", i+2, j+1, Dan[i][j]);
		}
		printf("\n");
	}
	
	return 0;
}

// 답지에서는 구구단 입력도 셀프로 하도록 했다^^... (그래도 됐었네)
// +) 우측 정렬도 추가

#include <stdio.h>

int main(void)
{
	int i,j;
	int Dan[3][9];

	for(i=0; i<3; i++)
	{
		for(j=0; j<9;j++)
		{
			Dan[i][j] = (i+2)*(j+1);
		}
	}

	for(i=0; i<3; i++)
	{
		for(j=0; j<9;j++)
		{
			printf("%d x %d = %2d\n", i+2, j+1, Dan[i][j]);
		}
		printf("\n");
	}
	
	return 0;
}
