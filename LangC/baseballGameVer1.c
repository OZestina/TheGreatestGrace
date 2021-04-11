//야구게임 (2021.04.09 새벽)

#include <stdlib.h>  //하단의 system을 위해 추가한 것 + rand함수 사용을 위해 필요!
#include <stdio.h>
#include <time.h>


int main()
{
	int num1, num2, num3;
	int getNum1, getNum2, getNum3;
	int strike=0, ball=0, outt=0;
	int num = 0;
	
	srand(time(NULL));
	num1 = rand() % 9 + 1;
	num2 = rand() % 9 + 1;
	num3 = rand() % 9 + 1;

	while (num1 == num2) {
		num2 = rand() % 9 + 1;
	}

	while (num1 == num3 || num2 == num3) {
		num3 = rand() % 9 + 1;
	}

	/*printf("%d %d %d \n", num1, num2, num3);*/ 

	while (strike != 3) {

		if (num == 0) {
			printf("(야구게임) 1~9 사이의 중복되지 않는 숫자의 수열을 맞춰보세요\n%d번째 시도입니다. \n", num+1);
		}
		else {
			printf("%d 스트라이크, %d 볼, %d 아웃, 다시 시도해보세요.\n%d번째 시도입니다. \n", strike, ball, outt, num);
		}

		scanf_s("%d %d %d", &getNum1, &getNum2, &getNum3);
		num++;

		strike = 0, ball = 0, outt = 0;

		//getNum1
		if (getNum1 == num1)
			strike++;
		else if (getNum1 == num2 || getNum1 == num3)
			ball++;
		else
			outt++;
		//getNum2
		if (getNum2 == num2)
			strike++;
		else if (getNum2 == num1 || getNum2 == num3)
			ball++;
		else
			outt++;
		//getNum3
		if (getNum3 == num3)
			strike++;
		else if (getNum3 == num2 || getNum3 == num1)
			ball++;
		else
			outt++;

	}
		
	if (strike == 3)
		printf("3 스트라이크! 축하합니다. \n%d번 만에 성공했어요.\n", num);
	
	
	system("pause"); //ctrl+F5 시 "아무 키나 누르세요~" 문장이 말미에 나오지 않을 때, 이 문장을 추가하면 나온다~ (근데 standard library 헤더 추가해줘야함)
	return 0;
}
