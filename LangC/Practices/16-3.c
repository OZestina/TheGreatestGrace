//2nd try - 답지 방법
//점수 입력과 성적 합계를 함수로 뺌!

#include <stdio.h>
int arr[5][5];

//entering grade
void Write(void)
{
	int sum;
	int i, j;
	for(i=0; i<4; i++)
	{
		sum=0;
		printf("%d번째 학생의 성적 입력\n", i+1);
		for(j=0; j<4; j++)
		{
			printf("과목 %d:", j+1);
			scanf("%d", &arr[i][j]);
			sum += arr[i][j];
		}
		arr[i][4] = sum;
	}
}

//과목별 성적 합계 입력
void Sum(void)
{
	int sum=0;
	int i, j;

	for (i=0; i<5; i++)
	{
		sum=0;
		for(j=0; j<4; j++)
		{
			sum += arr[j][i];
		}
		arr[4][i] = sum;
	}
}

int main(void)
{
	int i, j;

	Write();
	Sum();

	for(i=0; i<5; i++)
	{
		for(j=0; j<5; j++)
			printf("%2d ", arr[i][j]);
		printf("\n");
	}
	return 0;
}



//1st try - 내 방법
#include <stdio.h>

int main(void)
{
	int i, j;
	int arr[5][5] = {0};

	//입력
	for(i=0; i<4; i++)
	{
		printf("국어, 영어, 수학, 국사 순으로 성적 입력: ");
		for(j=0; j<4; j++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	//총점 구하기
	for(i=0; i<4; i++)
		for(j=0; j<4; j++)
			arr[i][4] += arr[i][j];
	
	//과목별 총점
	for(i=0; i<4; i++)
		for(j=0; j<5; j++)
			arr[4][j] += arr[i][j];

	//print
	for(i=0; i<5; i++)
	{
		for(j=0; j<5; j++)
			printf("%2d ", arr[i][j]);
		printf("\n");
	}

	return 0;
}
