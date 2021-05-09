//2021.05.09
//포인터 복습 완료. 하지만 현생이 바빠서 포인터랑 썸 그만 타기로 함. 나중에 필요할 때 고백으로 혼내줘야지!

/*
1) 필요한 배열을 전역변수로 선언해 함수 내에서 접근이 가능하게 함.
    - malloc 부분은 아직 복습 전이어서 최대 수(9)만큼 우선 배열 선언하고, 사용자가 입력한 수 만큼만 프린트하도록 했습니다.
2) 난수 생성 함수, 게임 실행 함수 총 2개의 함수 생성.
    - 게임 실행 함수인 Game()을 분할할 필요가 있을까요?
3) 게이머가 플레이할 배열의 길이를 입력하여 진행할 수 있도록 함.
4) 3과 관련해 ball의 카운팅을 더 용이하게 하기 위해 별도의 배열(list)을 생성 (line 19-생성, 70-계산)
    - 더 좋은 방법이 있을까요?
*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int nums[9];	//컴퓨터 난수 배열 저장
int getnums[9];	//게이머 배열 저장
int list[9];	//ball 확인 용 리스트

void NumMake(int arr[], int list[], int n)
{
	srand(time(NULL));

	int i, x;
	
	for (i = 0; i < n; i++)
	{
		x = rand() % 9 + 1;
		while(list[x - 1] != 0)
			x = rand() % 9 + 1;
		list[x - 1] = 1;
		arr[i] = x;
	}
	
	for (i = 0; i < 9; i++)	//배열 확인용 -> 확인 후 삭제 요
		printf("%d ", arr[i]);
	printf("\n");
}

void Game(int arr[], int nums[], int list[], int n)
{
	int strike=0, ball=0, outt=0;
	int num = 1;	//n번째 시도 카운팅
	int i;

	while (strike != n) {

		if (num == 1) {
			printf("(야구게임) 1~9 사이의 중복되지 않는 숫자의 수열을 맞춰보세요\n%d번째 시도입니다. \n", num);
		}
		else {
			printf("%d 스트라이크, %d 볼, %d 아웃, 다시 시도해보세요.\n%d번째 시도입니다. \n", strike, ball, outt, num);
		}

		for (i = 0; i < n; i++)
		{
			scanf_s("%d", &arr[i]);
		}
		num++;

		strike = 0, ball = 0, outt = 0;

		for (i = 0; i < n; i++)
		{
			if (arr[i] == nums[i])
			{
				strike++;
			}
			else if (list[arr[i] - 1] == 1)
			{
				ball++;
			}
			else
			{
				outt++;
			}
		}
	}

	printf("%d 스트라이크! 축하합니다. \n%d번 만에 성공했어요.\n", n, num);
}

int main()
{
	int n;

	printf("몇 개의 숫자로 게임을 진행하겠습니까? (9 이하의 수 입력) ");
	scanf_s("%d", &n);

	NumMake(nums, list, n);
	Game(getnums, nums, list, n);

	return 0;
}
