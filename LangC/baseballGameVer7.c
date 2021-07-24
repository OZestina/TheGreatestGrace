//updated 21.07.24

/* Assignment
1) GameScreen 함수 선언으로 Game 함수 간략화
	- Game 함수 내 GameScreen 함수
2) 화면꾸미는 문자를 상수로 설정! 하나만 바꾸면 취향에 맞게 수정 가능!
	- line 14
*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define GAME_OPTION 9
#define icon "#"

int nums[GAME_OPTION];	//컴퓨터 난수 배열 저장
int arr[GAME_OPTION];	//게이머 배열 저장
int list[GAME_OPTION];	//ball 확인 용 리스트

int HowMany(void)
{
	int n;

	printf("몇 개의 숫자로 게임을 진행하겠습니까? (1~9 사이의 수 입력)\n");
	scanf_s("%d", &n);
	while (1)
	{
		if (n >= 1 && n <= 9)
			return n;
		else
		{
			printf("1에서 9 사이의 숫자를 입력하세요.\n");
			while (getchar() != '\n') {}
			scanf_s("%d", &n);
		}
	}
}

void NumMake(int nums[], int list[], int n)
{
	int i, x;

	//random num, list 초기화
	for (i = 0; i < GAME_OPTION; i++)
	{
		nums[i] = 0;
		list[i] = 0;
	}

	for (i = 0; i < n; i++)
	{
		x = rand() % GAME_OPTION + 1;
		while (list[x - 1] != 0)
			x = rand() % GAME_OPTION + 1;
		list[x - 1] = 1;
		nums[i] = x;
	}

}

void GameScreen(int arr[], int strike, int ball, int outt, int n)
{
	int i;

	system("cls");                  //화면 정리용
	for (i = 0; i < 36; i++) { printf("%s", icon); } printf("\n");
	printf("%s                                  %s\n", icon, icon);

	//이전 단계 입력 수 보여주긔
	printf("#  Number: ");
	for (i = 0; i < n; i++)
	{
		printf("%d ", arr[i]);
	}

	for (i = 0; i < 9 - n; i++)
	{
		printf("  ");
	}
	printf("      #\n");
	printf("%s                                  %s\n", icon, icon);
	printf("%s ================================ %s\n", icon, icon);
	printf("%s                                  %s\n", icon, icon);

	//strike
	printf("%s  S : ", icon);
	for (i = 0; i < strike; i++) { printf("●"); }
	for (i = 0; i < (n - strike); i++) { printf("○"); }
	for (i = 0; i < 9 - n; i++) { printf("  "); }
	printf("          %s\n",icon);

	//ball
	printf("%s  B : ", icon);
	for (i = 0; i < ball; i++) { printf("●"); }
	for (i = 0; i < (n - ball); i++) { printf("○"); }
	for (i = 0; i < 9 - n; i++) { printf("  "); }
	printf("          %s\n", icon);

	//out
	printf("%s  O : ", icon);
	for (i = 0; i < outt; i++) { printf("●"); }
	for (i = 0; i < (n - outt); i++) { printf("○"); }
	for (i = 0; i < 9 - n; i++) { printf("  "); }
	printf("          %s\n", icon);
	printf("%s                                  %s\n", icon, icon);
	for (i = 0; i < 36; i++) { printf("%s", icon); } printf("\n");
}

void Game(int arr[], int nums[], int list[], int n)
{
	int strike = 0, ball = 0, outt = 0;
	int num = 0;	//n번째 시도 카운팅
	int i;

	//player num 초기화
	for (i = 0; i < GAME_OPTION; i++)
	{
		arr[i] = 0;
	}

	while (strike != n) {

		if (num == 0) {
			printf("(야구게임) 1~9 사이의 중복되지 않는 숫자의 수열을 맞춰보세요\n");
			printf("%d번째 시도입니다. \n", num + 1);
		}
		else {
			GameScreen(arr, strike, ball, outt, n);
			printf("다시 시도해보세요. %d번째 시도입니다. \n", num + 1);
		}

		for (i = 0; i < n; i++)
		{
			scanf_s("%d", &arr[i]);
		}
		num++;

		strike = 0, ball = 0, outt = 0;		//SBO 초기화
		for (i = 0; i < n; i++)
		{
			if (arr[i] == nums[i])
			{
				strike++;
			}
			else if (list[arr[i] - 1] > 0)
			{
				ball++;
			}
			else
			{
				outt++;
			}
		}
	}//end of while

	//게임 승리 시
	GameScreen(arr, strike, ball, outt, n);
	printf("%d 스트라이크! 축하합니다. \n%d번 만에 성공했어요.\n\n", n, num);
}

int NewGame(void)
{
	char c;

	while (1)
	{
		while (getchar() != '\n') {}
		printf("게임을 다시 하시겠습니까? (y/n)\n");
		scanf_s("%c", &c);

		if (c == 'y')
		{
			printf("게임을 다시 시작합니다.\n\n");
			return 1;
		}
		else if (c == 'n')
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

	while (a)
	{
		system("cls");                  //재게임 시 화면 정리용
		n = HowMany();                  //게임할 숫자 선택
		NumMake(nums, list, n);         //게임용 랜덤 배열 생성
		Game(arr, nums, list, n);		    //게임 진행
		a = NewGame();                  //게임 재 진행 여부 확인
	}

	return 0;
}
