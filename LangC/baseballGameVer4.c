//updated 21.06.27

/* Assignment
1) 9로 하드코딩된 부분 const로 대체
    > const int GAME_OPTION = 9; 로 했다가 안됨
      (배열의 크기는 컴파일타임에 결정되어야 하는데, const 상수는 런타임에 결정돼서 에러가 뜸)
    > #define GAME_OPTION 9 로 진행
      (#define 을 배열 크기에 대응시키는건 컴파일타임에 이루어져서 괜찮음)
      
2) 게임을 반복해서 플레이할 수 있도록 변경
    > srand(time(NULL)); 은 한 번만 불리도록 메인함수 내로 이동
    > 재 게임 여부를 확인하고 그에 맞춰 실행하는 코드를 NewGame() 함수로 만들어서 main 함수 하단에 추가
    > System("cls"); 추가로 재게임 시 깔끔한 화면 그림

*) 게임을 진행할 수(1~9) 입력받는 함수 정의
    >게임 시작할 때 1~9사이의 수만 입력되도록 처리

*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define GAME_OPTION 9

int nums[GAME_OPTION];	//컴퓨터 난수 배열 저장
int getnums[GAME_OPTION];	//게이머 배열 저장
int list[GAME_OPTION];	//ball 확인 용 리스트

int HowMany(void)
{
	int n;

	printf("몇 개의 숫자로 게임을 진행하겠습니까? (1~9 사이의 수 입력)\n");
	scanf_s("%d", &n);
	while(1)
	{
		if (n>=1 && n<=9)
			return n;
		else
		{
			printf("1에서 9 사이의 숫자를 입력하세요.\n");
			while(getchar()!='\n') {}
			scanf_s("%d", &n);
		}
	}
}

void NumMake(int arr[], int list[], int n)
{
	int i, x;
	
	for (i = 0; i < n; i++)
	{
		x = rand() % GAME_OPTION + 1;
		while(list[x - 1] != 0)
			x = rand() % GAME_OPTION + 1;
		list[x - 1] = 1;
		arr[i] = x;
	}
	
	/*
	for (i = 0; i < GAME_OPTION; i++)	//배열 확인용 
		printf("%d ", arr[i]);
	printf("\n");
	*/
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

int NewGame(void)
{
	char c;

	while(1)
	{
		while(getchar() != '\n') { }
		printf("게임을 다시 하시겠습니까? (y/n)\n");
		scanf_s("%c", &c);
				
		if (c == 'y')
		{
			printf("게임을 다시 시작합니다.\n\n");
			return 1;
		}
		else if(c=='n')
		{
			printf("게임을 종료합니다.\n");
			return 0;
		}
		else
		{
			printf("y 또는 n을 입력하세요.\n");
		}
	}
}

int main()
{
	int n;      //게임할 숫자 저장용 변수
	int a = 1;	//재게임 여부 확인용 변수

	srand(time(NULL));

	while(a)
	{
		system("cls");                  //재게임 시 화면 정리용
    n = HowMany();                  //게임할 숫자 선택
		NumMake(nums, list, n);         //게임용 랜덤 배열 생성
		Game(getnums, nums, list, n);   //게임 진행
		a = NewGame();                  //게임 재 진행 여부 확인
	}

	return 0;
}
